import scrapy


class QuotesSpider(scrapy.Spider):
    name = "crawler"
    crawled_sites = []

    def start_requests(self):
        urls = [
            'http://people.f4.htw-berlin.de/~zhangg/pages/teaching/pages/d01.html',
            'http://people.f4.htw-berlin.de/~zhangg/pages/teaching/pages/d06.html',
            'http://people.f4.htw-berlin.de/~zhangg/pages/teaching/pages/d08.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")
        page = page[len(page) - 1]
        self.crawled_sites.append(page)
        filename = '%s' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        for href in response.css('a::attr(href)'):
            if href not in self.crawled_sites:
                yield response.follow(href, self.parse)
