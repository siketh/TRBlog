import logging
from datetime import date

from app import app, models
from config import POSTS_PER_PAGE
from flask import render_template, redirect, url_for

log = logging.getLogger(__name__)


@app.route('/home')
@app.route('/index')
def index():
    log.info("Rerouting to landing page")
    return redirect(url_for('home'))


@app.route('/blog')
@app.route('/blog/<int:page_index>')
@app.route('/blog/post/<int:post_id>')
def blog(page_index=1, post_id=None):
    log.info("Received request for /blog")

    year = date.today().year

    if post_id is not None:
        log.debug("Querying for blog post with id: " + str(post_id))
        posts = models.Post.query.filter_by(id=post_id) \
            .paginate(page_index, POSTS_PER_PAGE, False)
    else:
        log.debug("Querying for all blog posts")
        posts = models.Post.query \
            .filter(~models.Post.tags.any(models.Tag.name.in_(['about', 'contact']))) \
            .order_by(models.Post.updated.desc()) \
            .paginate(page_index, POSTS_PER_PAGE, False)

    log.info("Rendering /blog/" + str(page_index))
    return render_template('post.html', page='blog', posts=posts, year=year)


@app.route('/')
def home(page_index=1):
    log.info("Received request for /")

    posts = models.Post.query \
        .filter(models.Post.tags.any(models.Tag.name.in_(['about']))) \
        .paginate(page_index, POSTS_PER_PAGE, False)

    year = date.today().year

    log.info("Rendering /")
    return render_template('post.html', page='home', posts=posts, year=year)


@app.route('/contact')
def contact(page_index=1):
    log.info("Received request for /contact")

    posts = models.Post.query \
        .filter(models.Post.tags.any(models.Tag.name.in_(['contact']))) \
        .paginate(page_index, POSTS_PER_PAGE, False)

    year = date.today().year

    log.info("Rendering /contact")
    return render_template('post.html', page='contact', posts=posts, year=year)


@app.route('/tags')
@app.route('/tags/<tag_name>')
@app.route('/tags/<tag_name>/<int:page_index>')
def tags(page_index=1, tag_name=None, post_id=None):
    log.info("Received request for /tags")

    year = date.today().year

    if post_id is not None:
        posts = models.Post.query.filter_by(id=post_id) \
            .paginate(page_index, POSTS_PER_PAGE, False)

    elif tag_name is None:
        all_tags = models.Tag.query.all()

        return render_template('tags.html', tags=all_tags, year=year)

    else:
        posts = models.Post.query \
            .filter(models.Post.tags.any(models.Tag.name.in_([tag_name]))) \
            .paginate(page_index, POSTS_PER_PAGE, False)

    log.info("Rendering /tags")
    return render_template('post.html', page='blog', posts=posts, year=year)
