# trevorroman.com

###My personal website, portfolio, and exercise in learning full-stack web development.

##DISCLAIMER:
This is an informal personal project I've been working on since 2015. It is not meant to be a general purpose tool for developers to fork and contribute to (though nothing is stopping you). I do welcome any suggestions or comments. My hope is that anyone looking to learn about web development with Python and Flask will find my project interesting and maybe even useful in their own endeavors.

## ABOUT:
TRBlog is a personal blogging web application stripped down to it's most essential elements. 

To me, these elements are:

 - User (Admin)
 - Posts
 - Tags 
 - Admin interface
 - RSS feed

My engineering philosophy is to begin with only what is absolutely necessary and work up the complexity from there. I have plans for future enhancements, but I believe the project currently has everything I require for my personal needs.

##GOALS:
The following were my goals when I first set out to build this project.

- Create a minimal blog and portfolio to showcase past and future projects, and to serve as a soapbox for my own thoughts; personal, and professional.
- Implement as much of my own code as possible.
- Leverage useful frameworks and modules when it makes sense.
- No established CMS, no bloat, use and implement only what is needed and nothing more.
- Learn what it takes to deploy a website from front-end to server configuration.
- Dig deep and learn as much as possible.

##CURRENT FEATURES:
- Minimal, elegant, and intuitive interface
- Administrative login for content management
- Tag-based search
- RSS feed
- Link to repository if a post features code

##FUTURE FEATURES:
 - Comments
 - Full text search
 - Custom admin interface
 - Generalize and release as a configurable minimal blogging application

##DEPENDENCIES:
- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Admin
- Flask-Security
- Flask-Login
- SQLAlchemy-Migrate
- Flask-Markdown
- Bootstrap 3

##CUSTOM BOOTSTRAP:
* Modifications:
  * @screen-xs = 550px
  * @grid-float-breakpoint = @screen-xs
* Github: https://gist.github.com/3328c139f430fa213d101806841b8c50
* Bootstrap Customization Page: https://getbootstrap.com/customize/?id=3328c139f430fa213d101806841b8c50

##LEARNING RESOURCES USED:
* [Flask Documentation](http://flask.pocoo.org/docs/0.11/)
* [Max Halford's Flask-Boilerplate](https://github.com/MaxHalford/Flask-Boilerplate)
* [Miguel Grinberg's Flask Mega Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [Flask-Security Documentation](https://pythonhosted.org/Flask-Security/)
* [Flask-Admin Documentation](https://flask-admin.readthedocs.io/en/latest/)
* [Flask-Login Documentation](https://flask-login.readthedocs.io/en/latest/)
* [Flask-Markdown Documentation](https://pythonhosted.org/Flask-Markdown/)
* [Digital Ocean VPS Setup Documentation](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04)
* [Digital Ocean Flask Deployment Documentation](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
* [SQLAlchemy Tutorial](http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html)

##LOCAL SETUP:
These are instructions for a local deployment of TRBlog on Ubuntu 16.

```sh
sudo apt-get install python3
sudo apt-get install python3-pip
sudp apt-get install git

git clone https://github.com/siketh/TRBlog.git
cd TRBlog
sudo python3 -m venv flask
. flask/bin/activate
pip3 install -r requirements.txt

./run.py
```

###Thank you for your interest in my project, I welcome any and all feedback or advice. 

###If you feel that I have misappropriated anything or not given due credit, please contact me immediately at troman360@gmail.com and I will correct the issue as soon as possible.
