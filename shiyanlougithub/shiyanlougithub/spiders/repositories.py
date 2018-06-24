# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem

class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?tab=repositories&page={}'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self, response):
        for rep in response.css('li.col-12'):
            item = ShiyanlougithubItem({
                'name' : rep.xpath('.//h3/a/text()').extract_first().strip(),
                'update_time' : rep.xpath('.//relative-time/@datetime').re_first('(.+)Z')
                })
            yield item
