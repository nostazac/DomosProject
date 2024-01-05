# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:35:38 2023

@author: ADMIN
"""

import http.client
import json
from urllib.parse import quote_plus

base =  '/maps/api/geocode/json'
def geocode(address):
    path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])
    
if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')