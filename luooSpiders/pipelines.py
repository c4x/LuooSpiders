# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import os

class LuoospidersPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        if not os.path.isdir(title):
            os.mkdir(title)
        print("download for %s :"%str(item['path']))
        urllib.request.urlretrieve(item['url'], item['path'])
        return item
