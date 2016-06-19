from urllib.parse import urljoin

from app import app, models
from config import BASE_URL
from flask import request
from werkzeug.contrib.atom import AtomFeed


@app.route('/recent')
def recent_feed():
    feed = AtomFeed('Recent Articles', feed_url=request.url, url=request.url_root)

    posts = models.Post.query \
        .filter(~models.Post.tags.any(models.Tag.name.in_(['about', 'contact']))) \
        .order_by(models.Post.updated.desc()) \
        .limit(15) \
        .all()

    base_url = BASE_URL + '/blog/post/'
    counter = 1

    for post in posts:
        url = base_url + str(counter)
        counter += 1

        feed.add(post.title, post.body,
                 content_type='html',
                 author=post.author.full_name,
                 url=make_external(url),
                 updated=post.updated,
                 published=post.created)

    return feed.get_response()


def make_external(url):
    return urljoin(request.url_root, url)
