# ARY NEWS Latest Stories Web Crawler
# 26 AUG 2020

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as Soup

url = "https://arynews.tv/en/latest-news/"
output_folder = "D:/ary/"

user_agent_header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
request = Request(url, headers=user_agent_header)
response = urlopen(request)
source_code = response.read()
soup = Soup(source_code, 'html.parser')

articles = soup.find_all('article')
for article in articles:
    a_tag = article.find_all('a')[-1]
    story_title = a_tag.text.strip()
    story_link = a_tag.get('href')

    request = Request(story_link, headers=user_agent_header)
    source_code = urlopen(request).read()
    story_soup = Soup(source_code, 'html.parser')
    paragraphs = story_soup.article.find_all('p')

    file_name = str()
    for char in story_title:
        if(char.isalpha() or char.isdigit() or char.isspace()):
            file_name += char

    file = open(output_folder+file_name+".txt", 'w', encoding='utf-8')
    for p in paragraphs:
        file.write(p.text.strip()+"\n")
    file.close()