from datetime import date

from app import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(e):
    year = date.today().year

    return render_template('404.html', posts=[], year=year), 404
