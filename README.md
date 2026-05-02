
# CodeGPT Fine-tuned for Code Generation

Fine-tuned Microsoft's CodeGPT (124M parameters) for code generation using full fine-tuning and LoRA.

## 🔗 Links
- **Live Demo:** https://huggingface.co/spaces/Pradnya27/code-generator
- **Best Model (Full Fine-tune):** https://huggingface.co/Pradnya27/codegpt-finetuned-code-generation
- **LoRA Model:** https://huggingface.co/Pradnya27/codegpt-lora-code-generation
- **Dataset:** https://huggingface.co/datasets/Rabinovich/Code-Generation-LLM-LoRA

## 📋 Project Summary
Systematically fine-tuned CodeGPT using 4 experiments comparing dataset sizes and training methods.

## 📊 Full Ablation Study

| | Exp 1 | Exp 2 | Exp 3 | Exp 4 (LoRA) |
|---|---|---|---|---|
| **Training examples** | 500 | 2000 | 5000 | 5000 |
| **Method** | Full | Full | Full | LoRA |
| **Starting loss** | 4.43 | 3.80 | 3.39 | 4.28 |
| **Final loss** | 2.71 | 2.47 | 2.31 | 3.14 |
| **Trainable params** | 124M | 124M | 124M | 589K (0.36%) |
| **Model size** | 651MB | 651MB | 651MB | 2.36MB |
| **Improvement** | 39% | 45% | 48% | 27% |

## 🔍 Key Findings
- More data consistently improves performance (500→5000 examples: 2.71→2.31 loss)
- LoRA is 275x smaller and 35% faster but full fine-tuning achieves lower loss
- For production with limited GPU budget, LoRA is preferred
- For maximum accuracy, full fine-tuning wins

## 🛠️ How to Run
```bash
pip install transformers datasets accelerate peft
python train.py
```

## 🔮 Future Work
- Train on full dataset (34,727 examples)
- Evaluate on HumanEval benchmark
- Try larger base model (CodeGPT-medium)
- Experiment with higher LoRA rank (r=32, r=64)
