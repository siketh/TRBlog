import logging
from datetime import date

from app import app
from flask import render_template

log = logging.getLogger(__name__)
year = date.today().year


@app.errorhandler(404)
def page_not_found(e):
    log.warning("Request returned error 404")
    return render_template('404.html', posts=[], year=year), 404


@app.errorhandler(500)
def internal_server_error(e):
    log.error("Request returned error 500")
    return render_template('500.html', posts=[], year=year), 500
