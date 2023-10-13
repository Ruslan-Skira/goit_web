import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]


    def parse(self, response):  # callback
        """
        response: Request

        """

        # for quote in response.xpath("/html//div[@class='quote']"):
        #     keywords = quote.xpath("div[@class='tags']/a/text()").extract()
        #     yield keywords

        for quote in response.xpath("/html//div[@class='quote']"):

            yield {
                "keywords": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").extract(),
                "quote": quote.xpath("span[@class='text']/text()").get()
                    }
        next_link =response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0]+ next_link)

    # def my_pass(arg):
    #     t = type(arg)
    #     if t == 'str':
    #         return t
    #     if t == 'scrapy.Request':
    #         return my_pass(t)
