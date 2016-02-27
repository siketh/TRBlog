#!flask/bin/python

import markdown

html = markdown.markdownFromFile('markdown_test.md', 'markdown_test.html')
