#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: multiDir.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-6-下午11:25
# ---------------------说明--------------------------
# 复杂的字典操作。
# ---------------------------------------------------
iij = 123
print(type(iij))
print(type(str(iij)))
people = {"name": "hanxu", "age": 10, "sex": 1}
peopleList = {}
peopleList.setdefault(people["name"], people)
for item in range(1, 10):
    # print("indexItem:", item)
    newpeople = {}
    newpeople.setdefault("name", people["name"] + "-" + str(item))
    newpeople.setdefault("age", people["age"] + item);
    newpeople.setdefault("sex", item % 2);
    peopleList.setdefault(newpeople["name"], newpeople)
print(peopleList)
print(peopleList["hanxu-2"]["age"])

# 注意使用美化print
import pprint

pprint.pprint(peopleList)
