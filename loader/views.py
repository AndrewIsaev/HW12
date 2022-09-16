from flask import Blueprint, render_template, request
from functions import add_post
loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")

@loader_blueprint.route("/post")
def post_page():
    return render_template("post_form.html")

@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    data = request.form.get("content")
    picture = request.files.get("picture")
    filename = picture.filename
    picture.save(f"./uploads/images/{filename}")
    add_post(f"/uploads/images/{filename}", data)
    return render_template("post_uploaded.html", picture=picture.filename, data=data)


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    return
