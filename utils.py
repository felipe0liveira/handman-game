import os
import time
import unicodedata
import emoji


def show(content):
    print(emoji.emojize(content))
def request(content):
    return input(emoji.emojize(content))


def wait(ms_delay):
    time.sleep(ms_delay/1000)


def clear():
    os.system("clear")


def normalize(word):
    return "".join(
        c
        for c in unicodedata.normalize("NFD", word.upper())
        if unicodedata.category(c) != "Mn"
    )