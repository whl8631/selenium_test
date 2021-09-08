# coding=utf-8
import csv

import pytest
import yaml


def get_testData(testCase_file):
    with open(testCase_file,encoding='UTF-8-sig') as f:
        rd = csv.DictReader(f)
        data = []
        for row in rd:
            data.append(row)
    return data


@pytest.mark.parametrize("datas",get_testData("test.csv"))
def test_case1(datas):
    print("1",datas)
    # a = datas["username"]
    b = datas["password"]
    # un = a.get('login').get('username')
    # print("aaaaa:",a.get('login').get("username")[1])
    print("4:",b)
    pass