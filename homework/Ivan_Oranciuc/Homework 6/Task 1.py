text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,"
        " dignissim vitae libero")

words = text.split()

updated_words = []

for word in words:
    if word[-1] in ',.':
        without_punctuation = word[:-1]
        with_punctuation = word[-1]
        updated_word = without_punctuation + 'ing' + with_punctuation
    else:
        updated_word = word + 'ing'

    updated_words.append(updated_word)

result = ' '.join(updated_words)

print(result)
