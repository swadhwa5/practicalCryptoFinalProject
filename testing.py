import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random
import sys

chars = []
words = []
bigrams = []
# initialize tokenizer and model from pretrained GPT2 model

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
sequence = "The"
inputs = tokenizer.encode(sequence, return_tensors='pt')

capitalize_word = "true"
add_number_in_sentence = "false"

for _ in range(1000):
    # initialize tokenizer and model from pretrained GPT2 model
    # we pass a maximum output length of 200 tokens
    outputs = model.generate(inputs, max_length=200, do_sample=True, temperature=2.0, top_k=50)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    text = text.split()

    for i in range(len(text)):
        text[i] = text[i].lower()

    new_text = []

    for word in text:
        if len(word) > 3:
            new_text.append(word)

    text = new_text

    new_text = []

    for word in text:
        if word.isalpha():
            new_text.append(word)

    text = new_text


    num_words = 6
    password_words = text[0:num_words]  # first 6 words
    # print("Your final sentence is: ", password_words)

    if (len(password_words) < 6):
      continue

    # have parameters to capitalize some words in between
    if capitalize_word == "true":
        # print("You have chosen to capitalize a word in your sentence!")
        random_pos = random.sample(range(0, 6), 1)[0]
        password_words[random_pos] = password_words[random_pos].upper()
        # print("So, now your final sentence is: ", password_words)


    # chose random letter positions
    random_pos_1 = random.sample(range(0, 3), 1)[0]
    random_pos_2 = random.sample(range(0, 10), 1)[0]

    if random_pos_2 < random_pos_1:
        temp = random_pos_1
        random_pos_1 = random_pos_2
        random_pos_2 = temp

    # print("Pick letters from each word at positions:", [random_pos_1, random_pos_2])

    for i in range(num_words):
        if random_pos_2 > len(password_words[i]) - 1:
            random_pos_2 = len(password_words[i]) - 1

        chars.append(password_words[i][random_pos_1])
        chars.append(password_words[i][random_pos_2])

        bigrams.append(password_words[i][random_pos_1] + password_words[i][random_pos_2])

        words.append(password_words[i])


    # if add_number_in_sentence == "true":
    #     print("You have chosen to add digits to your sentence!")
    #     # have parameters to include numbers in the password
    #     num_random_positions = random.sample(range(1, 4), 1)[0]
    #     random_positions = random.sample(range(1, 7), num_random_positions)
    #     random_positions.sort()
    #     random_digit = random.sample(range(0, 10), 1)[0]
    #     print("Add digit:", random_digit, "before words:", random_positions)
    #     for i in range(num_random_positions):
    #         final_password_array.insert((2 * (random_positions[i] - 1)) + i, str(random_digit))

    # final_password = ''.join(final_password_array)
    # print("You final password is: ", final_password)
c = Counter(chars)
plt.bar(*zip(*c.most_common()), width=.5, color='g')
plt.show()

c = Counter(words)
plt.bar(*zip(*c.most_common()), width=.5, color='r')
plt.show()

c = Counter(bigrams)
plt.bar(*zip(*c.most_common()), width=.5, color='b')
plt.show()