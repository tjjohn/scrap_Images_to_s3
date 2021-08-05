import scrapy
#pip install image

class CoverSpider(scrapy.Spider):
    name = 'cover'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        images = list()

        for img in response.css('.thumbnail::attr(src)').getall():
            images.append(response.urljoin(img))
        print("type-===============================",type(images))
        yield {
            'image_urls': images
        }
