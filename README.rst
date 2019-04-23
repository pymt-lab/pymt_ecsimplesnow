=================
pymt_ecsimplesnow
=================


.. image:: https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg
        :target: https://bmi.readthedocs.io/
        :alt: Basic Model Interface

.. image:: https://img.shields.io/badge/recipe-pymt_ecsimplesnow-green.svg
        :target: https://anaconda.org/conda-forge/pymt_ecsimplesnow

.. image:: https://img.shields.io/travis/pymt-lab/pymt_ecsimplesnow.svg
        :target: https://travis-ci.org/pymt-lab/pymt_ecsimplesnow

.. image:: https://readthedocs.org/projects/pymt_ecsimplesnow/badge/?version=latest
        :target: https://pymt_ecsimplesnow.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/csdms/pymt
        :alt: Code style: black


PyMT plugin for ECSimpleSnow


* Free software: MIT license
* Documentation: https://ecsimplesnow.readthedocs.io.




============ ======================================
Component    PyMT
============ ======================================
ECSimpleSnow `from pymt.models import ECSimpleSnow`
============ ======================================

---------------
Installing pymt
---------------

Installing `pymt` from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

*Note*: Before installing `pymt`, you may want to create a separate environment
into which to install it. This can be done with,

.. code::

  conda create -n pymt python=3.6
  conda activate pymt

Once the `conda-forge` channel has been enabled, `pymt` can be installed with:

.. code::

  conda install pymt

It is possible to list all of the versions of `pymt` available on your platform with:

.. code::

  conda search pymt --channel conda-forge

----------------------------
Installing pymt_ecsimplesnow
----------------------------



To install `pymt_ecsimplesnow`,

.. code::

  conda install pymt_ecsimplesnow
