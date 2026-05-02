
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer

# Load dataset
dataset = load_dataset("Rabinovich/Code-Generation-LLM-LoRA")

# Load model
model_name = "microsoft/CodeGPT-small-py"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model_name)

def preprocess(examples):
    combined = [q + tokenizer.eos_token + a for q, a in zip(examples["question"], examples["answer"])]
    out = tokenizer(combined, max_length=256, truncation=True, padding="max_length")
    out["labels"] = out["input_ids"].copy()
    return out

# Experiment 1 - 500 examples
small_dataset = dataset["train"].select(range(500))
tokenized_dataset = small_dataset.map(preprocess, batched=True, remove_columns=["question", "answer"])

training_args = TrainingArguments(
    output_dir="./codegpt-finetuned",
    num_train_epochs=2,
    per_device_train_batch_size=4,
    logging_steps=25,
    learning_rate=5e-5,
    report_to="none",
)

trainer = Trainer(model=model, args=training_args, train_dataset=tokenized_dataset)
trainer.train()
model.push_to_hub("Pradnya27/codegpt-finetuned-code-generation")
tokenizer.push_to_hub("Pradnya27/codegpt-finetuned-code-generation")
