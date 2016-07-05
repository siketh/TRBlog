import logging
from datetime import date

from app import app, models
from app.views import errors
from config import POSTS_PER_PAGE
from flask import render_template, redirect, url_for

log = logging.getLogger(__name__)
year = date.today().year


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

    posts = None

    # If the route is supplied a post_id, only query the database for a post with that id
    if post_id is not None:
        log.debug("Querying for blog post with id: " + str(post_id))
        posts = models.Post.query.filter_by(id=post_id) \
            .paginate(page_index, POSTS_PER_PAGE, False)

    # Otherwise query the database for all blog posts, except the one tagged as 'home'
    else:
        log.debug("Querying for all blog posts")
        posts = models.Post.query \
            .filter(~models.Post.tags.any(models.Tag.name.in_(['home']))) \
            .order_by(models.Post.updated.desc()) \
            .paginate(page_index, POSTS_PER_PAGE, False)

    # If the query isn't valid, trigger an internal server error
    if not valid_query(results=posts.items):
        return errors.error_500()

    # Otherwise render the page requested
    else:
        log.debug("Returned [" + str(len(posts.items)) + "] posts")
        log.info("Rendering /blog/" + str(page_index))
        return render_template('post.html', page='blog', posts=posts, year=year)


@app.route('/')
def home(page_index=1):
    log.info("Received request for /")

    posts = None

    # Only query for the post tagged as 'home'
    log.debug("Querying for the home page post")
    posts = models.Post.query \
        .filter(models.Post.tags.any(models.Tag.name.in_(['home']))) \
        .paginate(page_index, POSTS_PER_PAGE, False)

    # If the query isn't valid, trigger an internal server error
    if not valid_query(results=posts.items):
        return errors.error_500()

    # Otherwise render the page requested
    else:
        log.debug("Returned [" + str(len(posts.items)) + "] posts")
        log.info("Rendering /")
        return render_template('post.html', page='home', posts=posts, year=year)


@app.route('/tags')
@app.route('/tags/<tag_name>')
@app.route('/tags/<tag_name>/<int:page_index>')
def tags(page_index=1, tag_name=None, post_id=None):
    log.info("Received request for /tags")

    posts = None

    # If the route is not supplied a post_id or tag_name, query for all tags and render the tags page
    if post_id is None and tag_name is None:
        all_tags = models.Tag.query.all()

        # If the query isn't valid, trigger an internal server error
        if not valid_query(results=all_tags):
            return errors.error_500()

        # Otherwise render the page requested
        else:
            log.debug("Returned [" + str(len(all_tags)) + "] posts")
            log.info("Rendering /tags")
            return render_template('tags.html', tags=all_tags, year=year)

    # If the route is supplied a post_id and not a tag_name, only query the database for a post with that id
    elif post_id is not None and tag_name is None:
        posts = models.Post.query.filter_by(id=post_id) \
            .paginate(page_index, POSTS_PER_PAGE, False)

    # If the route is not supplied a post_id and is supplied a tag_name, query for all tags with the tag_name
    elif post_id is None and tag_name is not None:
        posts = models.Post.query \
            .filter(models.Post.tags.any(models.Tag.name.in_([tag_name]))) \
            .paginate(page_index, POSTS_PER_PAGE, False)

    # Otherwise, something unexpected happened
    else:
        return errors.error_500()

    # If the query isn't valid, trigger an internal server error
    if not valid_query(results=posts.items):
        return errors.error_500()

    # Otherwise render the page requested
    else:
        log.debug("Returned [" + str(len(posts.items)) + "] posts")
        log.info("Rendering /tags")
        return render_template('post.html', page='blog', posts=posts, year=year)


# Validate the pagination object returned from the database query
def valid_query(results=None):
    if results is None:
        log.error("Database query failed critically")
        return False

    elif len(results) == 0:
        log.error("No results were returned")
        return False

    return True
