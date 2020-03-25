from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
import scrapy


class MySpider(CrawlSpider):
    name = "drugInfo"
    allowed_domains = ["www.patientslikeme.com"]
    start_urls = ["https://www.patientslikeme.com/treatment_evaluations/browse?brand=false&id=2422&symptom_id=439"]
    rules = [Rule(LinkExtractor(allow=()), callback='parse_item', follow=True)]

    def parse_items (self,response):
        yield {
            'DrugName': response.xpath('//span[@itemprop="name"]/text()').extract(),
            'Evaluation': response.css('div#evaluations *::text').extract()
        }