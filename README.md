# 由XMTech维护的DiffSinger数据集制作工具包

## MakeDSDataset --> 常规声库数据集制作工具

### check_lab.py
检查拼音标注文件是否正确

用法：

```bash
python check_lab.py --path /path/to/dataset --dictionary /path/to/dictionary
```
其中，将/path/to/dataset替换为待检测数据集的路径，将/path/to/dictionary替换为字典文件的路径

### htk2csv.py
将HTK格式的音素标记转换为CSV格式

用法：

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

### build_dataset.py
这个脚本来自于OpenVPI仓库，可参考：
https://ecn4x4y9jhjs.feishu.cn/wiki/J4lZwVCryiuEUrkU7y3cHAJ3npf

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

### 价目表
价目表仅供参考，实际价格以我们实际报价为准。

#### UTAU声库转制（支持中文/日语 CVVC/VCV）


四阶及以内 200元<br>
+1阶 20元<br>
提供训练检查点权重，以及适用于OpenUtau/后续可能的编辑器声库

#### 歌声数据全自动标注 
350元<br>
提供训练检查点权重，以及适用于OpenUtau/后续可能的编辑器声库

#### 歌声数据歌词级手动标注（中文，日语）
45分钟内 599元<br>
+30分钟 150元<br>
随附数据修复服务，可选提供修复后干声<br>
提供MinLabel生成的json与lab文件<br>
提供训练检查点权重，以及适用于OpenUtau/后续可能的编辑器声库

#### 歌声数据音素级手动标注（中文，日语）
45分钟内 1399元<br>
+30分钟 699元<br>
随附数据修复服务，可选提供修复后干声<br>
提供MinLabel生成的json与lab文件<br>
提供vlabeler标注产生的htk lab文件<br>
提供训练检查点权重，以及适用于OpenUtau/后续可能的编辑器声库