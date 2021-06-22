# `Windows` 上配置 `beyond compare` 当作 `difftool` / `mergetool`

``` console
  git config --global diff.tool bc
  git config --global difftool.bc.path "c:/Program Files/Beyond Compare 4/bcomp.exe"

  git config --global merge.tool bc
  git config --global mergetool.bc.path "c:/Program Files/Beyond Compare 4/bcomp.exe"
```

