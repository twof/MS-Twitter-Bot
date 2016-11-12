import sys


def open_doc(source_text):
    doc = open(source_text)
    lines = doc.readlines()
    return lines


def gen_histogram_dict(lines):
    hist_dict = {}

    if isinstance(lines, list):
        for line in lines:
            for word in line.split(' '):
                stripped_word = ''.join([i for i in word if i.isalpha()])
                if stripped_word != '':
                    if stripped_word in hist_dict:
                        hist_dict[stripped_word] += 1
                    else:
                        hist_dict[stripped_word] = 1
    else:
        for word in line.split(' '):
            stripped_word = ''.join([i for i in word if i.isalpha()])
            if stripped_word != '':
                if stripped_word in hist_dict:
                    hist_dict[stripped_word] += 1
                else:
                    hist_dict[stripped_word] = 1

    return hist_dict


def unique_words(hist_dict):
    return len(hist_dict)


def frequency(word, hist_dict):
    if word not in hist_dict:
        return 0
    else:
        return hist_dict[word]
