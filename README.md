
# CodeGPT Fine-tuned for Code Generation

A fine-tuned language model for generating Python code, trained as part of an ML Engineer portfolio project.

## 🔗 Links
- **Model on Hugging Face:** https://huggingface.co/Pradnya27/codegpt-finetuned-code-generation
- **Dataset:** https://huggingface.co/datasets/Rabinovich/Code-Generation-LLM-LoRA

## 📋 Project Summary
Fine-tuned Microsoft's CodeGPT (124M parameters) on coding problems and solutions.
Used Hugging Face Transformers and trained on Google Colab with T4 GPU.

## 📊 Ablation Study — Effect of Training Data Size

| | Experiment 1 | Experiment 2 |
|---|---|---|
| **Training examples** | 500 | 2000 |
| **Epochs** | 2 | 2 |
| **Starting loss** | 4.43 | 3.80 |
| **Final loss** | 2.71 | 2.47 |
| **Improvement** | 39% | 45% |

**Key finding: 4x more data reduced final loss by an additional 9%**

## 📈 Training Loss Curves

### Experiment 1 (500 examples)
| Step | Loss |
|------|------|
| 25 | 4.43 |
| 100 | 3.14 |
| 200 | 2.74 |
| 250 | 2.71 |

### Experiment 2 (2000 examples)
| Step | Loss |
|------|------|
| 50 | 3.80 |
| 200 | 2.97 |
| 500 | 2.69 |
| 800 | 2.35 |
| 1000 | 2.47 |

## 🛠️ How to Run
```bash
pip install transformers datasets accelerate
python train.py
```

## 📁 Files
- `train.py` — training script

## 🔍 Key Learnings
- 4x more training data improved final loss from 2.71 → 2.47
- Loss stabilizes around epoch 1.5 suggesting diminishing returns
- Larger datasets show more consistent loss reduction across steps

## 🔮 Future Work
- Train on full dataset (34,727 examples)
- Experiment with LoRA fine-tuning for efficiency
- Evaluate on HumanEval benchmark
- Try larger base model (CodeGPT-medium)
