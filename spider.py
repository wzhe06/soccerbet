#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" lottery item class """

__author__ = 'ggstar'

import re
import lottery
import datetime
import requests


def url_get(url_str, decode):
    r = requests.get(url_str)
    return r.content.decode(decode, "ignore").encode('utf-8')


def crawl_match_info(match_id):
    url_str = "http://odds.500.com/fenxi/ouzhi-" + str(match_id) + ".shtml"
    print url_str
    content = url_get(url_str, "gb2312")
    #print content

    match = lottery.LotteryMatch("match_name", "match_link",  "match_time", "host_team", "guest_team", "item_arr")

    match_info_r = re.compile(r'<a class="hd_name"[\s\S]*?>([\s\S]*?)<')

    seq = 0
    for m in match_info_r.finditer(content):
        seq += 1
        if seq == 1:
            match.host_team = m.group(1)
        elif seq == 2:
            match.match_name = m.group(1)
        elif seq == 3:
            match.guest_team = m.group(1)

    match_time_r = re.compile(r'<p class="game_time">([\s\S]*?)</p>')

    for m in match_time_r.finditer(content):
        match.match_time = m.group(1)

    return match


def crawl_lottery_items(match_id):

    url_str = "http://odds.500.com/fenxi1/ouzhi.php?id=" + str(match_id) + "&ctype=1&start="+str(1)+"&r=1&style=0&last=1&guojia=0&chupan=0"
    content = url_get(url_str, "utf-8")

    item_r = re.compile(r'(xls="row"[\s\S]*?)<tr class="tr\d"')

    lottery_items = []

    item_seq = 0

    for m in item_r.finditer(content):

        item_seq += 1
        lottery_item = lottery.LotteryItem()
        lottery_item.id = item_seq

        one_item = m.group(1)
        company_pattern = re.compile(r'class="tb_plgs" title="(.*?)"')
        company_match = company_pattern.search(one_item)

        if company_match:
            lottery_item.company = company_match.group(1)

        odds_pattern = re.compile(r'style="cursor:pointer" >(.*?)</td>')

        seq = 0
        for odd in odds_pattern.finditer(one_item):
            seq += 1
            odd_f = float(odd.group(1))
            if seq == 1:
                lottery_item.w_odds = odd_f
            elif seq == 2:
                lottery_item.d_odds = odd_f
            elif seq == 3:
                lottery_item.l_odds = odd_f
            elif seq == 4:
                lottery_item.cw_odds = odd_f
            elif seq == 5:
                lottery_item.cd_odds = odd_f
            elif seq == 6:
                lottery_item.cl_odds = odd_f

        lottery_items.append(lottery_item)

        return_pattern = re.compile(r'</tr>\s*<tr>\s*<td row="1">(.*?)%</td>')

        return_rate_match = return_pattern.search(one_item)

        if return_rate_match:
            lottery_item.back_ratio = float(return_rate_match.group(1))

    return lottery_items


def get_match(match_id):
    match = crawl_match_info(match_id)
    match.item_arr = crawl_lottery_items(match_id)

    return match


def crawl_match_list():

    today = datetime.datetime.now()
    return crawl_match_list_by_date(str(today.year) + "-" + str(today.month) + "-" + str(today.day))


def crawl_match_list_by_date(date):

    url_str = "http://trade.500.com/jczq/dgp.php?date="+ date +"&playtype=both"
    content = url_get(url_str, "gb2312")
    match_id_r = re.compile(r'http://odds.500.com/fenxi/ouzhi-(\d+).shtml')

    match_ids = []

    for m in match_id_r.finditer(content):
        match_ids.append(m.group(1))

    return match_ids
