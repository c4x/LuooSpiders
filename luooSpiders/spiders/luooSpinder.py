# -*- coding: utf-8 -*-  
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from luooSpiders.items import luooSpidersItem
import os
import urllib    


#curl -o 阿卡贝拉/01. Ciao, Bella, Ciao [Italy].mp3 http://luoo.waasaa.com/low/luoo/radio685/01.mp3
class luooSpider(BaseSpider):
    name = "luoo"
    allowed_domains = ["luoo.net"]
    start_urls = [
        "http://www.luoo.net/music/700",
    ]

    # def callbackfunc(blocknum, blocksize, totalsize):
    #     percent = 100 * blocknum * blocksize / totalsize
    #     if percent >= 100:
    #         percent = 100
    #         print "%s%%"% str(percent)

    def parse(self, response):
        item = luooSpidersItem()
        special = response.url.split("/")[-1]
        container = Selector(response).xpath('/html/body/div[@class="container ct-sm"]')
        item['title'] = container.xpath('h1[@class="vol-name"]/\
            span[@class="vol-title"]/text()').extract()
        item['tracks'] = container.xpath('div[@class="vol-tracklist"]/ul/li[@class="track-item rounded"]/\
            div[@class="track-wrapper clearfix"]/a[@class="trackname btn-play"]/text()').extract()
        if not os.path.isdir(item['title'][0].encode('utf8')) :
            os.mkdir(item['title'][0].encode('utf8'))
            pass
        for index,track in enumerate(item['tracks']):
            mp3_url = "http://luoo.waasaa.com/low/luoo/radio%s/%s.mp3"%(special,str(index+1).zfill(2))
            path = item['title'][0].encode('utf8')+'/'+track.encode('utf8')[3:]+'.mp3'
            urllib.urlretrieve(mp3_url, path)
            # mp3 = open(path,'w')
            # mp3.write(urllib.urlopen(mp3_url).read())
            # mp3.close()
            # print track.encode('utf8')[3:]
            # os.system(cmd)
            pass

    