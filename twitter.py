#Prints my twitter bio at any given time.

from bs4 import BeautifulSoup
import urllib2

text = urllib2.urlopen("http://www.twitter.com/ryanstewartalex").read()
soup = BeautifulSoup(text, 'html.parser')
print(soup.p.text)