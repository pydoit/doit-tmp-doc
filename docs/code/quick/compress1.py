def task_compress():
    """Compress input file(s)"""
    return {
        "actions": [
             "7z a %(targets)s %(dependencies)s",
        ],
        "file_dep": ["huge.dat"],
        "targets": ["huge.compressed.7z"],
        "clean": True
    }
