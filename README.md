# 3D Visual Grounding使用说明

## 1. 算法描述

3D Visual Grounding是指机器接收到一组点云数据和language信息之后，给出language信息所对应的相关物体的点云。

## 2. 环境依赖及安装

CUDA版本: 11.7
其他依赖库的安装命令如下：

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
pip install "git+git://github.com/erikwijmans/Pointnet2_PyTorch.git#egg=pointnet2_ops&subdirectory=pointnet2_ops_lib"
pip install ThreeDVG
```

## 3. 使用示例

### 输入：
data_dict: dict
        {
            point_clouds,
            lang_num，
            lang_feat_list，
            lang_len_list，
            main_lang_feat_list，
            main_lang_len_list，
            first_obj_list，
            unk_list，
            unk，
            istrain
        }

point_clouds: Variable(torch.cuda.FloatTensor)
        (B, N, 3 + input_channels) tensor
        Point cloud to run predicts on
        Each point in the point-cloud MUST
        be formated as (x, y, z, features...)

### 随机数据测试：

```python
import os
import torch
import argparse
import numpy as np
from ThreeDVG  import MM3DVG
os.environ["CUDA_VISIBLE_DEVICES"] = "6"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_proposals", type=int, default=256, help="Proposal number [default: 256]")
    parser.add_argument("--no_lang_cls", action="store_true", help="Do NOT use language classifier.")
    parser.add_argument("--use_bidir", action="store_true", help="Use bi-directional GRU.")
    parser.add_argument("--no_height", action="store_true", help="Do NOT use height signal in input.")
    parser.add_argument("--use_color", action="store_true", help="Use RGB color in input.")
    parser.add_argument("--use_normal", action="store_true", help="Use RGB color in input.")
    parser.add_argument("--use_multiview", action="store_true", help="Use multiview images.")

    args = parser.parse_args()

    data_dict = {}
    point_clouds = torch.ones([1, 10, 4]).cuda()
    data_dict['point_clouds'] = point_clouds

    data_dict["lang_num"] = 1
    data_dict["lang_feat_list"] = torch.zeros([1, 1, 126, 300]).cuda()
    data_dict["lang_len_list"] = torch.Tensor([10]).cuda()
    data_dict["main_lang_feat_list"] = torch.zeros([1, 1, 126, 300]).cuda()
    data_dict["main_lang_len_list"] = torch.Tensor([10]).cuda()
    data_dict["first_obj_list"] = torch.Tensor([0]).cuda()
    data_dict["unk_list"] = torch.zeros([1, 300]).cuda()
    data_dict["unk"] = torch.zeros([1, 300]).cuda()
    data_dict["istrain"] = torch.Tensor([0]).cuda()
    GLOVE_PICKLE = "/data/zhaoyj/mmkg-3d-3dvg/glove.p"
    bbox = MM3DVG(args=args).inference(data_dict=data_dict)
```

## 4. 参数说明

```
point_clouds            点云数据 B, N, 3+1+128(multiview)
lang_num，              句子数，默认1 
lang_feat_list，        glove映射后的句子 B, N, 单词数, 映射维度（300）
lang_len_list，         句子单词数
main_lang_feat_list，   glove映射后的重要的一句，只有一句话则默认本身 B, N, 单词数, 映射维度（300）
main_lang_len_list，    句子单词数
first_obj_list，        句子中第一个重要的单词
unk_list，              glove中未对应的单词列表
unk，                   glove中未对应的单词
istrain                 是否为训练模式，为否
```

## 5. 论文引用

本项目代码使用了ICCV 2021的3DVG-Transformer，其提出了一个基于transformer的模型用于解决3D Visual Grounding任务，并取得了SOTA效果。