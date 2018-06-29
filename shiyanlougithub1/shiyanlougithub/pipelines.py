# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from shiyanlougithub.models import Repository, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class ShiyanlougithubPipeline(object):
    def process_item(self, item, spider):
        '''
        list = item['update_time']
        item['update_time'] = datetime.strptime(list.split('T')[0]+' '+list.split('T')[1],'%Y-%m-%d %H:%M:%S')
        '''
        item['update_time'] = datetime.strptime(item['update_time'], '%Y-%m-%dT%H:%M:%S')
        item['commits'] = int(item['commits'])
        item['branches'] = int(item['branches'])
        item['releases'] = int(item['releases'])
        
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind = engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()


