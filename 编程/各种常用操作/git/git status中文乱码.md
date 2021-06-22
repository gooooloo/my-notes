# 主题

git status 里显示中文文件名总是乱码。

错误类似 ` modified: "\345\220/\234.md"`



# 解决

这是因为 `git` 默认对 非`ascii` 的路径字符都 `quote`。

`git config --global core.quotepath false`

