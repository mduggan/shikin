# -*- coding: utf-8 -*-

import re

_YEAR_REGEX_STR = u'(昭和|平成)(\d+)'
YEAR_RE = re.compile(_YEAR_REGEX_STR)
NENBUN_RE = re.compile(_YEAR_REGEX_STR + u'年分')
NEN_RE = re.compile(_YEAR_REGEX_STR + u'年')
# Note both full-width and half-width spaces in this re. orz.
DATE_RE = re.compile(_YEAR_REGEX_STR + u'年([ 　\d]\d)月([ 　\d]\d)日(公表|発表|付け官報)')


def get_nenbun(text, weak=False):
    year = NENBUN_RE.search(text)
    if weak and year is None:
        year = NEN_RE.search(text)
    if year is not None:
        year = year.groups()[0] + year.groups()[1]

    return year


def year_to_western(emp, year):
    if not isinstance(year, int):
        year = int(year)
    # Heisei starts in 1988
    if emp == u'平成':
        year = 1988 + year
    elif emp == u'昭和':
        year = 1925 + year
    else:
        raise ValueError('Unhandled emperor: %s' % emp)
    return year
