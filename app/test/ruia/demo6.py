import asyncio
from ruia import Request


async def request_example():
    url = 'http://httpbin.org/get'
    params = {
        'name': 'ruia',
    }
    headers = {
        'User-Agent': 'Python3.6',
    }
    request = Request(url=url, method='GET', params=params, headers=headers)
    response = await request.fetch()
    json_result = await response.json()
    assert json_result['args']['name'] == 'ruia'
    assert json_result['headers']['User-Agent'] == 'Python3.6'
    print(json_result)


if __name__ == '__main__':
    asyncio.run(request_example())
