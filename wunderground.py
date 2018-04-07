#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Historical weather data from Weather Underground."""

from bs4 import BeautifulSoup
import json
import os
import re
import time
import urllib.request

_URL = "https://www.wunderground.com/history/airport/{}/{}/{}/{}/MonthlyHistory.html"

def download(airport, year, month, day):
    """Download monthly weather history from wunderground.com as HTML."""

    print("Downloading . . .", airport, year, month, day)
    time.sleep(1)  # be nice

    url = _URL.format(airport, year, month, day)

    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")

    return html

def parse(html, data, variable):
    """Parse HTML to find variable as [max, avg, min] in °F."""

    soup = BeautifulSoup(html, "html.parser")

    x = []
    for tr in soup.find_all("tr"):
        if re.search("<span>{}</span>".format(variable), tr.decode()):
            for td in tr.find_all("td"):
                t = td.text.strip()
                if "°F" in t:
                    x.append(int(t.split()[0]))

    try:
        data["max"].append(x[0])
        data["avg"].append(x[1])
        data["min"].append(x[2])
    except IndexError:
        print("- no data available for", variable)


def history(airport):
    """Return airport weather station data from 2010-2017."""

    filename = os.path.join("data/", airport + ".json")

    try:
        with open(filename) as fp:
            data = json.load(fp)
    except FileNotFoundError:
        data = get_data(airport, 2010, 2017)
        with open(filename, "w") as fp:
            json.dump(data, fp)

    return data

def get_data(airport, start, end):
    """Return airport weather station data from years start-end."""

    data = {"Max Temperature": {},
            "Min Temperature": {},
            "Mean Temperature": {},
            "Dew Point": {}}

    for k in data:
        for i in range(1, 13):
            m = str(i)
            data[k][m] = {"max": [], "avg": [], "min": []}

    for year in range(start, end+1):
        for i in range(1, 13):
            m = str(i)
            html = download(airport, year, i, 1)
            for k in data:
                parse(html, data[k][m], k)

    return data
