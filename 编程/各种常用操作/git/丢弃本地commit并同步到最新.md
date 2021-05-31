#git

# 场景

假设我的分支状态如下

``` console
$ git status
On branch master
Your branch and 'origin/master' have diverged,
and have 2 and 2 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

nothing to commit, working tree clean
```

``` console
$ git log --graph --all

* commit a8bcbdf9bf9743209fe079ccb503b8f976bbfae8 (HEAD -> master)
| Author: abc <a@b.c>
| Date:   Mon Mar 29 14:03:44 2021 +0800
|
|     c2
|
* commit 6ea7ed283840e7d270352b8c1048b9cd5afa7ad7
| Author: abc <a@b.c>
| Date:   Mon Mar 29 13:59:39 2021 +0800
|
|     b2
|
| * commit 6d5fe7b9bc36f1348d6dc612851a6c455c35b27c (origin/master, origin/HEAD)
| | Author: abc <a@b.c>
| | Date:   Mon Mar 29 13:59:03 2021 +0800
| |
| |     c1
| |
| * commit 9938afb42db4f7bf08c425cf66f1186c5435f680
|/  Author: abc <a@b.c>
|   Date:   Mon Mar 29 13:58:49 2021 +0800
|
|       b1
|
* commit c0c5b03e9813f1bdf4e11fe83f08198bab11f40f
  Author: abc <a@b.c>
  Date:   Mon Mar 29 13:56:38 2021 +0800

      a
```

我不想要 b2, c2 了，并且想把本地的 master 分支更新到最新，即 c1



# 解法

``` console
$ git reset --hard origin/master                                                                                                                                                                                                                                                130 ↵
HEAD is now at 6d5fe7b c1
```

``` console
$ git log --graph --all

* commit 6d5fe7b9bc36f1348d6dc612851a6c455c35b27c (HEAD -> master, origin/master, origin/HEAD)
| Author: abc <a@b.c>
| Date:   Mon Mar 29 13:59:03 2021 +0800
|
|     c1
|
* commit 9938afb42db4f7bf08c425cf66f1186c5435f680
| Author: abc <a@b.c>
| Date:   Mon Mar 29 13:58:49 2021 +0800
|
|     b1
|
* commit c0c5b03e9813f1bdf4e11fe83f08198bab11f40f
  Author: abc <a@b.c>
  Date:   Mon Mar 29 13:56:38 2021 +0800

      a
```



