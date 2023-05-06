from flask import Blueprint, render_template

from blog.models import Author

author = Blueprint('author', __name__, url_prefix='/authors', static_folder='../static')


@author.route('/')
def author_list():
    authors = Author.query.all()
    return render_template(
        'authors/list.html',
        authors=authors,
    )