import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def main():
    # initialize tokenizer and model from pretrained GPT2 model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    # make user choose the first word
    sequence = "Hi"
    inputs = tokenizer.encode(sequence, return_tensors='pt')
    # we pass a maximum output length of 200 tokens
    outputs = model.generate(inputs, max_length=200, do_sample=True, temperature=4.0, top_k=50)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(text)
    password_words = text.split()[:5] # first 5 words
    print(password_words)
    password = []
    for i in range(5):
        last_elem = len(password_words[i]) - 1
        if i == 4:
            password.append(password_words[i][0])
        else:
            password.append(password_words[i][0])
            password.append(password_words[i][last_elem])

    print(''.join(password))


if __name__ == "__main__":
    main()
