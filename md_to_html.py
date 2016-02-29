#!flask/bin/python

import markdown
import glob
import os

md_path = 'posts/md/'
html_path = 'posts/html/'

md_posts = glob.glob(os.path.join(md_path, '*.md'))

for md_post in md_posts:
	html_post = md_post.replace(md_path, html_path).replace('.md', '.html')
	
	print("Markdown File: " + md_post)
	print("HTML File: " + html_post)
	
	markdown.markdownFromFile(md_post, html_post)

	post = open(md_post, 'r').readlines()
	for line in post:
		if '#' not in line:
			print(line)

