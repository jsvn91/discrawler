from .Database import Database

class Engine(Database):

    def __init__(self):

        super().__init__()

        #-----------------

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

        #-----------------

        #--------------------------------------------
        urls_ls = None

        try:
            self.curr.execute(
                'select count(batch_id) from tbl_crawler_run_details where batch_id = %s and status_id = %s;',
                (self.batch_id, '0'))
        except:
            pass

        urls_count = self.get_row_data()

        self.urls_ls = (i for i in range(0, urls_count))
        #--------------------------------------------------

    def get_scrapper_name(self):

        # fetch scrapper_name from batch_id
        d = self.conn.cursor
        scrapper_name_2 = None
        try:
            self.curr.execute('select scrapper_name from tbl_crawler_details where batch_id = %s',(self.batch_id,))
        except:
            return scrapper_name_2

        for scrapper_name_1 in self.curr:
            for scrapper_name_2 in scrapper_name_1:
                return scrapper_name_2

        return scrapper_name_2

    def get_a_input(self,url_id):


        # url_id = None

        # try:
        #     url_id = next(self.urls_ls) + 1
        # except:
        #     return url_id

        url_id = url_id + 1

        try:
            self.curr.execute('select url from tbl_crawler_run_details where batch_id = %s and status_id = %s and url_id = %s;',
                              (self.batch_id, '0',url_id))
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
        return  urls_count
