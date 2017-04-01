# -*- coding: utf-8 -*-

# Scrapy settings for luooSpiders project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'luooSpiders'

SPIDER_MODULES = ['luooSpiders.spiders',]
NEWSPIDER_MODULE = 'luooSpiders.spiders'
ITEM_PIPELINES={'luooSpiders.pipelines.LuoospidersPipeline':100,}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'luooSpiders (+http://www.yourdomain.com)'
