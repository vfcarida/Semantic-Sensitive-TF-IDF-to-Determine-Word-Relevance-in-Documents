# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['http://quotes.toscrape.com/random']
    start_urls = ['http://http://quotes.toscrape.com/random/']

    def parse(self, response):
        pass
