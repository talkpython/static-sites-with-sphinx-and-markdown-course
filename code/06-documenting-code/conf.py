import os
import sys

sys.path.insert(0, os.path.abspath("."))

project = "Schlockchain"
copyright = "2021, Paul Everitt <pauleveritt@me.com>"
author = "Paul Everitt <pauleveritt@me.com>"
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv"]
html_static_path = ["_static"]
templates_path = ["_templates"]
myst_enable_extensions = [
    "colon_fence",
]
