#!/usr/bin/python

import json
import sys

tweets = []
for filename in sys.argv[1:]:
    with open(filename, 'r') as jsfile:
        jsfile.readline() # skip preamble
        tweets.extend(json.load(jsfile))

json.dump(tweets, sys.stdout, indent=2)

