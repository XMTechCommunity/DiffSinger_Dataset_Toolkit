import os

def add_suffix_to_files(directory, suffix):
    # 获取目录下的所有文件
    files = os.listdir(directory)

    for file_name in files:
        # 检查文件是否是普通文件
        if os.path.isfile(os.path.join(directory, file_name)):
            # 分割文件名和扩展名
            name, ext = os.path.splitext(file_name)
            # 构建新的文件名
            new_file_name = f"{name}_{suffix}{ext}"
            # 重命名文件
            os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))

    print("已完成文件重命名操作。")

# 指定工作目录和后缀
directory = "."  # 当前目录
suffix = "F4"

# 调用函数
add_suffix_to_files(directory, suffix)