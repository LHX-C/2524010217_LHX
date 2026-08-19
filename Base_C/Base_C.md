# Base_C.Linux的使用
## 学习目标
1. 配置 Linux 环境（WSL / 虚拟机 / 双系统任选其一）
2. 熟练基础 Shell 终端指令，完成文件查找、文本处理
3. 了解 Linux 分区、磁盘查看命令
4. 文件压缩打包
5. 权限管理、用户管理
6. 进程与资源查看
7. 远程连接、远程文件传输；VSCode / JetBrains IDE 远程开发
8. 环境变量配置、软件环境管理
## 常用 Shell 基础命令
### 文件目录操作
pwd                 # 查看当前路径
ls                  # 列出目录文件
cd 文件夹名          # 切换目录
mkdir test          # 创建文件夹
rm 文件名           # 删除文件
cp 源文件 目标路径   # 复制文件
mv 源文件 目标路径   # 移动/重命名文件
find ./ -name "*.py"# 文件查找
cat test.txt        # 查看文本
grep "关键词" test.txt #文本搜索
### 磁盘与分区查看
df -h    # 查看磁盘分区占用
du -sh * # 当前目录各文件大小
### 压缩打包
tar -zcvf file.tar.gz 文件夹名   # 压缩
tar -zxvf file.tar.gz           # 解压
### 权限与用户
chmod 755 test.sh    # 修改文件权限
sudo useradd testuser# 添加用户
#### 进程资源查看
top          # 实时查看进程资源
ps -aux      # 列出所有进程
kill -9 PID  # 强制结束进程
#### 远程连接 & 文件传输
ssh 用户名@服务器ip        # ssh远程登录
scp 本地文件 用户名@ip:路径 # 上传文件至服务器
### 远程开发配置要点
1. WSL：Windows 开启子系统，VSCode 安装 Remote‑WSL 插件直接开发
2. 云服务器：VSCode Remote‑SSH / Pycharm 远程解释器连接服务器编写代码