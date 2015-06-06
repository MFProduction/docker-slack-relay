#!/usr/bin/env python

import os
import json
import envoy

channels = {}

for item in os.environ["HUB_REPOS"].split(","):
    repo,channel = item.split(":")
    channels[repo] = channel
with open("/opt/qnib/slack-relay/channel_selector.json", "w") as fd:
    fd.write(json.dumps(channels))

proc = envoy.run("python /opt/qnib/slack-relay/relay.py")
