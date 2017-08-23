
import requests
from bs4 import BeautifulSoup
import re


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}

def page():
    url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.text,'lxml')
    soup_page = soup.find_all('table',class_="tagCol")
    url_all = []
    for each in soup_page:
        each_page = each.find_all('a')
        for i in each_page:
            tag = i.text
            url_all.append('https://book.douban.com/tag/'+tag)

    return url_all


def one_page(url_all):
    for each in url_all:
        response1 = requests.get(each,headers = headers)
        soup1 = BeautifulSoup(response1.text,'lxml')
        soup1_page = soup1.find('ul',class_="subject-list").find_all('h2',class_='')
        with open('url_page.txt','a+') as f:
            for i in soup1_page:
                url =i.a['href']
                response1 = requests.get(url, headers=headers)
                soup1 = BeautifulSoup(response1.text, 'lxml')
                soup1_title = soup1.find('span',property="v:itemreviewed").text
                soup1_content = soup1.find('div',class_="intro").text
                print(soup1_title)
                print(soup1_content)
                print(url)




'''
def loading_url():
    with open('url_page.txt','a') as f:
        response1 = requests.get(f.readline(),headers = headers)
        soup1 = BeautifulSoup(response1.text,'lxml')
'''



if __name__ == '__main__':
    one_page(page())