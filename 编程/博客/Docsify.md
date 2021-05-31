#git
# Docsify 是什么

- 通过 index.html 使得文件夹可以被访问
- 通过 js 使得 markdown 可以被访问

# Docsify 是怎样使得 markdown 可以被访问的？

TODO

# Docsify 是需要搭建服务器吗？

本质是不需要。任何监听端口而且重定向到 index.html 的服务器程序都可以。比如 `python3 -m http.server 8000` 。

不过 Docsify 似乎继承了 Node 环境，可以额外赠送一些服务器程序的功能。

# 插件

因为 Docsify 本身只是 html+js。所以它本身没有太多功能。但既然是 js，那么就可以通过 include 其他 js 来增加功能。最后就变成了 插件了。

# 界面布局

既然是 html+js，那必然是可以定制的

# 怎样和 github 集成？

GitHub Pages 有网站功能，同样是 html+js。所以Docsify 生成html并引入对应的js，GitHub Pages 就可以展示了。server其实是host在 github 上的。

# 怎样和 OneDrive 集成？

由于只是 html + js，所以当作一些文件系统看就是了。

# OneDrive 怎样和 GitHub 集成？

TODO。其实这个不是 Docsify 的话题。不过……看了一圈，没有好的方案。

可能最靠谱的方案是写个脚本定期 git push 了。

# 导航

docsify 的 目录导航似乎不好用，我自己写了个脚本去更新目录结构了。

