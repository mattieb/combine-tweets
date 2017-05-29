#!/usr/bin/python

import json
import sys

tweets = json.load(sys.stdin)
tweets.sort(key=lambda tweet: -tweet['id'])
json.dump(tweets, sys.stdout, indent=2)

