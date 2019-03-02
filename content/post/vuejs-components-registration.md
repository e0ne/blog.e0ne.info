---
title: "Vue.js Components Registration"
date: 2019-03-02T23:43:06+02:00
category: [web development]
tags: [vuejs]
archives: [2019]
author: Ivan Kolodyazhny
---

I can’t add anything from the technical point of view to the
[official documentation](https://vuejs.org/v2/guide/components-registration.html)
but I would like to drop a few lines about local vs global components
registration.

### Global registration

I prefer to use it mostly for the 3rd-party libraries which are used a lot.
E.g. vue-fontawesome, bootstrap-vue, etc. It’s reasonable to use global
registration for own components if they are used on the most pages.

### Local registration

I think it’s reasonable to use it as a default solution for component
registration. It allows you to do it on demand, so you always will know what
does some custom tag do.

Since I use TypeScript, I prefer the most obvious component registration. E.g.:

```
import ComponentA from @components/ComponentA.vue
new Vue({
  el: '#app',
  components: {
    'component-a': ComponentA,
  }
})
```

In general, I prefer to drop as many code, as possible but on this particular
situation I think that “Explicit is better than implicit.”. This code shows you
everything needed to use a component and understand where is its code:


* `import ComponentA from @components/ComponentA.vue` -- don’t need to search
  a code, just open `components/ComponentA.vue` file
* `component-a` -- it’s a name of the custom tag
* ComponentA -- here is a class name of your component.


Few additional lines of code are a reasonable payment for code clarity.
