import liaospider.getAllLinks as ga
import liaospider.getContent as gc

if __name__ == '__main__':
    js_root_url = 'http://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000'
    js_links = ga.get_title_link(js_root_url)
    theme = 'js'
    for link in js_links:
        if link == 'http://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/00143564690172894383ccd7ab64669b4971f4b03fa342d000':
            gc.store_content(theme,link)
    exit('结束')
    python_root_url = 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
    python_links = ga.get_title_link(python_root_url)
    for link in python_links:
        gc.store_content(link)

    git_root_url = 'http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000'
    git_links = ga.get_title_link(git_root_url)
    for link in git_links:
        gc.store_content(link)