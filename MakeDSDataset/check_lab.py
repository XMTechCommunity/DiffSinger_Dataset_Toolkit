import click
import os
from pydub import AudioSegment

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

    files = os.listdir(path)
    
    wav_files = {os.path.splitext(file)[0] for file in files if file.endswith('.wav')}
    lab_files = {os.path.splitext(file)[0] for file in files if file.endswith('.lab')}
    
    lab_has_error = False
    for wav_base in wav_files:
        if wav_base not in lab_files:
            print(f"错误：{wav_base}.wav 没有对应的 .lab 文件。Error: {wav_base}.wav does not have a corresponding .lab file.")
            lab_has_error = True
    
    for lab_base in lab_files:
        if lab_base not in wav_files:
            print(f"错误：{lab_base}.lab 没有对应的 .wav 文件。Error: {lab_base}.lab does not have a corresponding .wav file.")
            lab_has_error = True

    length_has_error = False
    for wav_file in wav_files:
        wav_path = os.path.join(path, f"{wav_file}.wav")
        audio = AudioSegment.from_wav(wav_path)
        if audio.duration_seconds > 25:
            print(f"警告：{wav_file}.wav 过长。Warning: {wav_file}.wav is too long.")
            length_has_error = True
    if length_has_error:
        print("过长的音频可能会造成训练时显存溢出。Too long audio files may cause CUDA Out Of Memory.")

    if not lab_has_error and not length_has_error:
        print("All files are paired successfully.")



if __name__ == '__main__':
    progress()
