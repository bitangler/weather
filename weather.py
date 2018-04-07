#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyze historic weather using data from Weather Underground."""

import at
import numpy as np
import wunderground

_MONTH = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def history(airport):
    """Historical weather data for an airport weather station."""

    data = wunderground.history(airport)

    form = "{:^10s}{:10.1f}{:10.1f}{:10.1f}{:10.1f}{:10.1f}{:10.1f}"
    print("{:^10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}".format("Month", "T_max", "T_avg", "T_min", "D_max", "D_avg", "D_min"))

    for i in range(1, 13):
        m = str(i)

        t_max = np.mean(data["Max Temperature"][m]["avg"])
        t_avg = np.mean(data["Mean Temperature"][m]["avg"])
        t_min = np.mean(data["Min Temperature"][m]["avg"])

        d_max = np.mean(data["Dew Point"][m]["max"])
        d_avg = np.mean(data["Dew Point"][m]["avg"])
        d_min = np.mean(data["Dew Point"][m]["min"])

        print(form.format(_MONTH[i], t_max, t_avg, t_min, d_max, d_avg, d_min))

if __name__ == "__main__":
    for airport in ["KTOC"]:
        history(airport)
