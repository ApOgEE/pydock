from bs4 import BeautifulSoup

print("This is APOGEEK Python Playground")

html = '''
<html><body>helo bro! my name is
<p>apogee</p></body></html>
'''

sup = BeautifulSoup(html, 'html.parser')

print("the html body tag: {}".format(sup.body))
print("the html p tag: {}".format(sup.p))

print("name: {}".format(sup.p.text))
