#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import json

file = {}
current_word = None
current_count = 0
current_doc= None
word = None
count=0

for line in sys.stdin:
    line = line.strip()

    word, doc ,num = line.split('\t',1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        if doc in file:
            current_count += count
        else:
            current_count = count
    else:
        if current_word:
            file[word]= {doc:count}
        current_count = count
        current_word = word
        current_doc = doc

if current_word == word:
    file[current_word]= {current_doc:current_count}
with open('/usr/local/bin/output.json',"w",encoding="utf-8") as dat:
    json.dump(file,dat)