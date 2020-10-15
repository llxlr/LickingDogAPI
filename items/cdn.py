#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def cf_purge(zone_id: str, email: str, global_api_key: str):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"
    headers = {
        "X-Auth-Email": f"{email}",
        "X-Auth-Key": f"{global_api_key}",
        "Content-Type": "application/json"
    }
    post_data = '{"purge_everything":true}'
    return requests.post(url, post_data, headers=headers).json()

from config import cf_zone_id, cf_email, cf_global_api_key
print(cf_purge(cf_zone_id, cf_email, cf_global_api_key))