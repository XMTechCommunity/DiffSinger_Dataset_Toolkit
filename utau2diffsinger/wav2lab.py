import os

# 这个程序用于将utau音频文件提取文件名转换为适用于sofa/mfa的lab文件。需要你的采样文件以下划线为分割，且不包含其他元素。
# 例如：a_ba_pa_ma_fa_da_ta.wav
# 文件夹内应该且仅该有wav格式的音频文件。

# 指定需要操作的文件夹路径
folder_path = "采样位置"  # 替换为你的文件夹路径

# 遍历文件夹内的所有文件
for filename in os.listdir(folder_path):
    # 检查是否为文件
    if os.path.isfile(os.path.join(folder_path, filename)):
        # 分离文件名和扩展名
        file_base, file_extension = os.path.splitext(filename)
        
        # 生成新的文件名，保持原文件名不变，仅替换扩展名为.lab
        new_filename = file_base + '.lab'
        
        # 完整的文件路径
        full_file_path = os.path.join(folder_path, new_filename)
        
        # 打开文件并写入内容
        with open(full_file_path, 'w') as lab_file:
            # 写入原文件名，下划线替换为空格
            lab_file.write(new_filename.replace('_', ' ')[:-4])
        
        print(f"已为 {filename} 生成lab：{new_filename}")

print("所有lab文件已经生成完毕。")
