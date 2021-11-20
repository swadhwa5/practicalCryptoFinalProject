import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def main():
    # initialize tokenizer and model from pretrained GPT2 model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    sequence = ""
    inputs = tokenizer.encode(sequence, return_tensors='pt')
    # we pass a maximum output length of 200 tokens
    outputs = model.generate(inputs, max_length=200, do_sample=True, temperature=5.0)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(text)


if __name__ == "__main__":
    main()
