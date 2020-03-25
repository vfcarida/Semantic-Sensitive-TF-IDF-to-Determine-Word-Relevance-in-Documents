from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# from scrapy.selector import HtmlXPathSelector
# import scrapy


class QuotesSpider(CrawlSpider):
    name = "drugInfoCrw"
    allowed_domains = ["sciencedirect.com"]
    start_urls = ["https://www.sciencedirect.com/science/article/pii/S0167739X18318144"]
    rules = [Rule(LinkExtractor(allow=()), callback='parse_item', follow=True)]

    def parse_item(self, response):
        yield {'separator': '---------------------'}
        yield {'Keywords': response.xpath('//div[@class="keyword"]//text()').extract()}
        yield {'Title': response.xpath('//span[@class="title-text"]//text()').extract()}
        yield {'Introduction': response.xpath('//section[@id="sec1"]//text()').extract()}

######### For Treato
# class QuotesSpider(CrawlSpider):
#     name = "drugInfoCrw"
#     allowed_domains = ["treato.com"]
#     start_urls = ["https://treato.com/drugs"]
#     rules = [Rule(LinkExtractor(allow=()), callback='parse_item', follow=True)]
#
#     def parse_item(self, response):
#
#         yield {'separator': '---------------------'}
#         yield {'Description': response.xpath('//div[@class="column large-12 medium-12 small-12 common-infos"]//text()').extract()}
#         yield {'Title': response.xpath('//h2[@class="posts-title"]//text()').extract() + response.xpath(
#                         '//h2[@class="posts-title"]//text()').extract()
#                          + response.xpath('//h1[@class="posts-title columns large-12 medium-11 small-11 no-padding"]//text()').extract()
#                          + response.xpath('//h1[@class="posts-title"]//text()').extract()
#                          + response.xpath('//span[@itemprop="name"]/text()').extract() + response.xpath('//h1[@class="concept-title"]/descendant-or-self::*/text()').extract()
#                }
#         #for post in response.xpath('//div[@class="collapsed-expand-parent"]'):
#         for post in response.xpath('//div[@class="column post-content"]/descendant-or-self::*/text()').extract():
#             yield {
#                 #'Text': post.xpath('//div[@class="column post-content"]/descendant-or-self::*/text()').extract()
#                 'Text': post,
#             }