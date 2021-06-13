import codecs
import datetime
import time
from lxml import html

from engine.ProxyGenerator import ProxyGenerator
from .Database import Database


class Engine(Database,ProxyGenerator):

    def __init__(self):

        Database.__init__(self)
        ProxyGenerator.__init__(self)

        self.proxy = self.get_a_proxy()

        #---------
        self.data = []

        #--------


        # -----------------

        try:
            self.scrapper_name = self.scrapper_name + '.py'
        except:
            self.scrapper_name = self.__class__.__name__ + '.py'
            pass

        try:
            self.curr.execute(
                'select batch_id from tbl_crawler_details where scrapper_name = %s or parser_name = %s;',
                (self.scrapper_name, self.scrapper_name))
        except:
            pass

        self.batch_id = self.get_row_data()

        if self.batch_id == None:
            self.batch_id = 0

        # -----------------

        # --------------------------------------------
        urls_ls = None

        try:
            self.curr.execute(
                'select count(batch_id) from tbl_crawler_run_details where batch_id = %s and status_id = %s;',
                (self.batch_id, '0'))
        except:
            pass

        urls_count = self.get_row_data()

        self.urls_ls = (i for i in range(0, urls_count))

        if 'parser' in self.scrapper_name:
            self.parser_data = []
            counter = 1
            for i in (i for i in range(0, urls_count)):
                while True:
                    file_name = str().join([str(counter),'_',str(self.batch_id),'_',str(i+1),'.json'])
                    # f = codecs.open(file_name,'r',encoding='utf8')
                    self.parser_data.append(file_name)

                    counter = counter + 1
                    pass

            print('HI')
            pass

        # --------------------------------------------------

    def get_proxy(self):
        self.proxy = self.get_a_proxy()

    def get_scrapper_name(self):

        # fetch scrapper_name from batch_id
        d = self.conn.cursor
        scrapper_name_2 = None
        try:
            self.curr.execute('select scrapper_name from tbl_crawler_details where batch_id = %s', (self.batch_id,))
        except:
            return scrapper_name_2

        for scrapper_name_1 in self.curr:
            for scrapper_name_2 in scrapper_name_1:
                return scrapper_name_2

        return scrapper_name_2

    def get_a_input(self, url_id):

        url_id = url_id + 1

        try:
            self.curr.execute(
                'select url from tbl_crawler_run_details where batch_id = %s and status_id = %s and url_id = %s;',
                (self.batch_id, '0', url_id))
        except:
            return []

        url = self.get_row_data()

        return url

    def get_row_data(self):

        urls_count = None
        try:
            for scrapper_name_1 in self.curr:
                for scrapper_name_2 in scrapper_name_1:
                    urls_count = scrapper_name_2
        except:
            return 0
        return urls_count

    def get_lxml_object(self,request_obj):
        tree_obj = None

        try:
            tree_obj = html.fromstring(request_obj.content)
        except:
            print("Parse error")
            pass

        return tree_obj


    def __del__(self):

        unique_runid = str().join([datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')])
        for data_id,data in enumerate(self.data):

            self.cat_data = {}
            self.cat_data['dataid'] = data_id
            self.cat_data['pagedata'] = data

            self.cat_data['timestamp'] = unique_runid
            self.cat_data['urlid'] = self.url_id_2

            file_name = str().join(['D:\Collection\Scrape', "\\" , str(data_id+1) ,'_',str(self.batch_id), r'_', self.url_id_2,r'.json'])

            f = codecs.open(file_name, 'w', encoding='utf8')
            f.close()
            f = codecs.open(file_name, 'w', encoding='utf8')
            f.write(str(self.cat_data))
            f.close()

        # eval(codecs.open(r'D:\Collection\Scrape\3000_1_20210613232940.json').read())

        # print('Destroyed',self.data.get('Name'))
