# Base_B.Git的使用
## 学习资源
- [廖雪峰 Git 教程](https://liaoxuefeng.com/books/git/)
- [Learn Git Branching 交互式练习](https://learngitbranching.js.org/?locale=zh_CN)
## 学习目标
1. 掌握代码拉取、提交、推送完整流程
2. 理解工作区、暂存区、本地仓库、远程仓库四者关系
3. 使用分支完成简单协作开发
4. 查看修改记录、处理代码冲突
5. 规范提交代码，会编写 `.gitignore` 和 `README.md`
## 核心概念
| 区域 | 说明 |
| --- | --- |
| 工作区 | 你本地实际编辑的文件夹文件 |
| 暂存区 | 临时存放将要提交文件的缓冲区，`git add` 将文件加入暂存区 |
| 本地仓库 | `.git`文件夹，`git commit` 将暂存区内容保存到本地版本库 |
| 远程仓库 | 托管在 Github/Gitee 的云端仓库，`git push`推送至远端 |
## 高频基础命令
```
# 初始化仓库
git init
# 克隆远程仓库
git clone 仓库地址

# 工作区 -> 暂存区
git add .
# 暂存区 -> 本地仓库
git commit -m "提交说明：修复xxbug"

# 推送到远程仓库
git push origin main
# 拉取远程最新代码
git pull origin main

# 分支操作
git branch dev        # 创建分支
git checkout dev      # 切换分支
git merge dev         # 合并分支

# 查看日志
git log
# 查看修改状态
git status
```
## 配套文件编写
### 1. `.gitignore`：忽略不需要上传的文件
```
# python缓存文件
__pycache__/
*.pyc
# 系统文件
.DS_Store
# 虚拟环境文件夹
venv/
```
### 2. `README.md`：项目说明文档
包含项目简介、环境依赖、安装步骤、运行教程。