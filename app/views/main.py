import logging
from datetime import date

from app import app, models, configuration
from flask import render_template, redirect, url_for, abort, request
from flask_login import login_user, logout_user, login_required

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
    if post_id is not None and page_index is not None:
        posts = query_by_id(post_id, page_index)

    # Otherwise query the database for all blog posts needed at this page index
    else:
        posts = query_for_posts(page_index)

    # If no posts returned, trigger a 404
    if posts is None:
        return abort(404)

    # Otherwise render the page requested
    else:
        log.info("Rendering /blog/" + str(page_index))
        return render_template('post.html', page='blog', posts=posts, year=year)


@app.route('/')
def home(page_index=1):
    log.info("Received request for home page")

    page = 'home'
    posts = None

    # Only query for the post tagged as 'home'
    posts = query_by_tag('home', page_index)

    # If the query isn't valid, trigger an internal server error
    if posts is None:
        return abort(404)

    # Otherwise render the page requested
    else:
        log.info("Rendering /")
        return render_template('post.html', page=page, posts=posts, year=year)


@app.route('/tags')
@app.route('/tags/<tag_name>')
@app.route('/tags/<tag_name>/<int:page_index>')
def tags(page_index=1, tag_name=None, post_id=None):
    log.info("Received request for /tags")

    posts = None

    # If the route is not supplied a post_id or tag_name, query for all tags and render the tags page
    if post_id is None and tag_name is None:
        all_tags = query_for_tags()

        # If no tags returned, trigger a 404
        if all_tags is None:
            return abort(404)

        # Otherwise render the page requested
        else:
            log.info("Rendering /tags")
            return render_template('tags.html', tags=all_tags, year=year)

    # If the route is supplied a post_id and not a tag_name, only query the database for a post with that id
    elif post_id is not None and tag_name is None:
        posts = query_by_id(post_id, page_index)

    # If the route is not supplied a post_id and is supplied a tag_name, query for all tags with the tag_name
    elif post_id is None and tag_name is not None:
        posts = query_by_tag(tag_name, page_index)

    # Otherwise, something unexpected happened
    else:
        return abort(404)

    # If no posts were returned, trigger a 404
    if posts is None:
        return abort(404)

    # Otherwise render the page requested
    else:
        log.info("Rendering /tags")
        return render_template('post.html', page='blog', posts=posts, year=year)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = query_for_user(email)

        if user is None:
            return abort(401)
        elif user.password == password:
            login_user(user)
            return redirect(url_for('admin.index'))
        else:
            return abort(401)
    else:
        return render_template('login.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('logout.html')


def query_by_id(post_id=None, page_index=None):
    if post_id is not None and page_index is not None:
        log.info("Querying for post with id '%d' and page index '%d'" % (post_id, page_index))
        results = models.Post.query.filter_by(id=post_id).paginate(page_index, configuration.POSTS_PER_PAGE, False)

        if query_successful(results.items):
            log.info("Query successful, returning %d results" % len(results.items))
            return results
        else:
            log.error("Query failed, returning None")
            return None

    if post_id is None:
        log.error("Post id was not initialized, could not query for post.")

    if page_index is None:
        log.error("Page index was not initialized, could not paginate query.")

    log.error("Query failed, returning None")
    return None


def query_for_posts(page_index=None):
    if page_index is not None:
        log.info("Querying for all posts on page %d" % page_index)
        results = models.Post.query \
            .filter(~models.Post.tags.any(models.Tag.name.in_(['home']))) \
            .order_by(models.Post.updated.desc()) \
            .paginate(page_index, configuration.POSTS_PER_PAGE, False)

        if query_successful(results.items):
            log.info("Query successful, returning %d results" % len(results.items))
            return results
        else:
            log.error("Query failed, returning None")
            return None

    if page_index is None:
        log.error("Page index was not initialized, could not paginate query.")

    log.error("Query failed, returning None")
    return None


def query_by_tag(tag_name=None, page_index=None):
    if tag_name is not None and page_index is not None:
        log.info("Querying for post with tag_name '%s' and page index '%d'" % (tag_name, page_index))
        results = models.Post.query \
            .filter(models.Post.tags.any(models.Tag.name.in_([tag_name]))) \
            .paginate(page_index, configuration.POSTS_PER_PAGE, False)

        if query_successful(results.items):
            log.info("Query successful, returning %d results" % len(results.items))
            return results
        else:
            log.error("Query failed, returning None")
            return None

    if tag_name is None:
        log.error("Tag name was not initialized, could not query for tag.")

    if page_index is None:
        log.error("Page index was not initialized, could not paginate query.")

    log.error("Query failed, returning None")
    return None


def query_for_tags():
    log.info("Querying for all tags")
    results = models.Tag.query.all()

    if query_successful(results):
        log.info("Query successful, returning %d results" % len(results))
        return results
    else:
        log.error("Query failed, returning None")
        return None


def query_for_user(email=None):
    if email is not None:
        log.info("Querying for user with email '%s'" % email)
        results = models.User.query.filter_by(email=email).all()

        if query_successful(results):
            log.info("Query successful, returning %d results" % len(results))
            return results[0]
        else:
            log.error("Query failed, returning None")
            return None

    if email is None:
        log.error("'email' was not initialized, could not query for User.")

    log.error("Query failed, returning None")
    return None


# Validate the pagination object returned from the database query
def query_successful(results=None):
    if results is None:
        log.error("Database query failed critically")
        return False

    elif len(results) == 0:
        log.error("No results were returned")
        return False

    return True
