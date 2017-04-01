# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from luooSpiders.items import luooSpidersItem
from scrapy.http import Request

class luooSpider(BaseSpider):
    name = "luoo"
    allowed_domains = ["luoo.net"]
    start_urls = ['http://www.luoo.net/tag/?p=1']

    def __init__(self, page=1, *args, **kwargs):
        super(luooSpider, self).__init__(*args, **kwargs)
        if page:
            self.page = int(page)

    def parse(self, response):
        print("current url:%s"%response.url)
        periodicals = response.xpath('//a[@class="cover-wrapper"]/@href').extract()
        last_page = int(max(response.xpath('//a[@class="page"]/text()').extract()))
        for periodical in periodicals:
            print("start periodical:%s"%periodical)
            yield Request(periodical, callback=self.parse_item)
        if self.page > last_page:
            self.page = last_page
        current = 1
        while current <= self.page:
            current += 1
            yield Request('http://www.luoo.net/tag/?p=%s' % current, callback=self.parse)

    def parse_item(self, response):
        special = response.url.split("/")[-1]
        container = Selector(response).xpath('/html/body/div[@class="container ct-sm"]')
        items = []
        titles = container.xpath('h1[@class="vol-name"]/\
            span[@class="vol-title"]/text()').extract()
        tracks = container.xpath('div[@class="vol-tracklist"]/ul/li[@class="track-item rounded"]/\
            div[@class="track-wrapper clearfix"]/a[@class="trackname btn-play"]/text()').extract()
        for index,track in enumerate(tracks):
            item = luooSpidersItem()
            mp3_url = "http://luoo.waasaa.com/low/luoo/radio%s/%s.mp3"%(special,str(index+1).zfill(2))
            path = titles[0]+'/'+track[3:]+'.mp3'
            item['title'] = titles[0]
            item['url'] = mp3_url
            item['path'] = path
            items.append(item)
        return items