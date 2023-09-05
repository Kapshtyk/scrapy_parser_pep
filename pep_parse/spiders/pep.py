import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        anchors = response.css("table.pep-zero-table").xpath(".//a")
        for anchor in anchors:
            href = anchor.xpath("./@href").get()
            if href:
                url = response.urljoin(href)
                yield scrapy.Request(url, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css("h1.page-title::text").get()
        data = {
            "name": title.split("–")[1],
            "number": title.split()[1],
            "status": response.xpath(
                '//dt[text()="Status"]/following-sibling::dd/abbr/text()'
            )
            .get()
            .strip(),
        }
        yield PepParseItem(data)
