"""Sphinx configuration."""
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath("../src"))

project = "Carcassonne"
author = "jens persson"
__copyright__ = f"{datetime.now().year}, {author}"


extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "myst_parser",
    "sphinx_click",
]
language = "en"
linkcheck_ignore = [
    "codeofconduct.html",
]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
]
