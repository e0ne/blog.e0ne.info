---
title: "Click - Implement CLI Without Pain"
date: 2019-02-16T22:30:52+02:00
category: [notes]
tags: [python, cli]
archives: [2019]
author: Ivan Kolodyazhny
---

I didn’t write reviews for libraries for a while. Honestly, I don’t want to
write a review for [click](https://click.palletsprojects.com/en/7.x/) because
a reading of it will require more time than you try it.

It’s an awesome library which is really easy to use. E.g.:

```
@click.command()
@click.option('--command', prompt='command name: clone or update',
              help='Clone or update repos')
def main(command):
    if command == 'clone':
        clone()

    elif command == 'update':
        update()
```

I didn’t find anything like this for Python. I will use it and recommend
anybody who needs CLI for his service or application.
