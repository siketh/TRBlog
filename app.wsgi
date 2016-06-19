import sys, os, logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/TRBlog')
os.chdir('/var/www/TRBlog')
from run import app
application = app