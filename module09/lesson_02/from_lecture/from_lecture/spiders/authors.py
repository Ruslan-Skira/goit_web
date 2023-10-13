import scrapy
from scrapy.http import Request, Response
from scrapy.utils.reactor import install_reactor


class AuthorsSpider(scrapy.Spider):
    # install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    name = "authors"  # robots name
    allowed_domains = ["quotes.toscrape.com"]  # no url in this domain not allowed
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        """Callback generator function """
        for quote in response.xpath("/html//div[@class='quote']"):
            yield {
                "keywords": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").extract(),
                "quote": quote.xpath("span[@class='text']/text()").get()
            }
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)
