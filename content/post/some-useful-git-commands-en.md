---
title: "Some Useful Git Commands"
date: 2019-01-11T23:04:16+02:00
category: [development]
tags: [git, cli]
archives: [2019]
author: Ivan Kolodyazhny

---
Since I started blogging in English, I think I can translate some useful posts even they were written a few years ago. It’s a translation of the same post in [Russian](https://blog.e0ne.info/post/git-some-useful-commands/)

I’m tired to blog the same so I created this blog post to have everything in one place.


### Set username/email for git:
`$ git config --global user.email "e0ne@e0ne.info"
$ git config --global user.name "e0ne"`
You can omit to set it `global` and it will be set only for the current repository.

### Set upstream branch
`$ git branch --set-upstream master upstream/master`

### Chage the last commit
`$ git commit --amend -a`

### Change the author of several commits
<br />$ git filter-branch --commit-filter '<br />        if [ "$GIT_COMMITTER_NAME" = "<Old Name>" ];<br />        then<br />                GIT_COMMITTER_NAME="<New Name>";<br />                GIT_AUTHOR_NAME="<New Name>";<br />                GIT_COMMITTER_EMAIL="<New Email>";<br />                GIT_AUTHOR_EMAIL="<New Email>";<br />                git commit-tree "$@";<br />        else<br />                git commit-tree "$@";<br />        fi' HEAD<br />$ git push


### Mark merge conflics as resolved
`$ git add file`

### Rollback local commits
reset --soft HEAD^

### Move tag to another commit
I hope you will NOT do it but if you need, you can do it in a following way:
`$ git tag -d ver_0.1
$ git push origin :refs/tags/ver_0.1`

### The best git manual
[http://git-scm.com/book](http://git-scm.com/book)

### My .gitconfig
It’s a bit outdated, I have to update it: [https://github.com/e0ne/dot-files/blob/master/.gitconfig](https://github.com/e0ne/dot-files/blob/master/.gitconfig)

### My global .gitignore
[https://github.com/e0ne/dot-files/blob/master/.gitignore](https://github.com/e0ne/dot-files/blob/master/.gitignore)

### Create brach from tag
`$ git checkout -b branchname tag`

### Pull remote changes and revert all local changes
`$ git fetch --all
$ git reset --hard origin/master`

### Clean working directory: remove all untracked files ad directories
`$ git clean -f -d`
