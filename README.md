# 📊 LLM Evaluation: A Curated Starter Kit  

This repository contains a short curated list of notebooks on LLM evaluation to help get started with **HumanEval**, **DeepEval**, and **LightEval**. These resources consolidate practical examples and tutorials from multiple sources, providing a foundation for assessing large language models' (LLMs) performance across tasks like code generation, reasoning, and benchmarking. The repository also provides a consistent `requirements.txt` files that fixes some install issues met in the sources.

> **Sources and Acknowledgments**:  
> - [HumanEval Benchmark for Evaluating LLM Code Generation Capabilities](https://www.datacamp.com/tutorial/humaneval-benchmark-for-evaluating-llm-code-generation-capabilities)  
> - [DeepEval Tutorial: Evaluate LLMs Effectively](https://www.datacamp.com/tutorial/deepeval)  
> - [Hugging Face Evaluation Guidebook - Comparing Task Formulations](https://github.com/huggingface/evaluation-guidebook/blob/main/contents/examples/comparing_task_formulations.ipynb)  
> - [Hugging Face Smol Course](https://github.com/huggingface/smol-course)  

---

## 📂 Repository Contents  

| Notebook/File                        | Description                                                                                   |  
|--------------------------------------|-----------------------------------------------------------------------------------------------|  
| `test-HumanEval.ipynb`               | Tutorial for using the **HumanEval** benchmark to evaluate LLMs' code generation capabilities, including the pass@k metric. |  
| `deepeval-geval.ipynb`               | Demonstrates the use of **DeepEval**'s G-Eval metric for evaluating LLMs using chain-of-thought (CoT) reasoning. |  
| `deepeval-mmlu.ipynb`                | Benchmarks LLMs using the **MMLU** dataset, which covers 57 diverse subjects via multiple-choice questions. |  
| `deepeval-test.ipynb`                | Pytest-like relevance tests for evaluating LLM outputs using **DeepEval**.                    |  
| `lighteval-custom-huggingface.ipynb` | A walkthrough of **LightEval** for testing Hugging Face models with custom configurations.    |  
| `lighteval-smol-course.ipynb`        | Practical exercises from Hugging Face's **Smol Course** for exploring lightweight evaluation methods. |  
| `requirements.txt`                   | Dependency file to ensure a smooth setup by resolving compatibility issues encountered in other repositories. |  

---

## ✅ How to Use  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/sdelahaies/llm-eval  
   cd llm-eval  
   ```  

2. **Set up the environment**:  
   Install the required dependencies using the provided `requirements.txt` file:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Explore the Notebooks**:  
   Open the notebooks in your favorite Jupyter environment (e.g., Jupyter Notebook, JupyterLab, or VS Code). Each notebook contains examples and explanations to guide you through evaluating LLMs using HumanEval, DeepEval, and LightEval.

---

## 📝 TODO List  

Here's what we aim to improve next:  

- [ ] Add examples of **LightEval** evaluations on additional Hugging Face models.  
- [ ] Integrate **MBPP** and other benchmarks for a broader evaluation of code generation capabilities.  
- [ ] Include a guide on creating custom metrics for DeepEval and LightEval.  

---

## 🚀 Get Involved  

Contributions are welcome! If you find issues or have ideas for improvement, feel free to open an issue or submit a pull request. Let's work together to advance LLM evaluation practices.  

---  

## 💡 Why This Repository?  

Evaluating LLMs is a critical step in understanding their strengths, limitations, and potential applications. By collecting and organizing resources from trusted tutorials and guides, this repository aims to provide a straightforward starting point for me, and other researchers, developers, and enthusiasts venturing into LLM evaluation.  

---

Enjoy exploring, experimenting, and learning! If you found this useful, don't forget to ⭐ the repository!  
