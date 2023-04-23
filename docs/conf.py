"""Sphinx configuration."""
project = "Jaba Websockets"
author = "geoff wood"
copyright = "2023, geoff wood"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
