from flask import Blueprint, render_template, request
from functions import search_posts

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

@main_blueprint.route("/")
def main_page():
    return render_template("index.html")

@main_blueprint.route("/search/")
def page_tag():
    data = request.args.get("s")
    posts = search_posts(data)
    return render_template("post_list.html", posts=posts, data=data)