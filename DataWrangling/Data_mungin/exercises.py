"""
Insterests:
pandas only gets tables from web sites
Web Scraping using request
HTML parser to read contents BeautifulSoup
"""

import pandas as pd
import json
"""
requests from a web site
"""
import requests
"""
Web text (HTML) parser
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
from bs4 import BeautifulSoup


"""
Reads the html and gets the tables from the web site
"""
fg500_html_df = pd.read_html('https://es.wikipedia.org/wiki/Fortune_Global_500')
"""
Result is a list of tables found as data frames
"""
list_2009 = fg500_html_df[0]
by_country = fg500_html_df[1]
by_city = fg500_html_df[2]

# print('list_2009')
# print(list_2009)
# print('by_country')
# print(by_country)
# print('by_city')
# print(by_city)

"""
Transform dataframe to a json to work as dictionary
"""
json_list_2009 = json.loads(list_2009.to_json(orient="records"))
# print(json_list_2009)

"""
Another way to scrap a web site is to use request
"""

response = requests.get('https://es.wikipedia.org/wiki/Fortune_Global_500')
'''
Prints response status
'''
# print(response.reason)
'''
prints response text (content is also useful)
'''
# print(response.text)

"""
Parses response text to a more html like soup
"""
soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())

"""
BeautifulSoup is a very helpful library for web scrapping. Examples:
"""
headlines = soup.select('span.mw-headline')
# print(headlines[0])
# print(headlines[0].name)
# print(headlines[0]['class'])
# print(headlines[0]['id'])
# print(headlines[0].text)
