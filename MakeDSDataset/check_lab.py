import click
import os

@click.command()
@click.option('--path', help='source folder')
@click.option('--dictionary', help='dictionary folder')
def progress(path, dictionary):
    if not os.path.isdir(path):
        print(f'Path {path} does not exist')
        return
    if not os.path.isfile(dictionary):
        print(f'Dictionary {dictionary} does not exist')
        return
    
    print(path,dictionary)


    files = os.listdir(path)
    
    # 创建两个字典，分别存储.wav和.lab文件的文件名（不包含扩展名）
    wav_files = {os.path.splitext(file)[0] for file in files if file.endswith('.wav')}
    lab_files = {os.path.splitext(file)[0] for file in files if file.endswith('.lab')}
    
    # 检查.wav文件是否有对应的.lab文件
    has_error = False
    for wav_base in wav_files:
        if wav_base not in lab_files:
            print(f"Error: {wav_base}.wav does not have a corresponding .lab file.")
            has_error = True
    
    # 检查.lab文件是否有对应的.wav文件
    for lab_base in lab_files:
        if lab_base not in wav_files:
            print(f"Error: {lab_base}.lab does not have a corresponding .wav file.")
            has_error = True

    # 如果没有错误，打印成功提示
    if not has_error:
        print("All files are paired successfully.")


if __name__ == '__main__':
    progress()