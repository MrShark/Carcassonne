"""Sphinx configuration."""  # noqa: INP001

import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path("../src").resolve()))

project = "Carcassonne"
author = "jens persson"
__copyright__ = f"2023-{datetime.now().year}, {author}"  # noqa: DTZ005


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
