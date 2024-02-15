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

    phoneme_has_error = False
    phonemes = []
    phoneme_lab_has = []
    dict = {}
    with open(dictionary, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            key = line.split('\t')[0]
            values = (line.split('\t')[1]).split(' ')
            dict.update({key: values})
            for value in values:
                if value not in phonemes:
                    phonemes.append(value)

    print("phonemes:", phonemes)

    for lab_file in lab_files:
        with open(os.path.join(path, f"{lab_file}.lab"), 'r', encoding='utf-8') as f:
            lab = f.read().split(" ")
            for words in lab:
                if words in dict:
                    for phoneme in dict[words]:
                        if phoneme not in phoneme_lab_has:
                            phoneme_lab_has.append(phoneme)
                else:
                    print(f"错误：{lab_file}.lab 中 {words} 不是有效的歌词，请检查。Error: {lab_file}.lab has an invalid word: {words}")
                    phoneme_has_error = True

    print("phoneme_lab_has:", phoneme_lab_has)
    set_phoneme = set(phonemes)
    set_phoneme_lab_has = set(phoneme_lab_has)

    missing = list(set_phoneme - set_phoneme_lab_has)
    if missing != []:
        print("错误：以下音素在数据集中没有找到。Error: The following phonemes are not found in the dataset.")
        print("请尝试补充录制数据．或者使用开源数据集补全音素。Please try to supplement the recording data or use an open-source dataset to complete the phoneme.")
        print(missing)
        if len(missing) > 5:
            print("缺失音素过多，可能导致模型训练失败。Missing phonemes are too many, which may cause the model to fail to train.")
        phoneme_has_error = True

    if not lab_has_error and not length_has_error and not phoneme_has_error:
        print("一切妥当。现在可以使用MFA或者SOFA处理数据了。Everything is fine. Now you can use MFA or SOFA to process the data.")

if __name__ == '__main__':
    progress()