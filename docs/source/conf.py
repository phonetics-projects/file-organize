# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'fileorganize'
copyright = '2025, Regents of the University of California'
author = 'Ronald Sprouse'
release = 'Beta'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode', 
              'sphinx.ext.napoleon',
              'sphinx_rtd_theme']

autodoc_typehints = 'description'

templates_path = ['_templates']
exclude_patterns = ['.ipynb_checkpoints']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
