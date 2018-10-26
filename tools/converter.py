from datetime import datetime
import html
import glob
import os.path

import tomd
from markdownify import markdownify as mad
import untangle


data_dir = '/Users/e0ne/working/blog/blog.e0ne.info/App_Data/'


TEMPLATE = """---
title: "{title}"
date: {date}+03:00
draft: {draft}
category: [{category}]
tags: [{tags}]
archives: [{year}]
aliases:
    - post/{slug}.aspx
---

{content}
"""


def load_categories(path):
    f_path = os.path.join(path, 'categories.xml')

    categories = {}
    document = untangle.parse(f_path)
    for category in document.categories.category:
        categories[category['id']] = category.cdata

    return categories


def _parse_tags(tags_node):
    tags = []
    if not hasattr(tags_node, 'tag'):
        return ''
    for t in tags_node.tag:
        tags.append(t.cdata)

    return ','.join(tags)


def _parse_categories(path, categories_node):
    all_categories = load_categories(path)
    categories = []
    if not hasattr(categories_node, 'category'):
        return ''
    for c in categories_node.category:
        categories.append(c.cdata)

    return ','.join(all_categories[cat] for cat in categories)


def convert(path):
    print('Converting...')

    file_pattern = os.path.join(path, 'posts/*.xml')
    for f in glob.glob(file_pattern):
        data = {'title': '',
                'date': '',
                'draft': '',
                'category': '',
                'tags': '',
                'slug': '',
                'conten t': ''}
        # print(f)
        # import pdb;pdb.set_trace()
        document = untangle.parse(f)

        dts = document.post.pubDate.cdata

        data['title'] = document.post.title.cdata.replace('"', '')
        data['date'] = dts.replace(' ', 'T')
        data['draft'] = document.post.ispublished.cdata == 'False'
        data['category'] = _parse_categories(path, document.post.categories)
        data['tags'] = _parse_tags(document.post.tags)
        data['slug'] = document.post.slug.cdata
        data['content'] = tomd.Tomd(html.unescape(document.post.content.cdata)).markdown

        dt = datetime.strptime(dts, "%Y-%m-%d %H:%M:%S")
        data['year'] = dt.year
        # data['content'] = mad(html.unescape(document.post.content.cdata))
        with open('content/post/{}.md'.format(data['slug']), 'w+') as md:
            md.writelines(TEMPLATE.format(**data))


if __name__ == '__main__':
    convert(data_dir)
