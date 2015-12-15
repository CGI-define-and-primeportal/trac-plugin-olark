#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from setuptools import setup

setup(
    name = 'OlarkPlugin',
    version = '0.0.0',
    packages = ['olarkplugin'],
    package_data = {'olarkplugin': ['templates/*.html']},
    author = "Nick Piper",
    author_email = "nick.piper@cgi.com",
    maintainer="CGI CoreTeam",
    maintainer_email="coreteam.service.desk.se@cgi.com",
    contact="CGI CoreTeam",
    contact_email="coreteam.service.desk.se@cgi.com",
    classifiers=['License :: OSI Approved :: BSD License'],
    license='BSD',
    url='http://define.primeportal.com/',
    description = "Integration with http://www.olark.com/. Not created by nor endorsed by Olark.",
    keywords = "trac plugin olark",

    entry_points = {
        'trac.plugins': [
            'olarkplugin.web_ui = olarkplugin.web_ui',
            'olarkplugin.admin = olarkplugin.admin'            
        ]
    },
)
