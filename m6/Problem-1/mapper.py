#!/usr/bin/env python

import sys
import json

def mapper(record):
	key = record[0]
	value = record[1].strip()
	words = value.split()
	seen = {}
	for each in words:
		intermediate = {}
		if (not seen.get(each,False)):
			seen[each]	= True
			intermediate.setdefault(each, [])
			intermediate[each].append(key)
			print each, intermediate[each]

for line in sys.stdin:
			record = json.loads(line)
			mapper(record)


