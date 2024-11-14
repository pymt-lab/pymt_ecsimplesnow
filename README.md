# pymt_ecsimplesnow

[![Basic Model Interface](https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg)](https://bmi.readthedocs.io/)

[![Test](https://github.com/pymt-lab/pymt_ecsimplesnow/actions/workflows/test.yml/badge.svg)](https://github.com/pymt-lab/pymt_ecsimplesnow/actions/workflows/test.yml)

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pymt_ecsimplesnow.svg)](https://anaconda.org/conda-forge/pymt_ecsimplesnow)


PyMT plugin for ECSimpleSnow

- Free software: MIT license
- Documentation: <https://ecsimplesnow.readthedocs.io>.

| Component    |  PyMT
| ---------    |  ----
| ECSimpleSnow |  from pymt.models import ECSimpleSnow

## Installing pymt

Installing pymt from the conda-forge channel
can be achieved by adding conda-forge to your channels with:
``` 
conda config --add channels conda-forge
```

*Note*: Before installing pymt, you may want to create a
separate environment into which to install it. This can be done with,
``` 
conda create -n pymt python=3
conda activate pymt
```

Once the conda-forge channel has been enabled,
pymt can be installed with:
``` 
conda install pymt
```

It is possible to list all of the versions of pymt
available on your platform with:
``` 
conda search pymt --channel conda-forge
```

## Installing pymt_ecsimplesnow

Once pymt is installed, the dependencies of
pymt_ecsimplesnow can be installed with:
``` 
conda install bmi-fortran=1.2 ecsimplesnow
```

To install pymt_ecsimplesnow,
``` 
conda install pymt_ecsimplesnow
```
