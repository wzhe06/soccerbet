#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" soccer bet main function file """

__author__ = 'ggstar'

import spider
import portfoliomodel
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')

m_match_ids = spider.crawl_match_list()

for m_match_id in m_match_ids:
    print m_match_id
    m_match = spider.get_match(m_match_id)

    portfolio = portfoliomodel.best_portfolio(m_match)

    m_match.display()
    portfolio.display()
    time.sleep(4)