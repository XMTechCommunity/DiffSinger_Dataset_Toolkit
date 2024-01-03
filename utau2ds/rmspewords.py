import os

# 获取当前目录下的所有文件和文件夹
for filename in os.listdir('.'):
    # 检查文件名是否包含连字符
    if ('-' in filename)or ('B' in filename)or ('L' in filename)or ('R' in filename)or ('@' in filename)or('↑' in filename)or('↓' in filename):
        # 拼接完整的文件路径
        file_path = os.path.join('.', filename)
        # 删除文件
        os.remove(file_path)
        print(f"Deleted: {file_path}")

print("所有包含连字符的文件已删除。")
