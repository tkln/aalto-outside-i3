# -*- coding: utf-8 -*-
"""
A py3status module for displaying outside.aalto.fi weather data.
"""

import json, requests


class Py3status:
    cache_timeout = 60 * 5
    def get(self):
        resp = requests.get(url = 'http://outside.aalto.fi/data.txt')
        data = json.loads(resp.text)
        return {
            'full_text':    str(data['gent-outside-t']) + ' °C',
            'cached_until': self.py3.time_in(cahe_timeout)
        }
