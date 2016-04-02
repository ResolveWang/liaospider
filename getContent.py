import requests
from bs4 import BeautifulSoup


def get_content(link):
    hea = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko","Accept-Language":"zh-CN,zh;q=0.8"}
    html = requests.get(link,headers=hea).text
    soup = BeautifulSoup(html,'html.parser')
    title = soup.find('div',{'class':'x-content'}).h4.get_text()
    content = soup.find('div',{'class':'x-wiki-content'}).get_text()
    return (title,content)

def store_content(theme,link):
    title = get_content(link)[0]
    # 处理特殊编码
    content = get_content(link)[1].replace(u'\xa0',u'')+'\n'
    path = theme+'.txt'
    with open(path,'a') as f:
        f.write(title)
        f.write(content)
