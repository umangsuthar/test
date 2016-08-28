import scrapy
import time
from sqtest.items import SqtestItem
class Dmoz(scrapy.Spider):
	name = "song"
	allowed_domains = ["songsmp3.net"]
	start_urls = ["http://songsmp3.net/"]

	def parse(self,response):
		sel = response.selector.xpath("//div[@class='list_box_2']/div[@class='list_box_inside']")
		for ss in sel.xpath("./ul/li/a/@href").extract():
			if ss.startswith('/1/'):
				s1 = ss
				s1 = "http://songsmp3.net"+s1
				#print(s1)
				yield scrapy.Request(s1,callback = self.MovieZip_parse)
	
	def MovieZip_parse(self,response):
		item = SqtestItem()

		nameOrg = response.selector.xpath("//h1/text()").extract()
		nameOrg = nameOrg[0]
		MovieName = "".join(nameOrg)
		item['MovieName'] = MovieName[:-9]
		item['TimeStamp'] = time.time()
		#print("\n")
		
		#print(item['MovieName'])
		#print("\n")
		da = response.selector.xpath("//div[@class='zip_links']//div[@class='link-item-zip']/a/@href").extract()
		item['Zip320']=da[0]
		item['Zip128']=da[1]

		print(item['Zip320'])
		print(item['Zip128'])
		#print("\n")
		yield item