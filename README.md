
# CodeGPT Fine-tuned for Code Generation

A fine-tuned language model for generating Python code, trained as part of an ML Engineer portfolio project.

## 🔗 Links
- **Live Demo:** https://huggingface.co/spaces/Pradnya27/code-generator
- **Model on Hugging Face:** https://huggingface.co/Pradnya27/codegpt-finetuned-code-generation
- **Dataset:** https://huggingface.co/datasets/Rabinovich/Code-Generation-LLM-LoRA

## 📋 Project Summary
Fine-tuned Microsoft's CodeGPT (124M parameters) on coding problems and solutions.
Used Hugging Face Transformers and trained on Google Colab with T4 GPU.

## 📊 Ablation Study — Effect of Training Data Size

| | Experiment 1 | Experiment 2 | Experiment 3 |
|---|---|---|---|
| **Training examples** | 500 | 2000 | 5000 |
| **Epochs** | 2 | 2 | 2 |
| **Starting loss** | 4.43 | 3.80 | 3.39 |
| **Final loss** | 2.71 | 2.47 | 2.31 |
| **Improvement** | 39% | 45% | 48% |

**Key finding: More training data consistently improves model performance.
5000 examples reduced final loss by 48% vs 39% for 500 examples.**

## 📈 Experiment 3 Training Loss (Best Model)
| Step | Loss |
|------|------|
| 100 | 3.39 |
| 300 | 2.77 |
| 500 | 2.59 |
| 700 | 2.44 |
| 900 | 2.30 |
| 1200 | 2.31 |

## 🛠️ How to Run
```bash
pip install transformers datasets accelerate
python train.py
```

## 📁 Files
- `train.py` — training script

## 🔍 Key Learnings
- 10x more data (500→5000) improved final loss from 2.71 → 2.31
- Diminishing returns observed after step 900 — loss plateaued around 2.31
- Larger datasets show more stable and consistent loss reduction

## 🔮 Future Work
- Train on full dataset (34,727 examples)
- Experiment with LoRA fine-tuning for efficiency
- Evaluate on HumanEval benchmark
- Try larger base model (CodeGPT-medium)
