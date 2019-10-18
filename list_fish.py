#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 下午4:13
import workflow
from workflow import web
import sys

wf = workflow.Workflow3()


def get_fish_data():
    data = web.get('https://www.printf520.com:8080/GetType').json()
    return data


def main(wf):
    data = wf.cached_data('fish', get_fish_data, max_age=3600)
    for each in data["Data"]:
        wf.add_item(each['title'], arg=each['id'], autocomplete=each['id'], icon="fish.png", valid=False)

    wf.send_feedback()


if __name__ == '__main__':
    wf = workflow.Workflow3()
    sys.exit(wf.run(main))
