import scrapy
import time
from scrapy.selector import HtmlXPathSelector
from ssong.items import SsongItem
class scrp(scrapy.Spider):
	name = "scr"
	allowed_domains = ["songsmp3.net"]
	start_urls = ["http://songsmp3.net/"]
	def parse(self,response):
		sel = response.selector.xpath("//div[@class='list_box_2']/div[@class='list_box_inside']")
		for ss in sel.xpath("./ul/li/a/@href").extract():
			if ss.startswith('/1/'):
				s1 = ss
				s1 = "http://songsmp3.net"+s1
				yield scrapy.Request(s1,callback = self.SongParse)

	def SongParse(self,response):
		nameOrg = response.selector.xpath("//h1/text()").extract()
		nameOrg = nameOrg[0]
		MovieName = "".join(nameOrg)
		Mname = MovieName[:-9]
		so = response.selector.xpath("//div[@class='download-single-links_box']//div[@class='link-item']")
		for link in so.xpath("./a/@href").extract():
			link = "http://songsmp3.net"+link
			#name12= so.xpath("./a/div[@class='link']/text()").extract()
			yield scrapy.Request(link,callback = self.Song_Link, meta={'name': Mname})
		'''print("\n")
		   print(name12)
		   print("\n")'''

	def Song_Link(self,response):
		item = SsongItem()
		print("\n")	
		#print(response.meta['name'])
		item['MovieName'] = response.meta['name']
		#print(item['MovieName'])
		item['TimeStamp'] = time.time()
		
		so_link = response.selector.xpath("//div[@class='download-single-links_box']//div[@class='sinlge_link_item']")
		ll = so_link.xpath("./div[@class='link-item_button3']/a/@href").extract()
		na = so_link.xpath("./div[@class='link-item2']/div[@class='link']/text()").extract()
		item['SongName'] = na[0]
		#print(item['SongName'])
		item['MP128'] = ll[0]
		item['MP320'] = ll[1]
		#print("\n")	
		#print(item['MP128'])
		#print(item['MP320'])
		#print("\n")
		yield item

