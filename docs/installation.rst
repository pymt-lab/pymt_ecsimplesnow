.. highlight:: shell

============
Installation
============


Stable release
--------------

Installing pymt_ecsimplesnow from the `conda-forge` channel can be achieved by adding
`conda-forge` to your channels with:

.. code::

  conda config --add channels conda-forge

To install pymt_ecsimplesnow, run this command in your terminal:

.. code-block:: console

    $ conda install pymt_ecsimplesnow

This is the preferred method to install pymt_ecsimplesnow, as it will always install the most recent stable release.

If you don't have `conda`_ installed, this `Anaconda installation guide`_ can guide
you through the process.

.. _conda: https://docs.anaconda.com/anaconda/
.. _Anaconda installation guide: https://docs.anaconda.com/anaconda/install/


From sources
------------

The sources for pymt_ecsimplesnow can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/wk1984/pymt_ecsimplesnow

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/wk1984/pymt_ecsimplesnow/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ conda install --file=requirements.txt
    $ python setup.py install


.. _Github repo: https://github.com/wk1984/pymt_ecsimplesnow
.. _tarball: https://github.com/wk1984/pymt_ecsimplesnow/tarball/master
