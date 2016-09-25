#!/flask/bin/python

import sys, os, logging

os.environ['ENV'] = 'PROD'
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/TRBlog')
os.chdir('/var/www/TRBlog')

from run import app as application
