import os
import emoji


def show(content):
    print(emoji.emojize(content))


def request(content):
    return input(emoji.emojize(content))


def clear():
    os.system("clear")
