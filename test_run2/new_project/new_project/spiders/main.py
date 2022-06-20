import scrapy


class PostSpider(scrapy.Spider):
    name = "comments"
    start_urls = [
        'https://trickbd.com/apps-review/780034#comments'
    ]

    def parse(self, response):
        for post in response.css('ol.commentlist li'):
            yield {
                'title': post.css('.trickbd-comment-content::text').get()
            }

        # next_page = response.css('a.next').attrib['href']
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
