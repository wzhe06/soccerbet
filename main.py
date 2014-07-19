#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" soccer bet main function file """

__author__ = 'ggstar'

import sys
import spider
import portfoliomodel
import time


def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

m_match_ids = spider.crawl_match_list()

for m_match_id in m_match_ids:
    m_match = spider.get_match(m_match_id)

    portfolio = portfoliomodel.best_portfolio(m_match)

    m_match.display()
    portfolio.display()
    time.sleep(4)