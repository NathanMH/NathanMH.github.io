#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nathan Mador-House'
SITENAME = "Nathan's Projects"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pronto Musica', 'https://www.prontomusica.org/'),
         ('Lara Deutsch', 'https://www.laradeutsch.ca/'))

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/NathanMH'),
          ('github', 'https://github.com/NathanMH'))

DEFAULT_PAGINATION = False

STATIC_PATHS = ['assets']
THEME = ("theme/blue-penguin")

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
