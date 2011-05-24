#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from setuptools import setup

setup(
    name = 'OlarkPlugin',
    version = '0.0.0',
    packages = ['olarkplugin'],
    package_data = {'olarkplugin': ['templates/*.html']},
    author = "Nick Piper",
    author_email = "nick.piper@logica.com",
    description = "Integration with http://www.olark.com/.",
    license = "BSD",
    keywords = "trac plugin olark",

    entry_points = {
        'trac.plugins': [
            'olarkplugin.web_ui = olarkplugin.web_ui',
            'olarkplugin.admin = olarkplugin.admin'            
        ]
    },
)
