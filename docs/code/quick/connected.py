def task_python_help():
    """Write python help string to a file"""
    return {
        "actions": [
            "python -h > %(targets)s",
        ],
        "targets": ["python.help"],
        "clean": True
    }


def task_doit_help():
    """Write doit help string to a file"""
    return {
        "actions": [
            "doit help > %(targets)s",
        ],
        "targets": ["doit.help"],
        "clean": True
    }


def task_compress():
    """Compress input file(s)"""
    return {
        "actions": [
             "7z a %(targets)s %(dependencies)s",
        ],
        "file_dep": ["huge.dat", "python.help", "doit.help"],
        "targets": ["result.7z"],
        "clean": True
    }
