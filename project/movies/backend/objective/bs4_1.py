#pip install fake-useragent


from bs4 import BeautifulSoup
import requests
 
url="http://www.iana.org/domains/example"
url="http://www.htmlandcssbook.com/code-samples/chapter-04/example.html"
print(url) 
# Getting the webpage, creating a Response object.
response = requests.get(url)
 
# Extracting the source code of the page.
data = response.text
print("printing data") 
# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'html.parser')
 
# Extracting all the <a> tags into a list.
tags = soup.find_all('a')
 
# Extracting URLs from the attribute href in the <a> tags.
for tag in tags:
    print(tag.get('href'))