project(
    'pymt_ecsimplesnow',
    'fortran',
    'cython',
    version: 'v0.3',
)

py = import('python').find_installation(pure: false)
compiler = meson.get_compiler('fortran', native: true)

python_inc = py.get_path('data') / 'include'
numpy_inc = run_command(
    py,
    [
        '-c',
        'import numpy; print(numpy.get_include())'
    ],
    check: true
).stdout().strip()
incs = include_directories(
    [
        'pymt_ecsimplesnow/lib',
        python_inc,
        numpy_inc,
    ]
)

deps = [
    compiler.find_library('bmif'),
    compiler.find_library('bmisnowf'),
]

# Files get copied to <python directory>/site-packages/<subdir>
install_pkg_srcs = [
    'pymt_ecsimplesnow/__init__.py',
    'pymt_ecsimplesnow/_bmi.py',
    'pymt_ecsimplesnow/_version.py',
]
py.install_sources(
    install_pkg_srcs,
    subdir: 'pymt_ecsimplesnow',
)

install_lib_srcs = [
    'pymt_ecsimplesnow/lib/__init__.py',
    'pymt_ecsimplesnow/lib/ecsimplesnow.pyx',
]
py.install_sources(
    install_lib_srcs,
    subdir: 'pymt_ecsimplesnow/lib',
)
py.extension_module(
    'ecsimplesnow',
    [
        'pymt_ecsimplesnow/lib/bmi_interoperability.f90',
        'pymt_ecsimplesnow/lib/ecsimplesnow.pyx',
    ],
    dependencies: deps,
    include_directories: incs,
    install: true,
    subdir: 'pymt_ecsimplesnow/lib',
)

install_subdir(
    'meta/ECSimpleSnow',
    install_dir: py.get_install_dir() / 'pymt_ecsimplesnow/data',
)

# This is a temporary fix for editable installs.
run_command('cp', '-r', 'pymt_ecsimplesnow/data', 'build')
