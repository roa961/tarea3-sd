#!/usr/bin/env python
"""mapper.py"""

import sys
import re
doct = {}
arr = []
for line in sys.stdin:
    #words = line.lower()
    #words = line.strip()
    #for char in [",", ".", '"', "'", "(", ")", "\\", ";", ":", "$1", "$", "&"]:
     #   words = words.replace(char, '')
    line = re.sub(r'\W+','',line.strip())
    try:
        file, words = line.split('<splittername>')
    except:
        continue
    words = words.split()
    for word in words:
        arr.append('{}\t{}\t{}'.format(word,file,1))
    for item in arr:
        print(item)
