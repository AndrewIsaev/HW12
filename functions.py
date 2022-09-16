import json

PATH = "posts.json"

def load_json():
    with open(PATH, encoding="utf-8") as file:
        return json.load(file)

def search_posts(search_key:str):
    posts_list = []
    for post in load_json():
        if search_key.lower() in post["content"].lower():
            posts_list.append(post)
    return posts_list


print(search_posts("пока все на работе"))