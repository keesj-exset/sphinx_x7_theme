import os

VERSION = '0.2.1'


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return cur_dir


def setup(app):
    app.add_html_theme('sphinx_x7_theme', get_html_theme_path())
