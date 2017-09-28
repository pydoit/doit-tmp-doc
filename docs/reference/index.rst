================
Reference Manual
================

.. todo:: list of topics to cover here is still not complete.

Terms and definitions
=====================

.. glossary::

    action
        simple call of shell command or python function. Action can be parametrized and can calculate values usable in other tasks. Actions can be invoked only via tasks.

    task
        invokable named set of actions and other tasks metadata (required inputs, created outputs, clear behaviour...)

    subtask
        task with parametrized name

    task declaration
        the act of providing dictionary of the task metadata.

    target
        a file, which can be created by a task.

    (stateful) file
        any file mentioned in a task declaration as file_dep (task input) or target (task output). doit keeps track of file existency and state (by default using MD5 checksum) between invocations.

    file dependency
        dependency of a file on another one(s). All files in task target are dependent on files in the task "file_dep".

    task dependency
        dependency of one task on another one(s). Explicit task dependency is set by "task_dep" in task declaration. Each task is implicitly dependent via file dependency, thus the task is dependent on all tasks creating files mentioned in it's "file_dep".

    task uptodate evaluation
        the act of evaluating all (explicit and implicit) task dependencies and task uptodate rules with aim to recognize that the task as a whole is uptodate or not.

    task execution
        the act of executing all actions of a task.

    task collection
        the act of collecting all task declarations with aim to get list of invocable tasks and targets.

    invokable target
        the fact, that name of any of files specified in a task's "targets" can be used to invoke the task. Each file from "targets" is invokable.

    python-action
        action defined by means of python function and optionally positional and keyword arguments.

    cmd-action
        action invoked via shell.

    cmd-action string
        cmd-action defined as single string which is supposed to be invoked via shell.

    cmd-action list
        cmd-action defined as list of strings and pathlib file names representing shell command arguments. The cmd-action list is invoked in one shell call.

    (task) main actions
        actions mentioned in task declaration under key "actions", defining the activity creating task results.

    (task) clean actions
        actions mentioned in task declaration under key "clean", defining the activity cleaning task results.

    (task) uptodate actions
        actions mentioned in task declaration under key "uptodate", defining the activity determining, if the task is uptodate.

    result database
        database persisting status of last task execution incl. files from all "file_dep" and "targets" lists.

    DB-backend
        specific technology used to serialize data in result database.

    command run
        doit subcommand used to invoke main task actions

    command clean
        doit subcommand used to invoke clean task actions

    command list
        doit subcommand used to list avaialble tasks and subtasks

    command ignore
        doit subcommand used to temporarily disable check of a task results.

    command forget
        doit subcommand used to remove temporarily disabled check of a task results.

Task execution life-cycle
=========================

Following chart explains simplified task execution lifecycle.

.. uml::
    :caption: Task execution life-cycle
    :scale: 50%
    :align: center

    (*) -->  "declare tasks"
    note right: write dodo.py,\ntask_* functions returning dicts
    -->  collect tasks
    note right: execute `doit list`\nor first part of `doit run`
    -->  evaluate tasks
    note right: `doit run` continues
    -->  execute tasks
    note right: only tasks not uptodate
    --> (*)

`DOIT_CONFIG`
=============
desribe all keys usable in `DOIT_CONFIG`

- default_tasks
- check_file_uptodate (custom file uptodate checker)
- backend
- dep_file
- verbosity
- reporter
- minversion

`dodo.py` file
==============
- it is the default file from which `doit` loads task definitions.
- can have another name, then `doit` must explicitly set it via `-f` option.

action definitions
==================

- cmd-action as string

  - simple string (no interpolation)
  - string with interpolated kwargs
  - `CmdAction(cmd_string_builder_fun)`

    - without any argument
    - with kwargs (dependencies, changed, targets plus custom ones)

  - parsed cmd-action (cmd-action as string)

- python-action

  - just function name (no explicit kwargs)

    - not using implicit kwargs
    - using implicit kwargs

  - function name with args and kwargs

    - not using implicit kwargs
    - using implicit kwargs

actions calculating values
==========================
Actions can calculate values usable by other tasks.

- how to calculate and store value by python-action
- how to calculate and store value by cmd-action (`CmdAction` with `save_out`)

getargs: read values calculated by other tasks
==============================================

.. todo: as in http://pydoit.org/dependencies.html#getargs No discussion about saving values, just
    refer to related section.


action usage scenarios
======================
When can be actions used:

- main actions
- clean actions
- uptodate actions
- ??? some more?

`doit` invocation
=================

- `doit` cli
- `$ python -m doit`
- from iPython
- embed into another python code

.. todo:: Elaborate on it

`doit` command line interface
=============================

.. todo:: Elaborate on it



Task declaration parameters
===========================

- name
- basename
- actions
- file_dep
- targets
- task_dep
- clean
- uptodate
- title
- doc
- verbosity

Task names
==========

- explicit task name
- sub-task name
- implicit task via target reference
- private/hidden tasks

Task selection
==============
- default tasks
- DOIT_CONFIG["default_tasks"]
- multiple task selection by list
- multiple task selection by wildcard
- indirect selection via task dependency

Task dependencies
=================

- file dependency
  - default MD5 checksum
  - custom file status calculation

- explicit task dependency

Task uptodate status
====================

- when is task uptodate (rules to determine it)
  - all following conditions must be true

    - each file from file_dep is uptodate at the moment of task evaluation
    - each file from targets is uptodate (last execution was succesful)
    - calculated uptodate is "OK"

- calculating file uptodate status
- calculating task uptodate status

    - all file_dep are uptodate

Complex dependency options
==========================
.. todo:: explain, tasks can be declared also later on during execution.

reporter: reporting progress and result
=======================================
- explain existing options
- refer to customization where custom reporter can be defined

DB-Backend
==========

.. todo:: purpose, formats, how to extend.

`doit` customization
====================
- embed into your own product
- implement custom DB-Backend
- develop plugins/libraries
- custom reporter

Tools embeded in `doit`
=======================

There are tools, which are not essential to core of `doit` processing engine, but come very often
handy. For that reason they are included in `doit`.

.. todo:: mostly the http://pydoit.org/tools.html stuff
