# 由XMTech维护的DiffSinger数据集制作工具包

## MakeDSDataset --> 常规声库数据集制作工具

### check_lab.py
检查拼音标注文件是否正确

```bash
python check_lab.py --path /path/to/dataset --dictionary /path/to/dictionary
```
其中，将/path/to/dataset替换为待检测数据集的路径，将/path/to/dictionary替换为字典文件的路径

### htk2csv.py
将HTK格式的音素标记转换为CSV数据集标注文件

```bash
python htk2csv.py /path/to/htk_file [可选：--output /path/to/new_csv_path]
```
请在单个文件夹按以下结构放置wav和htk格式的lab文件：
```bash
opencpop
└── 2001000026.wav
└── 2001000026.lab
```
然后将/path/to/htk_file指向实际的标注文件

如果需要将转换后的文件保存到其他位置，请使用--output参数指定新路径

### generate_ph_num.py
为CSV数据集标注文件生成ph_num字段<br>
（ph_num代表多少个音素属于一个单词，训练唱法模型中的dur时需要）
```bash
python generate_ph_num.py --csv_path /path/to/csv_file --dictionary /path/to/dictionary
```
其中，将/path/to/csv_file替换为待生成ph_num字段的CSV格式标注文件，将/path/to/dictionary替换为字典文件的路径<br>
请确保你的标注文件与所使用字典配套

### csv2htk.py
**非必要，仅为数据集维护使用**<br>
将CSV格式的数据集标注文件转换回htk lab文件
```bash
python csv2htk.py /path/to/csv_file --output /path/to/new_htk_path
```
其中，将/path/to/csv_file替换为待转换的CSV格式标注文件，将/path/to/new_htk_path指向导出htk lab文件的路径


### build_dataset.py
这个脚本来自于OpenVPI仓库，可参考：
https://ecn4x4y9jhjs.feishu.cn/wiki/J4lZwVCryiuEUrkU7y3cHAJ3npf<br>
在本流程弃用，仅为使用OpenVPI数据集制作流程产生的标注文件提供兼容。<br>
你可以尝试使用本脚本将OpenVPI数据集制作流程产生的TextGrid标注文件转换为csv格式，并使用csv2htk.py将转换后的CSV格式标注文件转换为HTK格式。<br>
**使用--skip_silence_insertion可防止此脚本对音频及标注文件添加静音。**

## utau2ds --> UTAU声库转DiffSinger数据集工具

### main.ipynb
使用VSCode或者Jupyter Notebook打开，按提示运行即可

### audiomix.py
将较短的音频混合为长音频，以适用于MFA推理，现已弃用。

SOFA已可精确推理短音频。

## dsdict_tool --> OpenUtau字典制作工具

### add_prefix.py
将原版dsdict词典添加多语种前缀
```bash
python add_prefix.py -i /path/to/dsdict.yaml -o /path/to/new_dsdict.yaml -p zh
```
将/path/to/dsdict.yaml替换为原字典的路径，将/path/to/new_dsdict.yaml替换为目标路径，将zh替换为需要添加的前缀。<br>
不指定/path/to/new_dsdict.yaml，会在源路径生成一个updated_原名的yaml文件。<br>
不指定-p参数，会默认添加zh前缀。

### dictionary_to_dsdict.py
将训练字典转换为dsdict.yaml字典
```bash
python dictionary_to_dsdict.py -i /path/to/dictionary.txt -o /path/to/dsdict.yaml
```
将/path/to/dictionary.txt替换为训练字典的路径，将/path/to/dsdict.yaml替换为目标路径。<br>
请注意，生成的dsdict.yaml字典不包含symbols字段，请在生成字典后手动整理并添加symbols字段。

## 小广告

如果你对DiffSinger制作流程感到困惑，或因设备性能问题无法完成数据集制作流程，可联系XMTech团队为您提供声库代制作服务。

我们会在审核您的采样来源合法性以及采样质量后，向您收取少许费用用于人工成本付出以及算力服务器租赁。

我们会拒绝包括但不限于以下来源的采样用于声库制作：
 - 1.政府人员或知名从政业者的声音采样，即使他们已授权并专门为歌声合成软件录制声音采样。
 - 2.明显来自音频分离软件产生的干声
 - 3.听感上近似于知名演绎者的声音采样，您需要证明声音来源的合法性
 - 4.如果采样来源于知名演绎者，您还需请声音提供者使用已认证账号向XMTech成员发送信息以验证身份。
 - 5.（待补充）

如有需要，可在[Bilibili 私信](https://space.bilibili.com/51208271)联系XMTech成员获取代制作服务详细价格信息。