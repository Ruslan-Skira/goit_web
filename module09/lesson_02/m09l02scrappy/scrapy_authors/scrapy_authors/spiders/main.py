import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = 'authors'
    custom_settings = {"FEED_FORMAT": "csv", "FEED_URI": "result_main.csv"}
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    counter = 0

    def parse(self, response):

        for quote in response.xpath("/html//div[@class='quote']"):
            self.counter+=1
            yield {
                "id": self.counter,
                "keywords": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").extract(),
                "quote": quote.xpath("span[@class='text']/text()").get()
            }
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)

# run spider
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()

