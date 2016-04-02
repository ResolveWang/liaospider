from bs4 import BeautifulSoup
import requests

#js教程的根连接  http://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000
def get_title_link(root_url):
    hea = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko","Accept-Language":"zh-CN,zh;q=0.8"}
    original_url = 'http://www.liaoxuefeng.com'
    html = requests.get(root_url,headers=hea).text
    soup = BeautifulSoup(html,'html.parser')
    links = []
    all = soup.find('div',{'class':'x-sidebar-left-content'}).find('ul',{'style':'margin-right:-15px;'}).find_all('li')
    for link_title in all:
        link = original_url+link_title.a['href']
        links.append(link)
    return links





