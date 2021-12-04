from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random
import sys

# choose two random positions and if it overflows, use the last letter
# remove any words more than 3 letters

# Added parameters
# have parameters to capitalize some words in between
# have parameters to include numbers in the password

def main():
    args = sys.argv
    capitalize_word = args[1].lower()
    add_number_in_sentence = args[2].lower()

    # initialize tokenizer and model from pretrained GPT2 model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    sequence = "The"
    inputs = tokenizer.encode(sequence, return_tensors='pt')
    # we pass a maximum output length of 200 tokens
    outputs = model.generate(inputs, max_length=200, do_sample=True, temperature=2.0, top_k=50)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    text = text.split()
    # print(text)

    # make lower case
    for i in range(len(text)):
        text[i] = text[i].lower()

    new_text = []
    # remove words with length <= 3
    for word in text:
        if len(word) > 3:
            new_text.append(word)

    text = new_text

    new_text = []
    # remove words that don't contain letters
    for word in text:
        if word.isalpha():
            new_text.append(word)

    text = new_text

    # print(text)

    num_words = 6
    password_words = text[0:num_words]  # first 6 words
    print("Your final sentence is: ", password_words)

    # have parameters to capitalize some words in between
    if capitalize_word == "true":
        print("You have chosen to capitalize a word in your sentence!")
        random_pos = random.sample(range(0, 6), 1)[0]
        password_words[random_pos] = password_words[random_pos].upper()
        print("So, now your final sentence is: ", password_words)


    # chose random letter positions
    random_pos_1 = random.sample(range(0, 3), 1)[0]
    random_pos_2 = random.sample(range(0, 10), 1)[0]

    if random_pos_2 < random_pos_1:
        temp = random_pos_1
        random_pos_1 = random_pos_2
        random_pos_2 = temp

    print("Pick letters from each word at positions:", [random_pos_1, random_pos_2])

    password = []
    for i in range(num_words):
        if random_pos_2 > len(password_words[i]) - 1:
            random_pos_2 = len(password_words[i]) - 1
        password.append(password_words[i][random_pos_1])
        password.append(password_words[i][random_pos_2])

    final_password = ''.join(password)
    # print(final_password)

    final_password_array = list(final_password)

    if add_number_in_sentence == "true":
        print("You have chosen to add digits to your sentence!")
        # have parameters to include numbers in the password
        num_random_positions = random.sample(range(1, 4), 1)[0]
        random_positions = random.sample(range(1, 7), num_random_positions)
        random_positions.sort()
        random_digit = random.sample(range(0, 10), 1)[0]
        print("Add digit:", random_digit, "before words:", random_positions)
        for i in range(num_random_positions):
            final_password_array.insert((2 * (random_positions[i] - 1)) + i, str(random_digit))

    final_password = ''.join(final_password_array)
    print("You final password is: ", final_password)


if __name__ == "__main__":
    main()
