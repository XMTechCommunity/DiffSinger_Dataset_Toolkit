import os
from pathlib import Path
from pydub import AudioSegment

# 设置音频文件夹地址
audio_dir = "your_audio_folder_path"

# 获取文件夹下所有wav文件
files = [f for f in os.listdir(audio_dir) if f.endswith('.wav')]

# 按四个wav文件分组
groups = [files[i:i+4] for i in range(0, len(files), 4)] 

#进行wav音频的合并
for group in groups:

    # 如果文件数不足4个,使用剩余文件进行合并
    if len(group)<4:
        group = group + ['']*(4-len(group)) 

    # 按文件名顺序进行合并    
    out_name = '_'.join([f[:f.index('.')] for f in group if f]) + '.wav'
    out_path = Path(audio_dir+"\out", out_name)

    combined = AudioSegment.empty()
    for f in group:
        if f:
            combined += AudioSegment.from_wav(Path(audio_dir, f))
    
    # 保存合并结果    
    combined.export(out_path, format="wav")