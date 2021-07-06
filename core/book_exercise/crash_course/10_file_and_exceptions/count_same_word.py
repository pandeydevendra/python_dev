def given_word_count(filename, search_word):
    with open(filename, 'r') as f_obj:
        w_count = 0
        for line in f_obj:
            # print(line, type(line))
            l_w_count = line.lower().count(search_word)
            # print(l_w_count)
            w_count += l_w_count
        print(f"""The word {search_word} occured {w_count} times in the {filename} file.""")


given_word_count('programming.txt', 'love')
given_word_count('alice.txt', 'the')
given_word_count('siddhartha.txt', 'siddhartha')