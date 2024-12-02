import json


fruits_list = json.load(open("data/fruits.json", "r", encoding="utf-8"))
jobs_list = json.load(open("data/jobs.json", "r", encoding="utf-8"))
objects_list = json.load(open("data/objects.json", "r", encoding="utf-8"))

words_list = [
    {"tip": "é uma fruta", "list": fruits_list},
    {"tip": "é um objeto", "list": objects_list},
    {"tip": "é uma profissão", "list": jobs_list},
]
