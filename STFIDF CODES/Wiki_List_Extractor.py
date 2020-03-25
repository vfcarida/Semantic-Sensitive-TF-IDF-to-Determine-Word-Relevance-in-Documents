from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
import scrapy


class QuotesSpider(CrawlSpider):
    name = "drugInfoCrw"
    allowed_domains = ["treato.com"]
    start_urls = ["https://treato.com/drugs"]
    rules = [Rule(LinkExtractor(allow=()), callback='parse_item', follow=True)]

    def parse_item(self, response):

        yield {'separator': '---------------------'}
        yield {
            'Title': response.xpath('//h1[@class="firstHeading"]//text()').extract(),
             'Lists': response.xpath('//span[@class="toctext"]//text()').extract(),
           }