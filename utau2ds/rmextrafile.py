import os
import fnmatch

# 获取当前工作目录的文件列表
files = os.listdir('.')

# 对于每一个文件，检查是否是.wav文件
for filename in files:
    if not fnmatch.fnmatch(filename, '*.wav'):
        # 如果不是.wav文件，则删除
        os.remove(filename)
        print(f'Deleted: {filename}')

print('Deletion complete.')
