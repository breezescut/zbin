#!/usr/bin/env python

# 1. 目录读写
'''
- 目录扫描，列出所有的文件
- 文件属性读取（文件类型创建时间、修改时间、文件大小、文件读写权限等）
- 改变文件属性
- 创建文件、删除文件，文件改名
- 处理目录信息
'''

import os
import sys


class dirOp():
    @staticmethod
    def dir_list(sdir):
        for i in os.listdir(sdir):
            print(os.path.abspath(i), end='\t')
        
    

if __name__ == '__main__':
    dirOp.dir_list(sys.argv[1])
        
# 2. 文件读写

# 3. 网络TCP/IP Socket

# 4. Http 请求

# 5. HTML 处理

# 6. XML 处理

# 7. Json 读写

# 8. 字符串处理

# 9. 操作系统控制