#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

DEVELOP = False

SITEURL = 'https://mark.feltner.me'
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

ANALYTICS = {
    'GOOGLE': 'UA-45806952-1'
}


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
