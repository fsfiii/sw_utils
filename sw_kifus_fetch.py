#!/usr/bin/env python

import os
import requests
import sys

output_dir = '.'
user = 'ohithere'

a = sys.argv
if len(a) > 1 and a[1]:
    output_dir = a[1]
    os.makedirs(output_dir, exist_ok=True)

if len(a) > 2 and a[2]:
    user = a[2]

url = 'https://www.shogi-extend.com/w.json?format_type=kento&query=%s' % user

r = requests.get(url)
kifu_urls = [g['kifu_url'] for g in r.json()['game_list']]

for kurl in kifu_urls:
    kur = requests.get(kurl)
    kif = kur.text
    path = output_dir + '/' + kurl.split('/')[-1]
    print('writing kifu: %s' % path)
    with open(path, 'w') as kif_file:
        kif_file.write(kif)
