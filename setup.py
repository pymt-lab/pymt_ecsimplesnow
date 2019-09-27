#! /usr/bin/env python
import os
import sys
import subprocess
import numpy as np

import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension
from model_metadata.utils import get_cmdclass, get_entry_points

from setuptools.command.build_ext import build_ext as _build_ext
from numpy.distutils.fcompiler import new_fcompiler
from scripting.contexts import cd


common_flags = {
    "include_dirs": [
        np.get_include(),
        os.path.join(sys.prefix, "include"),
    ],
    "library_dirs": [
    ],
    "define_macros": [
    ],
    "undef_macros": [
    ],
    "extra_compile_args": [
    ],
    "language": "c",
}

libraries = [
]

# Locate directories under Windows %LIBRARY_PREFIX%.
if sys.platform.startswith("win"):
    common_flags["include_dirs"].append(os.path.join(sys.prefix, "Library", "include"))
    common_flags["library_dirs"].append(os.path.join(sys.prefix, "Library", "lib"))

ext_modules = [
    Extension(
        "pymt_ecsimplesnow.lib.ecsimplesnow",
        ["pymt_ecsimplesnow/lib/ecsimplesnow.pyx"],
        libraries=libraries + ["bmisnowf"],
        extra_objects=['pymt_ecsimplesnow/lib/bmi_interoperability.o'],
        **common_flags
    ),
]

packages = find_packages()
pymt_components = [(
        "ECSimpleSnow=pymt_ecsimplesnow.bmi:ECSimpleSnow",
        "meta/ECSimpleSnow",
    ),
]


def get_finclude(compiler):
    lib_dir = compiler.library_dirs[0]
    inc_dir = os.path.join(os.path.dirname(lib_dir), "include")
    common_flags["include_dirs"].append(inc_dir)
    
    from glob import glob
    paths = glob(os.path.join(inc_dir, "iso_c_binding.mod"), recursive=True)
    print("*2* {}".format(paths))


def get_fcompiler():
    print("*1* {}".format(sys.platform))
    hint=None
    if sys.platform.startswith("win"):
        hint="flang"
    compiler = new_fcompiler(compiler=hint)
    compiler.customize()
    if sys.platform.startswith("win"):
        get_finclude(compiler)
    print("*3* {}".format(common_flags["include_dirs"]))
    return compiler


def build_interoperability(compiler):
    cmd = []
    cmd.append(compiler.compiler_f90[0])
    cmd.append(compiler.compile_switch)
    if sys.platform.startswith("win") is False:
        cmd.append("-fPIC")
    for include_dir in common_flags['include_dirs']:
        if os.path.isabs(include_dir) is False:
            include_dir = os.path.join(sys.prefix, "include", include_dir)
        cmd.append('-I{}'.format(include_dir))
    cmd.append('bmi_interoperability.f90')

    if sys.platform.startswith("win"):
        cmd = ["flang", "-c", "-v", "bmi_interoperability.f90"]

    print("*4* {}".format(cmd))

    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        raise


class build_ext(_build_ext):

    def run(self):
        compiler = get_fcompiler()
        compiler.dump_properties()
        with cd('pymt_ecsimplesnow/lib'):
            build_interoperability(compiler)
        _build_ext.run(self)


cmdclass = get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass())
cmdclass["build_ext"] = build_ext

setup(
    name="pymt_ecsimplesnow",
    author="Kang Wang",
    description="PyMT plugin for ecsimplesnow",
    version=versioneer.get_version(),
    setup_requires=["cython"],
    ext_modules=ext_modules,
    packages=packages,
    cmdclass=cmdclass,
    entry_points=get_entry_points(pymt_components),
)
