#git

# `Ubuntu` 上装 `git` `server`

0. 参考资料 https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server
1. 确保`ubuntu`上有 `ssh` 运行
	1. `sudo apt install openssh-server`
	2. `sudo service ssh start`
2. 创建一个 `repo` 的专用 `Ubuntu` `user`
	
	1. `sudo adduser myuser`
3. 在该 `user` 里为允许的 `client` 机器配置 `ssh` 权限
	1. `su myuser`
	2. `mkdir ~/.ssh`
	3. `chmod 700 ~/.ssh`
	4. `touch ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys`
	5. `vim ~/.ssh/authorized_keys`，添加目标`client` 的 `ssh pub key`
4. 创建 `git` 项目
	1. `mkdir ~/xxx.git && cd ~/xxx.git`
	2. `git init --bare`
5. 这个`git`项目的地址是 `myuser@ip:/~/xxx.git`
6. 为了安全，还可以在 `~/.ssh/authorized_keys` 里限制**每一个** `client` 的行为
	```
	no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty
	公钥1
	```