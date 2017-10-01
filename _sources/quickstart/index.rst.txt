===========
Quick Start
===========

Installation
============

Latest version of `doit` requires python 3.4 and newer.

Install via pip (best into activated virtualenv)::

    $ pip install doit

and test version::

    $ doit --version

.. note:: For Python 2.7 use::

    $ pip install doit==0.29.0
    
   Advanced parts of this doc may break in Python 2.7.

Deploy power of your shell commands
===================================

To make our example easy to run on Windows as well as on Linux, we will use
command `echo` redirecting some text into a file::

    $ echo welcome > file.txt
    $ echo dear user >> file.txt
    $ echo enjoy powers of doit >> file.txt

If you used the `>` (overwrite) and `>>` (append) properly, the `file.txt`
shall now have lines::

    welcome
    dear user
    enjoy powers of doit

Let's do something similar by `doit`. Create file `dodo.py`:

.. literalinclude:: /code/quick/echo1.py

The function `task_echo_to_cave` declares the task "echo_to_cave" by means of
returning dictionary with task metadata. The keyword `"actions"` here simply
lists shell commands to call.

First, list all tasks defined in `dodo.py` file by::

    $ doit list
    echo_to_cave   Call holla to cave.txt

File `cave.txt` was not created yet as the task was only listed.

Let's execute it by::

    $ doit run echo_to_cave
    . echo_to_cave

The command reported the task run and executed it.

Check content of the file `cave.txt`::

    pssst
    holla
    olla
    lla
    la
    a

Delete the file `cave.txt` manually and execute the command again but do not
add any `run` or task name::

    $ doit
    . echo_to_cave

By default, `doit` runs all default tasks.

The file `cave.txt` shall be again present and shall have the same content as before.


Parametrize name of target file
================================

Hardcoded file names are not always practical. Let's add `"targets"` keyword into task
declaration and provide it with list of target files names, in this case just one.

Also modify the string to be echoed (adding "parametrized") to see our fingerprint in the new result.

.. literalinclude:: /code/quick/echo_target.py

Call::

    $ doit
    . echo_to_cave

Checking content of the `cave.txt` we shall see::

    parametrized pssst
    parametrized holla
    parametrized olla
    parametrized lla
    parametrized la
    parametrized a

The string of `cmd-action` is (always) interpolated with keyword `targets` (there are
more such keywords). The value for `targets` is takes from task declaration and provided as space
delimited list of file names (so it is single string).

Who is going to clean that?
===========================

Manually deleting files we have created is no fun (imagine you created tens of such files).

`doit` is ready to clean the mess for you. Simply add `"clean"` keyword to task declaration and
provide it with value `True`:

.. literalinclude:: /code/quick/echo_clean.py

This time ask `doit` to do the cleaning work::

    $ doit clean
    echo_to_cave - removing file 'cave.txt'

The file `cave.txt` shall be removed now.

Repeating the last (cleaning) command will not do anything.

Try running the main actions of task `echo_to_cave` again and check, all still works as expected.

Speed up by skipping already done
=================================

Its time to do something real. We will need command `7z` installed in our system. Feel free
to modify this example with your favourite archiving command.

The plan is to automate compressing huge file in such a way, it recreates the archive only when the
source file or target archive has changed.

We will need a file to compress. Best is to use a file, which takes at least few
seconds to compress. Put it into current directory and call it `huge.dat`.

Use `7z` command `a` (add to archive)::

    $ 7z a huge.compressed.7z huge.dat
    7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
    p7zip Version 9.20 (locale=cs_CZ.UTF-8,Utf16=on,HugeFiles=on,4 CPUs)
    Scanning

    Creating archive huge.compressed.7z

    Compressing  huge.dat

    Everything is Ok

File `huge.compressed.7z` shall be now present in our directory.

It's time for automation. Create `dodo.py`:

.. literalinclude:: /code/quick/compress1.py

Remove the `huge.compressed.7z`.

First list the commands available::

    $ doit list
    compress   Compress input file(s)

and then run it::

    $ doit
    .  compress

The archive file shall be created now.

Ask `doit` to do the work again::

    $ doit
    -- compress

Almost zero execution time and `"--"` in front of task name (instead of `"."`) tell us, `doit` saw
no need to repeat the task, whose results are already uptodate.

This will hold true as long as content of input and output files do not change (checked by MD5
checksum).

Assembling mammuth piece by piece
=================================
Real tasks are complex. With `doit`, things can be split to smaller tasks and
executed step by step until required result is completed.

Following example takes one existing file `huge.dat`, creates another two (`python.help` and
`doit.help`) and finally creates `result.7z` containing all three compressed.

.. literalinclude:: /code/quick/connected.py

File dependencies are clearly defined, tasks are well documented::

    $ doit list
    compress      Compress input file(s)
    doit_help     Write doit help string to a file
    python_help   Write python help string to a file

tasks are run when needed::

    $ doit
    .  python_help
    .  doit_help
    .  compress

processing is optimized and run only when necessary::

    $ doit
    .  python_help
    .  doit_help
    -- compress

and to clean is easy::

    $ doit clean
    compress - removing file 'result.7z'
    doit_help - removing file 'doit.help'
    python_help - removing file 'python.help'

If you wonder why tasks `python_help` and `doit_help` are always rerun, the reason is, these tasks
do not have "file_dep" so they are always considered outdated.

Python defined actions
======================

.. todo:: show python actions in action
