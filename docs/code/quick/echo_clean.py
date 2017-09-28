def task_echo_to_cave():
    """Call holla to PARAMETRIZED target file"""
    return {
        "actions": [
             "echo parametrized pssst > %(targets)s",
             "echo parametrized holla >> %(targets)s",
             "echo parametrized olla >> %(targets)s",
             "echo parametrized lla >> %(targets)s",
             "echo parametrized la >> %(targets)s",
             "echo parametrized a >> %(targets)s",
        ],
        "targets": ["cave.txt"],
        "clean": True
    }
