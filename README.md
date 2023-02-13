# 视觉-文本实体链接使用说明

## 1. 环境依赖

CUDA版本: 11.7
其他依赖库的安装命令如下：

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
```

## 2. 下载安装

可使用如下命令下载安装算法包：
```bash
pip install ThreeDVG
```

## 3. 使用示例及运行参数说明

### 输入：
data_dict: dict
        {
            point_clouds,
            lang_feat
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
