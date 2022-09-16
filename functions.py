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


def add_post(picture, content):
    all_posts = load_json()
    a = {"pic": picture, "content": content}
    all_posts.append(a)
    with open(PATH, "w", encoding="utf-8") as file:
        json.dump(all_posts, file, ensure_ascii=False)


