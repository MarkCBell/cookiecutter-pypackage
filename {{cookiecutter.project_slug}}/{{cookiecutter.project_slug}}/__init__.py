# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import pkg_resources  # Suppress 'UserWarning: Module curver was already imported from ...'
    __version__ = pkg_resources.require('{{ cookiecutter.project_name }}')[0].version

