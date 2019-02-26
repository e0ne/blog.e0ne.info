---
title: "Cast JavaScipt object to TypeScript classes"
date: 2019-02-26T23:54:14+02:00
category: [web development]
tags: [typescript, javascript]
archives: [2019]
author: Ivan Kolodyazhny
---

TypeScript could give you a false hope that I’ve got a strong-typed code and
everything will work as expected with JavaScript. In reality, TypeScript
doesn’t do anything after sources are compiled to JavaScript. It means, in
runtime, you’ll face good-known JavaScript with it dynamic typing.

The lack of any runtime type checking is a big minus for TypeScript. You’ll
lose all your type at the same moment when browser executes code.

I’d got a pretty simple code in my Vue component:

```
data() {
        return {
            clouds: Array<Cloud>(),
        };
    }
```

And I use Axios to work with AJAX. I know that it’s a good time to use
[Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) but
it’s a different story. My code looks like:

```
axios.get('/api/clouds/')
            .then((response) => {
                this.clouds = response.data;
            });
```

And here is Cloud class definition:

```
export class Cloud {
    public created_at: Date;
    public description: string;
    public name: string;
    public nodes: object;
    public updated_at?: Date;
    public id: string;
  }
}

```

I skipped some code to make it cleaner and fit it in the blog.

If you are experienced with TypeScript, probably you understand already what
goes wrong. When I do `this.clouds = response.data;`, a browser will execute
compiled to JavaScript code which doesn’t know anything about `Cloud` type. It
means, that instead of an array of `Cloud`, I’ll get an array of simple
JavaScript objects with primitive types. It works good enough until I use some
specific Date methods and properties of my `Cloud.created_at` or
`Cloud.updated_at` properties. Since TypeScript doesn’t do any type casting
itself, `cloud.created_at` will be a string, not a Date object.

To fix it, I need manually convert JavaScript object to my TypeScript class.
I added a static method to `Cloud` type to covert JavaScript to TypeScript
objects:

```
static fromObject(obj: CloudObject): Cloud {
      let cloud = Object.create(Cloud.prototype);
      return Object.assign(cloud, json, {
        created_at: new Date(json.created_at),
      });
  }
```

All ‘magic’ is done by [Object.assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) function.

I introduced CloudObject interface just to verify types during the compile
time and have my linter happy:

```
export interface CloudObject {
    created_at: Date;
    description: string;
    name: string;
    nodes: object;
    updated_at?: Date;
    id: string;
}

```
