---
marp: true
---


# Introduction to BeautifulSoup

BeautifulSoup is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files. It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.


---


## Installation

You can install BeautifulSoup by using pip:

```python
pip install beautifulsoup4
```


---


## Basic Usage

```python
import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get("http://www.example.com")
print(r.content)

# Use the 'html.parser' to parse the page
soup = BeautifulSoup(r.content, 'html.parser')

# Print the parsed data of html
print(soup.prettify())
```

In this example, we first make a request to the website and then parse the HTML content of the page using BeautifulSoup. The `prettify()` function is used to display the parsed HTML content in a more readable format.


---


## Extracting Data

You can navigate and search the parse tree using various methods provided by BeautifulSoup. For example, you can find all instances of a tag at once:

```python
for link in soup.find_all('a'):
    print(link.get('href'))
```

This will print all the URLs found within `<a>` tags in the HTML content.

BeautifulSoup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree, making it a powerful tool for web scraping.

---

BeautifulSoup provides several methods for navigating and searching the parse tree:

1. **Navigating the tree**: BeautifulSoup provides several ways to navigate the parse tree, including `.contents` to get a list of a tag's children, `.descendants` to iterate over all of a tag's children recursively, `.string` to get a tag's text, and `.parent` and `.parents` to navigate up the tree.


---


2. **Searching the tree**: BeautifulSoup provides methods like `.find_all()` and `.find()` to search the parse tree. You can pass in a string to match against a tag's name, a list of strings to match against any of several tag names, a function to filter tags that match certain criteria, and more.


---


3. **CSS Selectors**: BeautifulSoup also supports searching the tree with CSS selectors using the `.select()` method. For example, `soup.select('div.content')` will return all `div` tags with the class `content`.


---


4. **Sibling and Next/Previous element**: BeautifulSoup provides `.next_sibling`, `.previous_sibling`, `.next_siblings`, `.previous_siblings` to navigate between page elements that are on the same level of the parse tree (siblings), and `.next_element`, `.previous_element`, `.next_elements`, `.previous_elements` to navigate to next or previous elements in the tree.


---


5. **Searching by Attributes**: You can search for tags that have certain attributes, like `soup.find_all('a', attrs={'class': 'sister'})` to find all `a` tags with the class `sister`.
