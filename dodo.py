import glob

from doitpy import docs


DOC_ROOT = 'docs/'
DOC_BUILD_PATH = DOC_ROOT + '_build/html/'


def task_docs():
    """Build Sphinx based documentation.
    """
    doc_files = glob.glob('docs/*.rst') + ['README.rst']
    yield docs.spell(doc_files, 'docs/dictionary.txt')
    sphinx_opts = "-A include_analytics=1 -A include_donate=1"
    yield docs.sphinx(DOC_ROOT, DOC_BUILD_PATH, sphinx_opts=sphinx_opts,
                      task_dep=['spell'])
