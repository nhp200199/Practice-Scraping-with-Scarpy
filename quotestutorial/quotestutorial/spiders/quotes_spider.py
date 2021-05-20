import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        all_div_quotes = response.css(".quote")

        for quote in all_div_quotes:
            title = quote.css(".text::text").extract()
            author = quote.css(".author::text").extract()
            tags = quote.css(".tag::text").extract()
            yield{
                'title':title,
                'author':author,
                'tags':tags
            }
