# Use the Request library
import requests
# Set the target webpage
url = "https://brickset.com/sets/year-1999"
r = requests.get(url)
# This will get the full page
print(r.text)
# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
# This will modify the headers user-agent
headers = { 'User-Agent' : "Mobile" }
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
print("**********")
# This will get the status code
print("Status code:")
print("\t *", r.status_code)

#use scrapy web crawler search for image links in the website
import scrapy

class NewSpider(scrapy.Spider):

 name = "new_spider"

 start_urls = ['https://brickset.com/sets/year-1999']


 def parse(self, response, **kwargs):

  xpath_selector = '//img'


  for x in response.xpath(xpath_selector):

    newsel = '@src'

    yield {

      'Image Link': x.xpath(newsel).extract_first(),

}

# To recurse next page

  Page_selector = '.next a ::attr(href)'

  next_page = response.css(Page_selector).extract_first()

  if next_page:

     yield scrapy.Request(

       response.urljoin(next_page),

       callback=self.parse

 )

import requests

class TestApplication(request.TestCase):

	def test_upper(self):
		self.asserEqual('foo'.upper(),'FOO')

	
	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

if __name__== '__main__':
	requests.main()
