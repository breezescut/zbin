# Environment Config
仅以此文档记录各类软件安装和配置

## Visual Studio Code
### Python VSC Config
- disable python lint

### Golang VSC Config

### C/C++ VSC Config
- [C++ 扩展](https://blogs.msdn.microsoft.com/c/?p=1072)
- Clang 工具链比 GCC 工具链优秀, VSC 有Clang 插件, 但尚未安装 Windows 上的 Clang 工具链
### Git VSC Config
- 持久化 Github 账号: git config --global credential.helper wincred

## Golang 环境配置
- 安装 64 位版本
- 环境变量未配置
- 工具链未安装(因为需要翻墙, 没搞定 Windows 翻墙)

## Python 环境配置
- 安装了 Anaconda 用于支持 Python
- 默认 Python3, 用 Anaconda 另外装了个 python27 的虚拟环境
- Ubuntu 上没有安装 Anaconda, 直接用 apt-get 安装了 python3 和 Python(默认2.x) 两种版本

### [Anaconda 教程](http://www.jianshu.com/p/2f3be7781451)
- 国内镜像配置
  * conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  * conda config --set show_channel_urls yes
  * 支持设置多个镜像
- Conda 环境管理
  * 创建新环境: conda create --name python27 python=2.7 # 纯python环境
  * 创建新环境+库: conda create --name python27 python=2.7 anaconda(包名, Anaconda 代表包集合, 换 numpy 表示只安装 numpy包)
  * 激活环境:source activate python27
  * 反激活环境: source deactivate python27
  * 查看已安装环境: conda info -e
  * 删除已有环境: conda remove --name python27 --all
- Conda 包管理
  * 安装包: conda install scipy
  * 查看已安装包: conda list (查看各种方式安装的包, 不依赖于pip)
- Conda 常用操作
  * 查看指定环境的安装包: conda list -n python27
  * 查找 package 信息: conda search numpy
  * 安装 package: conda install [ -n pytohn27 ] numpy
  * 更新 package: conda update [ -n python27 ] numpy
  * 删除 package: conda remove [ -n  python27 ] numpy
  * 更新 conda: conda update conda
  * 更新 Anaconda: conda update anaconda
  * 更新 python: conda update python
  * 安装 anaconda : conda install anaconda
