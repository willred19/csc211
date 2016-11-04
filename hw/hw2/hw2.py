'''HW02: Python Review

These problems are (somewhat) representative of the sorts of
programming tasks you will need to be able to perform to create the
applications this class is designed to teach. You will (hopefully) be
able to solve these problems directly, but if you are having trouble
with them, then please use these problems as motivation for further
study.

Use the "Exercises" section from each chapter in "How to Think Like a
Computer Scientist" as a reference for further study.

'''

#----------------------------------------------------------------------
# Problem 0
#
# Create a function 'random_list' that generates a list containing 100
# random integers between 0 and 1000 (use iteration, append, and the
# random module).
#
# name: random_list
# parameters: none
# returns: (list) list of random integers between 0 and 1000
#
# Code goes below here
import random
def random_list():
    rannum = []
    for i in range (100):
        rannum.append(random.randrange(1, 1000))
    return rannum






#----------------------------------------------------------------------
# Problem 0.5
#
# Write a function called 'average' with a single parameter, 'numbers'
# (list), and return the average of all the numbers in that list.
#
# name: average
# parameters:
# - numbers (list)
# returns: (float) average of all the numbers in the list
#
# Code goes below here
def average(numbers):
    tot = sum(numbers)
    tot = sum(numbers) /len(numbers)
    return tot






#----------------------------------------------------------------------
# Problem 1
#
# Write a function to count how many even numbers are in a given
# list. Your function should be named "count_even" and it should take
# one parameter, "numbers" (a list).
#
# name: count_even
# parameters:
# - numbers (list)
# returns: (int) count of even numbers in the list
#
# Code goes below here
def count_even(numbers):
    even = 0
    for n in numbers:
        if n % 2 == 0:
            even = even + 1
    return even





#----------------------------------------------------------------------
# Problem 2
#
# Write a function to sum all the even numbers in a given list. Your
# function should be named "sum_even" and it should take one
# parameter, "numbers" (a list).
#
# name: sum_even
# parameters:
# - numbers (list)
# returns: (int) sum of even numbers in list
#
# Code goes below here
def sum_even(numbers):
    add = 0
    for n in numbers:
        if n % 2 == 0:
            add = add + n
    return add






#----------------------------------------------------------------------
# Problem 3
#
# What is the longest word in Alice in Wonderland? You can obtain a
# free plain text version of the book, along with many others, from
# http://www.gutenberg.org. Go to this website and download the text
# of Alice in Wonderland. You will need to then upload it to your
# homework directory:
#
# /home/<username>/csc211/hw/hw2/<name_of_alice_textfile>
#
# To solve this problem, you will be creating TWO functions.
#
# Create a function 'word_count' that takes one parameter, "text" (a
# string), and returns a dictionary of all the words in this string.
#
# name: word_count
# parameters:
# - text (str)
# returns: (dict) map of word to count of occurrences
#
# You will also create a function 'longest_word_in_alice' that takes
# no parameters. It should:

#
# - Open the text file for "Alice in Wonderland" from gutenberg.org
# - Read the content into a string
# - Call 'word_count', retrieving the dictionary it returns
# - Find the longest word in that dictionary and return it
#
# name: longest_word_in_alice
# parameters: none
# returns: (str) longest word in "Alice in Wonderland"
#
# Code goes below here






#----------------------------------------------------------------------
# Problem 4
#
# KJV Bible class
#
# Create a new class, called 'Bible', that will provide an interface
# to the content of the 1611 King James translation of the Holy
# Bible. It should have a number of methods:
#
# - __init__ [i.e constructor]: The constructor should:
#     - take no parameters
#     - call the provided function 'read_bible' to load the Bible data
#       structure into memory
#     - save this data structure as the attribute 'verses'.
#
# - get_book
#
#    parameters:
#      - book (str): name of book to return
#
#    returns: (list) list of individual verse data structures (from
#       self.verses) whose book is equal to the given book name
#
# - get_chapter
#
#    parameters:
#      - book (str): name of book from which to find the chapter
#      - chapter (int): chapter number to return
#
#    returns: (list) list of individual verse data structures (from
#       self.verses) whose book is equal to the given book name and
#       whose chapter number is equal to the given chapter number
#
# - get_verse
#
#    parameters:
#      - book (str): name of book from which to find the chapter
#      - chapter (int): chapter number to return
#      - verse (int): verse number to return
#
#    returns: (list) list of individual verse data structures (from
#       self.verses) whose book is equal to the given book name and
#       whose chapter number is equal to the given chapter number and
#       whose verse number is equal to the given verse number
#
# EXTRA CREDIT
#
# - n_grams (ref: https://en.wikipedia.org/wiki/N-gram)
#
#    parameters:
#      - size (int): size of n-grams from which to build the table
#      - book (str, optional, default=None): name of book from which
#          to build N-gram table. If None, perform for whole Bible
#      - chapter (str, optional, default=None): name of chapter from
#          which to build N-gram table. If not None, assumes book has
#          been given (need to check and throw Exception if not
#          given). If None, perform for whole book.
#      - verse (str, optional, default=None): name of verse from which
#          to build N-gram table. If not None, assumes book and
#          chapter have been given (need to check and throw Exception
#          if not given). If None, perform for whole chapter.
#      - stopwords (list, optional, default=None): list of stop words to
#          ignore in building the n-gram table
#
#    returns: (dict) dictionary of n-gram to number of occurrences in
#       the given subset of the Bible



from functools import lru_cache
import gzip, csv
memoize = lru_cache(1)
@memoize
def read_bible():
    cols = ['book','chapter','verse','text']
    with gzip.open('csc211/hw/hw2/bible.tsv.gz','rt') as rfp:
        reader = csv.DictReader(rfp,cols,delimiter='\t')
        verses = list(reader)
    return verses

# Code goes below here





