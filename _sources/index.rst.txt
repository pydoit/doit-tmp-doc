.. doit documentation master file, created by
   sphinx-quickstart on Thu Sep 28 10:57:03 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=========================
You are welcome to `doit`
=========================

tasks => {doit + shell + python} => done
========================================
Declare your task(s) in `dodo.py`::

    def task_compress():
        """Compress input file(s)"""
        return {
            "actions": [
                "7z a %(targets)s %(dependencies)s",
            ],
            "file_dep": ["lauer.dat", "hardy.dat", "elephant.txt"],
            "targets": ["bigarchive.7z"],
            "clean": True
        }

Install `doit` and go::
    
    $ pip install doit

    $ doit list  # see list of tasks with one-line helpstring
    compress    Compress input file(s)

    $ doit  # run all default tasks
    . compress

    $ doit  # skip doing tasks with results being already uptodate
    -- compress

    $ doit clean  # clean created files
    compress - removing file 'bigarchive.7z'

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents

   usecases/index
   quickstart/index
   tutorials/index
   concepts/index
   reference/index
   howtos/index



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
