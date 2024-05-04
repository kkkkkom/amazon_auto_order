# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
from datetime import datetime
import sphinx_material

project = "Aamzon Auto Order"
copyright = f"{datetime.now().year}, kkkkkom"
author = "kkkkkom"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages", 
    "sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_show_sourcelink = True
html_sidebars = {"**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]}

extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"
html_short_title = f"{project} {release}"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
]

html_theme_options = {
    "repo_url": "https://github.com/kkkkkom/amazon_auto_order",
    "repo_type": "github",
    "repo_name": "Amazon Auto Order Repo",
    "html_minify": False,
    "html_prettify": True,
    "css_minify": True,
    "logo_icon": "&#xe869",
    "color_primary": "orange",
    "color_accent": "blue",
    "theme_color": "#2196f3",
    "master_doc": False,
    "nav_links": [
        {
            "href": "https://kkkkkom.github.io/amazon_auto_order/",
            "title": "AAO",
            "internal": False,
        },
    ],
    "heroes": {
        "index": "The official AAO Documentation",
        "customization": "Configuration options to personalize your site.",
    },
    "version_dropdown": False,
    "version_json": "_static/versions.json",
    "table_classes": ["plain"],
    "navigation_with_keys": True,
    "globaltoc_maxdepth": 1,
}

html_show_sphinx = True
html_compact_lists = True

new_html_context = {
    # "Edit on github" button
    "display_github": False,
    "github_host": "",
    "github_user": "",
    "github_repo": "",
    "github_version": "master/",
    "conf_py_path": "doc/rst/",
    "source_suffix": ".rst",
    "favicon": "favicon.png",
}

if "html_context" in globals():
    html_context.update(new_html_context)
else:
    html_context = new_html_context

