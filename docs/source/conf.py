# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import plyslv
from datetime import date

project = 'polysolve'
author = plyslv.__author__
copyright = f"{author}, {date.today().year}"
release = plyslv.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.apidoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.intersphinx",
]
apidoc_modules = [
    {"path": "../../plyslv",
    "destination": "api"},
]
templates_path = ['_templates']
exclude_patterns = []
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
