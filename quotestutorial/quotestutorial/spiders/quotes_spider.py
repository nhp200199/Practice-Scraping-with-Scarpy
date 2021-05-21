from ..items import QuotestutorialItem
import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    page_number = 2

    def parse(self, response):
        all_div_quotes = response.css(".quote")

        item = QuotestutorialItem()

        for quote in all_div_quotes:
            title = quote.css(".text::text").extract()
            author = quote.css(".author::text").extract()
            tags = quote.css(".tag::text").extract()

            item['title'] = title
            item['author'] = author
            item['tags'] = tags
            yield item
        
        next_page = f'http://quotes.toscrape.com/page/{QuoteSpider.page_number}/'

        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
