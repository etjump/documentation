# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import date

project = 'ETJump'
copyright = f'{date.today().year}, ETJump Team'
author = 'ETJump Team'
release = '3.3.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
extensions = ['myst_parser', 'sphinx_copybutton', 'sphinx.ext.todo']
myst_enable_extensions = ['attrs_inline']
myst_links_external_new_tab = True
myst_heading_anchors = 3
todo_include_todos = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_logo = "img/etjump-logo.svg"
html_theme_options = {
    "sidebar_hide_name": True,
    # Respect users choices for browser fonts, dark theme inherits these too
    "light_css_variables": {
        "font-stack": "sans-serif",
        "font-stack--monospace": "monospace",
        "font-stack--headings": "serif",
    },
}
