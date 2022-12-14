# Configuration file for the Sphinx documentation builder.

# -- Project information

from datetime import date


project = 'JetDeploy'
copyright = '{}, JetDeploy'.format(date.today().year)
author = 'JetDeploy'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

myst_heading_anchors = 3
#myst_enable_extensions = 'html_image'