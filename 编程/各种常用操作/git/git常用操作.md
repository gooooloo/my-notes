# `Git status` 文件路径中`unicode`显示错误

错误类似 ` modified: "\345\220/\234.md"`
这是因为 `git` 默认对 非`ascii` 的路径字符都 `quote`。
可以这样解决 `git config --global core.quotepath false`

# `git track` 到已有`branch`
`git branch -u origin/master`

# `oh-my-zsh`里慢
https://stackoverflow.com/questions/12765344/oh-my-zsh-slow-but-only-for-certain-git-repo
```
git config --add oh-my-zsh.hide-status 1
git config --add oh-my-zsh.hide-dirty 1
```

# `Windows` 上配置 `beyond compare` 当作 `difftool` / `mergetool`

``` console
  git config --global diff.tool bc
  git config --global difftool.bc.path "c:/Program Files/Beyond Compare 4/bcomp.exe"
   
  git config --global merge.tool bc
  git config --global mergetool.bc.path "c:/Program Files/Beyond Compare 4/bcomp.exe"
```

