# -*- coding: utf-8 -*-
import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['https://zh.wikipedia.org/']
    start_urls = ['http://https://zh.wikipedia.org//']

    print("111")
    def parse(self, response):
        pass
