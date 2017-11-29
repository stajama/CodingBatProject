#!/usr/bin/env python3

import pprint
import requests
import lxml
from bs4 import BeautifulSoup as datSoup
import scraperBuild

r = requests.session()
data = {"uname": "stajama@gmail.com",
        "pw": "efsdf9684Def_esdfed"}
result = r.get("http://codingbat.com/java")
# tree = lxml.html.fromstring(result.text)
head = {"referer": "http://codingbat.com/java"}
result2 = r.post("http://codingbat.com/java", data=data, headers=head)

soupMix = datSoup(result2.text,"lxml")
# print(soupMix.prettify())
x = soupMix.find_all('a')
# for i in x:
#     print(i)
#     print(type(i))

sections = {}
for line in x:
    if "/java/" in str(line):
        collect = str(line)
        collect = collect[collect.find("/java/") + 6 : collect.find("\">")]
        sections.setdefault(collect, {})


for i in sections:
    # print(i)
    result = r.get("http://codingbat.com/java/{}".format(i))
    info = datSoup(result.text, "lxml")
    for j in info.find_all("a"):
        collect = str(j)
        if "prob" in collect and "MakeBricks" not in collect:
            # print(j)
            start = collect.find(">")
            problemName = collect[start + 1 : collect.find("<", start)]
            link = "http://codingbat.com/prob/{1}".format(i, collect[collect.find("/prob/") + 6: collect.find('"', collect.find("prob"))])
            sections[i].setdefault(problemName, {})
            sections[i][problemName]["link"] = link

# pprint.pprint(sections)

# print("-" * 79)
# print(sections["String-1"]["atFirst"]["link"])
# testing = sections["String-1"]["withoutEnd"]["description"]
# result = r.get(testing)
# soupMix = datSoup(result.text, "lxml")
# # print(soupMix.prettify())
# for i in soupMix.find_all("p"):
#     if "max2" in str(i):

for section in sections:
    for problem in sections[section]:
        testing = sections[section][problem]["link"]
        result = r.get(testing)
        soupMix = datSoup(result.text, "lxml")
        for i in soupMix.find_all('p'):
            if "max2" in str(i):
                string = str(i)
                start = string.find('"max2">')
                sections[section][problem]["description"] = string[start + 7 : string.find("<", start)]
                # should grab code here too
                # should grab examples here too ('tests')
                break


for part in sections:
    print(part + '\n\n')
    for problem in sections[part]:
        if not "makeBricks" in problem or not "MakeBricks" in problem:
            print(problem)
            print(sections[part][problem]["description"] + '\n')
# pprint.pprint(sections)

scraperBuild.mainDeal(sections)