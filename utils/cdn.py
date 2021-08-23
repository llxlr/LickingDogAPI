#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import asyncio
import aiohttp


def cf_purge(zone_id, email, global_api_key):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"
    headers = {
        "X-Auth-Email": f"{email}",
        "X-Auth-Key": f"{global_api_key}",
        "Content-Type": "application/json"
    }
    data = '{"purge_everything":true}'
    return requests.post(url, data=data, headers=headers).json()


async def cf_purge_async(zone_id, email, global_api_key):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"
        headers = {
            "X-Auth-Email": f"{email}",
            "X-Auth-Key": f"{global_api_key}",
            "Content-Type": "application/json"
        }
        data = '{"purge_everything":true}'
        async with session.get(url, data=data, headers=headers, timeout=30) as response:
            assert response.status == 200
            html = await response.read()
            return html

asyncio.get_event_loop()
