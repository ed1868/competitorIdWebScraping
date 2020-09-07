import scrapy


class CompetitoridSpider(scrapy.Spider):
    name = 'competitorID'
    allowed_domains = ['https://www.hotels.com/']
    start_urls = ['http://https://www.hotels.com//']

    def parse(self, response):
        pass
