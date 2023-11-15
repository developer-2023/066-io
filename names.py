# docs.python.org/3/library/functions.html#open
# 7:21:00 Harvard CS50’s Introduction to Programming with Python – Full University Course

with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())