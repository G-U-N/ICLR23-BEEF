# ICLR23-BEEF

[![LICENSE](https://img.shields.io/badge/license-MIT-green?style=flat-square)](https://github.com/yaoyao-liu/class-incremental-learning/blob/master/LICENSE)[![Python](https://img.shields.io/badge/python-3.8-blue.svg?style=flat-square&logo=python&color=3776AB&logoColor=3776AB)](https://www.python.org/) [![PyTorch](https://img.shields.io/badge/pytorch-1.8-%237732a8?style=flat-square&logo=PyTorch&color=EE4C2C)](https://pytorch.org/)[![CIL](https://img.shields.io/badge/ClassIncrementalLearning-SOTA-success??style=for-the-badge&logo=appveyor)](https://paperswithcode.com/task/incremental-learning)

The code repository for "BEEF: Bi-Compatible Class-Incremental Learning via Energy-Based Expansion and Fusion " [[paper](https://openreview.net/pdf?id=iP77_axu0h3)]

```bibtex
@inproceedings{wang2023beef,
  title={BEEF: Bi-Compatible Class-Incremental Learning via Energy-Based Expansion and Fusion},
  author={Wang, Fu-Yun and Zhou, Da-Wei and Liu, Liu and Ye, Han-Jia and Bian, Yatao and Zhan, De-Chuan and Zhao, Peilin},
  booktitle={The Eleventh International Conference on Learning Representations},
  year={2023}
}
```

## Prerequisites

The following packages are required to run the scripts:

- [torch](https://github.com/pytorch/pytorch)
- [torchvision](https://github.com/pytorch/vision)
- [tqdm](https://github.com/tqdm/tqdm)
- [numpy](https://github.com/numpy/numpy)

## Training scripts

- Train CIFAR-100

  ```
  python main.py --config=./configs/beef/cifar-50-10.json
  ```
- Train ImageNet-100

  ```
  python main.py --config=./configs/beef/imagenet-50-10.json
  ```
- Train imbalanced protocols

  ```
  python main.py --config=./configs/beef/cifar-50-10-random.json # uniform ramdom type
  
  python main.py --config=./configs/beef/cifar-50-10-imbalance-1.json # half-half-type
  
  python main.py --config=./configs/beef/cifar-50-10-imbalance-0.9.json # exp type
  ```


Remember to change `YOURDATAROOT` into your own data root, or you will encounter errors.

## Results

 Experimental results show that our method achieves state-of-the-art performance.

| Protocols                | Reproduced Avg | Reported Avg |
| ------------------------ | -------------- | ------------ |
| CIFAR-100 B50 5 steps    | 71.75          | 71.70        |
| ImageNet-100 B50 5 steps | 78.48          | 77.27        |
| CIFAR-100 uniform        | 70.85          | 71.08        |
| CIFAR-100 half-half      | 67.72          | 66.81        |
| CIFAR-100 exp            | 68.86          | 67.85        |

## Contact

If there are any questions, please feel free to contact the author: Fu-Yun Wang ([wangfuyun@smail.nju.edu.cn](mailto:wangfuyun@smail.nju.edu.cn)). Enjoy the code.
