# `Windows` 上 `git` `CRLF`

0. 参考资料
1. `Unix` 上换行只有 `LF`，`Windows` 上是 `CRLF`

1. 如果一个文件现在 `Unix` 上编辑后在 `Windows` 上编辑，`git` 会报 `CRLF` 改动。反之亦然。

2. `git autocrlf` 可以自动帮助修改文件（而**不是隐藏**改动）
	```
   core.autocrlf=true:      core.autocrlf=input:     core.autocrlf=false:

        repo                     repo                     repo
      ^      V                 ^      V                 ^      V
     /        \               /        \               /        \
   crlf->lf    lf->crlf     crlf->lf    \             /          \
   /            \           /            \           /            \
	```

所以可以看到

|  `core.autocrlf`  |      |      |
| ---- | ---- | ---- |
|`true`|    x -> LF -> CRLF |  warning "LF will be replaced by CRLF" |
|`input`|   x -> LF -> LF    | warning "CRLF will be replaced by LF" |
|`false`|   x -> x -> x       |no warning |



3. 所以如果要做 `Unix` 上用，就用 `=true` 最好。
