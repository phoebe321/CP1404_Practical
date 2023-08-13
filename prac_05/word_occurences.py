"""
Word Occurrences
Estimate: 30 minutes
Actual:   60 minutes
"""


def main():
    word_count = count_words()
    align_the_output(word_count)


def count_words():
    text = input("Text: ")
    word_count = {}
    words = text.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def align_the_output(word_count):
    maximum_word_length = max(len(word) for word in word_count.keys())
    for word, count in word_count.items():
        print(f"{word.ljust(maximum_word_length)} : {count}")


main()