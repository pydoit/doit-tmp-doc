======
Howtos
======

.. todo: Elaborate on it.

Topics:

- installation
    - system wide installation on Linux
    - system wide installation on Windows
    - virtualenv installation (incl. doit) in one step

- testing and debugging
- using pathlib, shellutil and tempfile
- checking binaries are available
- simplify cumbersome command line calls
- handle AWS credentials (use profile set by AWS_DEFAULT_PROFILE)
- standardize release of your python package

    - spell, build doc
    - test, coverage
    - bump version, build dist, upload...

- sync deep directory of files with

    - put/update files in directory of files intended to by synced to FTP/AWS S3/...
    - put dodo.py into root of the tree
    - provide tasks:

        - publish
        - fetch
        - sync (will delete on remote what is locally not present)

  - call from anywhere withing the tree using `-k` (`--seek-file`)

- multiple files fetch, convert, merge, filter + publish pattern
- Complete lengthy processing under one second
- Cross platform ZIP operations
- Cross platform tar operations
- Share dodo.py via directory
- Share doit script via pypi

Planning `dodo.py`
==================

- clarify requirements

    - what shall the script do
    - why using doit (speed, orchestration, sharing dodo.py with others...)
    - environment it will run in (local machine, the same OS, multiple OS)

- available tools

    - what shell commands can help use
    - can we fulfill the same with pure python?

- identify possible inputs, intermediate files, outputs, actions and tasks
- flowchart: group actions into tasks
- decide about each action implementation (python-action or cmd-action)
- draft dodo.py: populate stub `task_*` functions incl. docstrings.
- write README.rst (to summarize your plan) and cover:

    - installation

      - method (best use tox based with requirements.txt)
      - draft requirements.txt to specify required python packages
      - draft list of other shell commands required for the script

    - tasks visible to the user
