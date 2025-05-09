from stats import number_of_words
from stats import symbol_breakdown
from stats import sort_dictionaries

def get_book_text(filepath):
    with open(filepath) as opened:
        text = opened.read()
    return text

def main():
    frankenstein = get_book_text("/home/rachen/workspace/github.com/boot.dev/bookbot/books/frankenstein.txt")
    print(frankenstein)


def test():
    frankenstein = get_book_text("/home/rachen/workspace/github.com/boot.dev/bookbot/books/frankenstein.txt")
    num = number_of_words(frankenstein)
    dict = symbol_breakdown(frankenstein)
    list = sort_dictionaries(dict)
    return print(f"============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num} total words
--------- Character Count -------
{list["char"]}: {dict["num"]}
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ==============="

    
test()
