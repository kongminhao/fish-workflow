#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 下午4:25
import workflow
import sys
from workflow import web

query = sys.argv[1]


def get_hot_data():
    url = "https://www.printf520.com:8080/GetTypeInfo?id={}".format(query)
    data = web.get(url).json()
    return data


def main(wf):
    data = wf.cached_data('hotdata-{}'.format(query), get_hot_data, max_age=30)
    for each in data["Data"]:
        wf.add_item(each['title'], arg=each['url'], icon="fish.png", valid=True)
    wf.send_feedback()


if __name__ == '__main__':
    wf = workflow.Workflow3()
    sys.exit(wf.run(main))
