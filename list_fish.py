#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 下午4:13
import workflow
from workflow import web
import sys
import os

wf = workflow.Workflow3()


def get_fish_data():
    from pypinyin import pinyin, Style

    os.environ['PYPINYIN_NO_PHRASES'] = 'true'
    data = web.get('https://www.tophub.fun:8080/GetType').json()
    for each in data["Data"]:
        chinese_spell_list = pinyin(each['title'], strict=False, style=Style.FIRST_LETTER)
        chinese_spell = ""
        for e in chinese_spell_list:
            chinese_spell += e[0]
        each["chinese_spell"] = chinese_spell.lower()
    return data


def main(wf):
    data = wf.cached_data('fish', get_fish_data, max_age=3600)
    # data = get_fish_data()
    for each in data["Data"]:
        if len(sys.argv) == 1:
            wf.add_item(each['title'], arg=each['id'], autocomplete=each['chinese_spell'] + " " + each['id'],
                        icon="fish.png", valid=False)
        elif each['chinese_spell'].startswith(sys.argv[1]):
            wf.add_item(each['title'], arg=each['id'], autocomplete=each['chinese_spell'] + " " + each['id'],
                        icon="fish.png", valid=False)

    wf.send_feedback()


if __name__ == '__main__':
    wf = workflow.Workflow3()
    sys.exit(wf.run(main))
