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
            item = ShiyanlougithubItem()
            item['name'] = rep.xpath('.//h3/a/text()').extract_first().strip()
            item['update_time'] = rep.xpath('.//relative-time/@datetime').re_first('(.+)Z')
            course_url = response.urljoin(rep.xpath('@href').extract_first())
            request = scrapy.Request(url=course_url, callback=self.parse_course)
            request.meta['item'] = item
            yield request

    def parse_course(self,response):
        item = response.meta['item']
        item['commits'] = response.xpath('(//span[@class="num text-emphasized"])[1]/text()').extract_first(default='111111').strip()
        item['branches'] = response.xpath('(//span[@class="num text-emphasized"])[2]/text()').extract_first(default='111111').strip()
        item['releases'] = response.xpath('(//span[@class="num text-emphasized"])[3]/text()').extract_first(default='1111111').strip()
        yield item
