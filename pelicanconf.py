#!/usr/bin/env python
"""Pelican Config File"""
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'Kyle Pericak'
SITENAME = 'kyle.pericak.com'
SITEURL = ''
PATH = 'content'
OUTPUT_PATH = 'appengine/blog'
TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# RELATIVE_URLS = True
LINKS = (('How this site was made', 'pelican-guide'),
         ('Check out Breqwatr!', 'https://breqwatr.com'))
SOCIAL = (('LinkedIn', 'https://ca.linkedin.com/in/kpericak'),
          ('Twitter', 'https://twitter.com/kylepericak'))
DEFAULT_PAGINATION = 10
PANDOC_ARGS = (['--toc', '--template=pandoc-template-toc'])
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {'title': 'Table of contents:'},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {}},
    'output_format': 'html5'}
