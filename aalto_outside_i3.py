# -*- coding: utf-8 -*-
"""
A py3status module for displaying outside.aalto.fi weather data.
"""

import json, requests


class Py3status:

    cache_timeout = 300
    format = '{temp:.2f} °C'

    def get_weather(self):
        resp = requests.get(url = 'http://outside.aalto.fi/data.txt')
        data = json.loads(resp.text)

        temp = float(data['gent-outside-t'])
        moist = float(data['gent-outside-h'])
        pres = float(data['gent-outside-b'])
        lum = float(data['gent-outside-l'])

        return {
            'cached_until':  self.py3.time_in(self.cache_timeout),
            'full_text':     self.format.format(temp = temp, moist = moist,
                                                pres = pres, lum = lum)
        }
