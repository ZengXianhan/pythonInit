# -*- coding: utf-8 -*-
import scrapy
import re

class WikiSpider(scrapy.Spider):
    base_url = 'https://zh.wikipedia.org/'
    name = 'wiki'
    allowed_domains = [base_url]
    start_urls = [base_url + 'wiki/Python']

    def parse(self, response):
        css_selector = response.css('.a :: attr(href)')
        title_selector = response.xpath('//*[@id="firstHeading"]/text()')
        href_selector = response.xpath("//@href")
        title = title_selector.extract()[0]
        hrefs = href_selector.extract()
        wiki_hrefs = set()
        for href in hrefs:
            wiki_href = re.match("/wiki/*", href)
            if(wiki_href is not None):
                wiki_hrefs.add(self.base_url + wiki_href.string)

        pass