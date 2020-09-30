# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy import settings

class Test1Pipeline:
    def process_item(self, item, spider):
        host = '127.0.0.1'
        user = 'root'
        psd =  '123456'
        db = 'spiders'
        c = 'utf8'
        port = 3306
        # 数据库连接
        con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)
        # 数据库游标
        cue = con.cursor()
      # sql="insert into gamerank (rank,g_name,g_type,g_status,g_hot) values(%s,%s,%s,%s,%s)" % (item['rank'],item['game'],item['type'],item['status'],item['hot'])
        try:
            cue.execute("insert into zuo(title,author,reply,link) values(%s,%s,%s,%s",
                        [item['title'],item['author'],item['reply'] ,item['link']])
        except Exception as e:
            print('Insert error:', e)
            con.rollback()
        else:
            con.commit()
        con.close()
        return item
        return item
