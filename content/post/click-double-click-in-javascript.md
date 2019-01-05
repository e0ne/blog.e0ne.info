---
title: "Click and Double Click in JavaScript"
date: 2019-01-05T21:37:53+02:00
category: [javascript, web development]
tags: [javascript, js]
archives: [2019]
author: Ivan Kolodyazhny
---

Spent a few hours on a simple task: create different handlers for ‘click’ and ‘double click’ events on the same element, onclick handler should not be executed if a double click event is raised.

I hope, there is a better solution but I didn’t find it. I leave it here in case if somebody helps me with it:
```javascript
<html>
<body>
    <a href="#" id="clickMe">Click Me</a>

    <script type="text/javascript">
        /* click or double click */
        var timeout = null;
        let link = document.getElementById('clickMe')
        link.addEventListener('click', (e) => {
            if (timeout === null){
                timeout = setTimeout(() => {
                    timeout = null
                    alert('click')
                    e.preventDefault();
                }, 300);
            }
        })

        link.addEventListener('dblclick', (e) => {
            clearTimeout(timeout)
            timeout = null;
            alert('double click')
            e.preventDefault();
        })
    </script>
</body>
</html>
```

I use pure JavaScript to not depend on any framework in this example.

