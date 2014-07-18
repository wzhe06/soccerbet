#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" determine lottery portfolio model """

__author__ = 'ggstar'

import lottery


def get_best_profit(portfolio):

    def min_pay(w, d, l, wp, dp, lp):
        if w * wp <= d * dp and w * wp <= l * lp:
            return w * wp
        if d * dp <= w * wp and d * dp <= l * lp:
            return d * dp
        else:
            return l * lp

    for i in range(100):
        for j in range(100-i):

            profit = min_pay(portfolio.win_item.cw_odds,
                             portfolio.draw_item.cd_odds,
                             portfolio.lose_item.cl_odds,
                             i, j, 100 - i -j)

            if profit > portfolio.profit:
                portfolio.profit = profit
                portfolio.win_percentage = i
                portfolio.draw_percentage = j
                portfolio.lose_percentage = 100 - i - j

    return portfolio


def best_portfolio(match):

    portfolio = lottery.LotteryPortfolio()

    for item in match.item_arr:

        if portfolio.win_item.cw_odds < item.cw_odds:
            portfolio.win_item = item

        if portfolio.draw_item.cd_odds < item.cd_odds:
            portfolio.draw_item = item

        if portfolio.lose_item.cl_odds < item.cl_odds:
            portfolio.lose_item = item

    portfolio = get_best_profit(portfolio)

    return portfolio