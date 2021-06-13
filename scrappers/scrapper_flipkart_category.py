import time
import requests
import codecs
from engine.Engine import Engine


class scrapper_flipkart_category(Engine):

    def __init__(self):
        super().__init__()
        pass

    def get_category_crawl(self):
        url = self.url
        headers = {}
        r = requests.get(url,headers=headers,proxies=self.get_proxy())
        tree = self.get_lxml_object(r)
        try:
            page_count = tree.xpath('//div[@class="_2MImiq"]/span/text()')[-1].split(' ')[-1]
            page_count = int(page_count)
        except:
            page_count = 0
            pass

        self.data.append(r.content)

        for newr in list(range(2,page_count+1)):
            new_url = url.replace('page=1','page='+str(newr))
            data = None
            try:
                r = requests.get(new_url, headers=headers, proxies=self.get_proxy())
                data = r.content
            except:
                pass

            self.data.append(data)

        print('Hi Scrapper')
