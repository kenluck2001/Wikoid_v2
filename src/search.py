import requests as req
import lxml
from lxml import html
from collections import defaultdict



WIKIPEDIA_BASE=u'https://en.wikipedia.org'

class Search(object):
    def __init__(self, url):
        self.r = req.get(url)
        self.tree = lxml.html.fromstring(self.r.content)
        self.elements = self.tree.findall('.//div/p') #get informative text
        self.graph = defaultdict(list) # <url>, [list of keywords]

    def get_all_keywords_with_links(self):
        urls = self.elements[0].findall('.//a') #get all url in first paragragh
        keyword_page_url = [ (el.text_content(),el.get('href')) for el in urls] #get urls in first paragraph.
        #remove citation links
        stopword = ('citation needed', '/wiki/Wikipedia:Citation_needed')
        if stopword in keyword_page_url:
            keyword_page_url.remove(stopword)

        return keyword_page_url

    def get_page(self):
        output = ''
        if self.elements:
            output = self.elements[0].text_content()
        return output

    def get_html(self, url):
        r = req.get(url)
        return r.content

    def create_graph(self):
        #get source_keyword from initial url
        url_string = self.r.url
        url_list = url_string.split('/')
        source_keyword = url_list[-1]
        #add the source to the last element
        graph = []

        for keyword, url in  self.get_all_keywords_with_links():    
            #get relationships between keywords   
            self.graph[url].append(keyword) 

        for keylist in  self.graph.values():
            output = source_keyword, keylist
            graph.append(output)

        total_list = []

        for keys, keylist in graph:
            for nextkey in keylist:
                output = keys, nextkey
                total_list.append(output)

        total_list  = list(set(total_list ))
        return total_list
