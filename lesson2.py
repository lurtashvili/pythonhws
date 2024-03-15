from random import choice
def random_line(file_name):
    lines = open(file_name).read().splitlines()
    print(lines)
    random_choice = choice(lines)
    print(random_choice)
random_line("txt1.txt")


def word_count(file_name):
    with open(file_name) as f:
        file = f.read().split()
        length = len(file)
    return length
print(word_count("txt1.txt"))
