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
<div class="movie">
    <div class="title">Movie Title</div>
    <div class="star">5</div>
    <div class="tags">
        <div class="tag">Comedy</div>
        <div class="tag">2019</div>
        <div class="tag">China</div>
    </div>
</div>
</body>
</html>
"""


class MyItem(Item):
    title = TextField(css_select='.title')
    star = TextField(css_select='.star')
    tags = TextField(css_select='.tag', many=True)

    async def clean_star(self, value):
        return int(value)


async def main():
    item = await MyItem.get_item(html=HTML)
    print('Title: ', item.title)
    print('Star: ', item.star)
    for tag in item.tags:
        print('Tag: ', tag)


if __name__ == '__main__':
    asyncio.run(main())
