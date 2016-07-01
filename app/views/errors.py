import logging
from datetime import date

from app import app
from flask import render_template

log = logging.getLogger(__name__)


@app.errorhandler(404)
def page_not_found(e):
    log.warning("Request returned error 404")

    year = date.today().year

    return render_template('404.html', posts=[], year=year), 404
