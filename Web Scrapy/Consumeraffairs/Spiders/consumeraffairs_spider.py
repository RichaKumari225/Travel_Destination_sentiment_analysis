from scrapy import Spider, Request
from consumeraffairs.items import ConsumeraffairsItem


class ConsumeraffairsSpider(Spider):
    name = 'consumeraffairs_spider'
    allowed_urls = ['https://www.consumeraffairs.com/']
    start_urls = ['https://www.consumeraffairs.com/travel/travel-sites/#travel-site-features']

    # Custom headers to mimic a browser request
    custom_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Referer": "https://www.google.com/",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1"
    }

    def start_requests(self):
        """
        Initiate requests with custom headers to avoid detection.
        """
        for url in self.start_urls:
            yield Request(
                url=url,
                callback=self.parse,
                headers=self.custom_headers
            )

    def parse(self, response):
        """
        Parse the main page and extract review URLs.
        """
        if response.status == 403:
            self.logger.warning(f"Received 403 Forbidden on {response.url}")

        site_urls = response.xpath('//td[@class="brd-card__tit brd-card__td"]/a/@href').extract()

        for url in site_urls:
            full_url = response.urljoin(url)  # Ensure absolute URLs
            yield Request(
                url=full_url,
                callback=self.parse_review_page,
                headers=self.custom_headers
            )

    def parse_review_page(self, response):
        """
        Extract review data and handle pagination.
        """
        if response.status == 403:
            self.logger.warning(f"Received 403 Forbidden on {response.url}")

        # Extracting review data
        reviews = response.xpath('//div[@class="rvw js-rvw"]')
        site = response.xpath('//h1[@class="prf-hr-tl__cpy-nm  "]/text()').extract_first()

        for review in reviews:
            user = review.xpath('.//div[@class="rvw-aut__inf"]/strong[1]/text()').extract_first()
            rating = review.xpath('.//img[@class="stars-rtg stars-rtg--sm"]/@data-rating').extract_first()
            review_date = review.xpath('.//span[@class="ca-txt-cpt ca-txt--clr-gray"]/text()').extract_first()
            text = review.xpath('.//div[@class="rvw-bd ca-txt-bd-2"]/p[2]/text()').extract_first()

            verified_reviewer = review.xpath('.//div[@class="rvw-aut__inf"]/strong[2]/text()').extract_first(default="")
            verified_buyer = review.xpath('.//div[@class="rvw-aut__inf"]/strong[3]/text()').extract_first(default="")
            helpful = review.xpath('.//span[@class="rvw-foot__helpful-count js-helpful-count ca-txt--clr-gray"]/strong/text()').extract_first(default="")

            # Create and yield the item
            item = ConsumeraffairsItem()
            item['user'] = user
            item['rating'] = rating
            item['verified_reviewer'] = verified_reviewer
            item['verified_buyer'] = verified_buyer
            item['review_date'] = review_date
            item['text'] = text
            item['helpful'] = helpful
            item['site'] = site

            yield item

        # Follow pagination links
        next_page_url = response.xpath('.//a[@class="ca-a-md ca-a-uprcs ca-a-blk prf-pgr__nxt js-pager-next"]/@href').extract_first()
        
        if next_page_url:
            full_next_page = response.urljoin(next_page_url)
            self.logger.info(f"Following next page: {full_next_page}")
            
            yield Request(
                url=full_next_page,
                callback=self.parse_review_page,
                headers=self.custom_headers
            )
