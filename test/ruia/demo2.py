import asyncio
from ruia import Item, TextField

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div class="container">
    <div class="movie"><a class="title">Movie 1</a><span class="star">3</span></div>
    <div class="movie"><a class="title">Movie 2</a><span class="star">5</span></div>
    <div class="movie"><a class="title">Movie 3</a><span class="star">2</span></div>
    <div class="movie"><a class="title">Movie 4</a><span class="star">1</span></div>
    <div class="movie"><a class="title">Movie 5</a><span class="star">5</span></div>
</div>
</body>
</html>
"""


class MyItem(Item):
    target_item = TextField(css_select='.movie')
    title = TextField(css_select='.title')
    star = TextField(css_select='.star')

    async def clean_star(self, value):
        return int(value)


async def main():
    async for item in MyItem.get_items(html=HTML):
        print(f'Title={item.title}, Star={item.star}')


if __name__ == '__main__':
    asyncio.run(main())
