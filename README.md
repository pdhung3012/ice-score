# ICE-Score: Instructing Large Language Models to Evaluate Code

_**January 2024**_ - ICE-Score has been accepted to EACL 2024 🎉🎉🎉

---
* [Example](#example)
* [Environment Setup](#environment-setup)
* [Folder Description](#folder-description)
* [Usage](#usage)
* [Citation](#citation)
* [Acknowledgement](#acknowledgement)

## Example
![](./assets/ice-score.png "Example")

## Environment Setup
Our experiment is mainly built on the [codegen-metrics](https://github.com/JetBrains-Research/codegen-metrics) and [code-bert-score](https://github.com/neulab/code-bert-score) repositories. To replicate all experiments, please follow their instructions to set up the environment.


To run `compute_results.ipynb` and modules in `llm-code-eval` folder, use the following command to install all dependencies:
```bash
pip install -r requirements.txt
```


## Folder Description
- `data/` contains all processed data used in the paper.
    - `data/conala/` contains the CoNaLa dataset with all automatic evaluation results.
    - `data/humaneval/` contains the HumanEval dataset with all automatic evaluation results.
      - `data/humaneval/humaneval_java_grade.json`: Java split
      - `data/humaneval/humaneval_cpp_grade.json`: C++ split
      - `data/humaneval/humaneval_python_grade.json`: Python split
      - `data/humaneval/humaneval_js_grade.json`: JavaScript split
 
- `experiment_source/` contains the scripts to collect all automatic evaluation results. They require specific modifications to run on your machine. Note that for any of these scripts using `metrics_evaluation.metrics`, you need to use the implementations in `metrics_evaluation` folder from [codegen-metrics](https://github.com/JetBrains-Research/codegen-metrics).


- `llm_code_eval` contains the implementation of a minimum viable product (MVP) of this project. You are able to use it to evaluate any generated code snippet. Please refer to the `Use Large Language Models To Downstream Tasks Of Source Code` for more details.


## Usage
We implement a minimum viable product (MVP) for this project. To install the project, please use the following command:
```bash
pip install -e .
```
You can use it to evaluate any generated code snippet, with the inputs of `problem`, `output`, `task`, `aspect` and `model`, like the following example:
```python
from llm_code_eval import evaluate

score = evaluate(problem="Given a list of integers, return the sum of all the integers.", 
                    output="sum = 0\nfor i in range(len(list)):\n\tsum += list[i]\nreturn sum", 
                    task="code-gen", aspect="usefulness", model="gpt-3.5-turbo")

print(score)
```

If you want to evaluate with reference code, you can use the option of `reference` in the following example:
```python
from llm_code_eval import evaluate

score = evaluate(problem="Given a list of integers, return the sum of all the integers.", 
                output="sum = 0\nfor i in range(len(list)):\n\tsum += list[i]\nreturn sum", 
                reference="sum = 0\nfor i in range(len(list)):\n\tsum += list[i]\nreturn sum", 
                task="code-gen", aspect="usefulness", model="gpt-3.5-turbo")

print(score)
```


You can also use the option of `cot=True` to enable the zero-shot chain-of-thought evaluation in the following example:
```python
from llm_code_eval import evaluate

score, eval_step = evaluate(problem="Given a list of integers, return the sum of all the integers.", 
                            output="sum = 0\nfor i in range(len(list)):\n\tsum += list[i]\nreturn sum", 
                            task="code-gen", aspect="usefulness", model="gpt-3.5-turbo", cot=True)

print(score)
print(eval_step)
```

## Citation
```
@inproceedings{zhuo2024ice,
  title={ICE-Score: Instructing Large Language Models to Evaluate Code},
  author={Zhuo, Terry Yue},
  booktitle={Findings of the Association for Computational Linguistics: EACL 2024},
  pages={2232--2242},
  year={2024}
}
```

## Acknowledgement
We thank [JetBrains Research](https://research.jetbrains.org/) and [NeuLab](http://www.cs.cmu.edu/~neulab/) for their open-source code and data.
