#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" lottery related class """

__author__ = 'ggstar'


class LotteryItem(object):

    def __init__(self):
        self.company = ""
        self.id = 0
        self.w_odds = float(0)
        self.d_odds = float(0)
        self.l_odds = float(0)
        self.cw_odds = float(0)
        self.cd_odds = float(0)
        self.cl_odds = float(0)
        self.back_ratio = 0
        self.count = 1

    def display(self):
        print "%s\t%s\t%s\t%s\t%s\t" % (self.id, self.company, self.cw_odds, self.cd_odds, self.cl_odds)


class LotteryMatch(object):

    def __init__(self, match_name, match_link,  match_time, host_team, guest_team, item_arr):
        self.match_name = match_name
        self.match_link = match_link
        self.match_time = match_time
        self.host_team = host_team
        self.guest_team = guest_team
        self.item_arr = item_arr

    def display(self):
        print "match name:\t%s\nmatch members:\t%s VS %s\nmatch time:\t%s" % \
              (self.match_name, self.host_team, self.guest_team, self.match_time)

    def display_items(self):
        for item in self.item_arr:
            item.display()


class LotteryPortfolio(object):

    def __init__(self):
        self.fund_count = 0

        self.profit = 0

        self.win_item = LotteryItem()
        self.draw_item = LotteryItem()
        self.lose_item = LotteryItem()

        self.win_percentage = 0
        self.draw_percentage = 0
        self.lose_percentage = 0

    def display(self):
        print "profit:\t%s\nwin:\t%s %s\t%s\t%s\ndraw:\t%s %s\t%s\t%s\nlose:\t%s %s\t%s\t%s" % \
              (self.profit,
               self.win_item.id, self.win_item.company, self.win_item.cw_odds, self.win_percentage,
               self.draw_item.id, self.draw_item.company, self.draw_item.cd_odds, self.draw_percentage,
               self.lose_item.id, self.lose_item.company, self.lose_item.cl_odds, self.lose_percentage)