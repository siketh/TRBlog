# trevorroman.com
###My personal website, portfolio, and exercise in learning web development.

##DISCLAIMER:
This project should be viewed as a bit of a playground. I have a lot to learn about Flask and web development in general.
I'm still learning what constitutes a good project setup, what to check in, what not to check in, etc. This project is 
not live in any form other than a very basic landing page on my domain.

##GOALS:
1. Create a minimal blog and portfolio webapp to showcase past and puture projects, and to serve as a soapbox for my own 
thoughts; persoal, and professional.
2. Implement as much of my own code as possible.
3. Leverage useful frameworks and modules when it makes sense.
4. No CMS, no bloat, use and implement only what is needed and nothing more.
5. Dig deep and learn as much as possible.

##PLANNED FEATURES:
1. Minimal, elegant, and intiutive interface.
2. Support for comments on blog posts. Commenters will log in with Google account, or possibly other services.
3. RSS feed
4. Full text search
5. Articles featuring code can be forked directly from the post
6. Simple and secure admin page

##DEPENDENCIES:
* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-Admin
* Flask-Markdown
* Bootstrap 3

##SETUP (LINUX):

Setup is still a work in progress:

1. Install flask virtual environment and dependencies.
```
python3 -m venv flask
flask/bin/pip install flask
flask/bin/pip install flask-sqlalchemy
flask/bin/pip install flask-admin
flask/bin/pip install flask-markdown
./run.py
```
2. Setup DB...
3. Download Custom Bootstrap
  * Modifications:
   ** @screen-xs = 550px
   ** @grid-float-breakpoint = @screen-xs
  * Github: https://gist.github.com/3328c139f430fa213d101806841b8c50
  * Bootstrap Customization Page: https://getbootstrap.com/customize/?id=3328c139f430fa213d101806841b8c50
4. Unzip Bootstrap download into app/static

###Thank you for your interest, I welcome any and all feedback or advice.
