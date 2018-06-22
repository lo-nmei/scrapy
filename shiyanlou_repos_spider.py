# -*- coding=utf-8 -*-

import scrapy

class Shiyanlou_Repos_Spider(scrapy.Spider):

    name = 'shiyanlou-repos'
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?tab=repositories&page={}'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        for rep in response.css('li.col-12 d-block width-full py-4 border-bottom public source ::text'):
            yield {
                'name' : rep.xpath('.//h3/a/text()').extract_first(),
                'update_time' : rep.xpath('.//relative-time/@datetime').extract_first()
                }
