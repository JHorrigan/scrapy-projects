import scrapy

class QuotesSpider(scrapy.Spider):
	
	# Spider identifier must be unique within a project
	name = "quotes"

	# Must return an iterable of requests (list or generator)
	# Subsequent requests will be generated from these
	'''def start_requests(self):
		urls = [
			'http://quotes.toscrape.com/page/1/',
			'http://quotes.toscrape.com/page/2/',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)'''

	# Or simply define a start_urls class attribute. Default implementation
	# of start_requests will be used and parse() called on response
	start_urls = [
		'http://quotes.toscrape.com/page/1/',
		'http://quotes.toscrape.com/page/2/',
	]

	# Handle response download. Response is an instance of Text Response
	# which holds the page content and has helpful methods to handle it
	def parse(self, response):
		# parse() usually parses response, extract scraped data as dicts,
		# find new urls to follow and create new requests
		page = response.url.split("/")[-2]
		filename = 'quotes-%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)