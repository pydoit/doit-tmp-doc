from pathlib import Path

from doitpy import docs

DOIT_CONFIG = {
    "default_tasks": ["sphinx"]
}


DOC_ROOT = Path('docs')
DOC_BUILD_PATH = DOC_ROOT / '_build' / 'html'


def task_docs():
    """Build Sphinx based documentation.
    """
    doc_files = list(DOC_ROOT.rglob('*.rst'))
    doc_files.append(Path('README.rst'))
    yield docs.spell(doc_files, 'docs/dictionary.txt')
    sphinx_opts = "-A include_analytics=1 -A include_donate=1"
    yield docs.sphinx(DOC_ROOT, DOC_BUILD_PATH, sphinx_opts=sphinx_opts,
                      task_dep=['spell'])
