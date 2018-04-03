import collections


def main():
    user_input = input('Enter words here: ')
    user_input.join(' ')
    words = list()
    nonalpha_index = [index for index, char in enumerate(user_input, 0) if not char.isalpha()]
    nonalpha_index.append(len(user_input))
    nonalpha_index.insert(0,0)
    for num in range(len(nonalpha_index)- 1):
        if nonalpha_index[num] + 1 == nonalpha_index[num + 1]:
            continue
        else:
            words.append(user_input[nonalpha_index[num]:nonalpha_index[num + 1]].strip().lower())
    words = sorted(words)
    count_for_each_word = [words.count(words[index]) for index in range(len(words))]
    word_count = collections.OrderedDict(zip(sorted(words), count_for_each_word))
    longest_key = max([len(word) for word in words])
    for key in word_count:
        spacing = ((longest_key-len(key))*' ')
        print('{0}{1} : {2}'.format(key, spacing, word_count[key]))


main()