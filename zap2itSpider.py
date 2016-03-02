# -*- coding: utf-8 -*-
import scrapy


class zap2itSpider(scrapy.Spider):
    name = "zap2it"
    allowed_domains = ["zap2it.com"]
    start_urls = (
        'http://tvschedule.zap2it.com/tvlistings',
        'http://asoiaf.westeros.org/index.php?/forum/21-the-world-of-ice-and-fire/',
        'http://asoiaf.westeros.org/index.php?/forum/22-re-read-project/'
    )

    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            'votes': response.css('.question .vote-count-post::text').extract()[0],
            'body': response.css('.question .post-text').extract()[0],
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }
