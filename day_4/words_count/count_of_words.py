from collections import Counter
def words_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())

print(words_count("input.txt"))
