# ChartEdit: How Far Are MLLMs From Automating Chart Analysis? Evaluating MLLMs' Capability via Chart Editing (ACL 2025 Findings)

[![🤗 Benchmark](https://img.shields.io/badge/Benchmark-HuggingFace-FFD21E.svg?logo=huggingface&logoColor=yellow)](https://huggingface.co/datasets/xxxllz/ChartEdit) [![📑 Paper (arXiv:2505.11935)](https://img.shields.io/badge/arXiv-2505.11935-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2505.11935)

This is the official repo of [ChartEdit](https://arxiv.org/abs/2505.11935).

> ChartEdit: How Far Are MLLMs From Automating Chart Analysis? Evaluating MLLMs' Capability via Chart Editing
>
> Xuanle Zhao*, Xuexin Liu*, Haoyue Yang*, Xianzhen Luo, Fanhu Zeng, Jianling Li, Qi Shi†, Chi Chen†


## Overview
The main pipeline for constructing the ChartEdit benchmark. 
![image](fig/main.png)

## Evaluation
Please first download the benchmark from [HuggingFace](https://huggingface.co/datasets/xxxllz/ChartEdit) and follow the ```generate_openai.py``` to generate the output code.

See ```eval``` for evaluating model performance from chart and code levels.


## Case Study
![image](fig/case.png)

## Citation
```
@article{zhao2025chartedit,
  title={ChartEdit: How Far Are MLLMs From Automating Chart Analysis? Evaluating MLLMs' Capability via Chart Editing},
  author={Zhao, Xuanle and Liu, Xuexin and Yang, Haoyue and Luo, Xianzhen and Zeng, Fanhu and Li, Jianling and Shi, Qi and Chen, Chi},
  journal={arXiv preprint arXiv:2505.11935},
  year={2025}
}
```
