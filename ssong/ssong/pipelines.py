# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class SsongPipeline(object):
	def __init__(self):
		self.con = sqlite3.connect('/home/sahajanand/Desktop/Crawlar/song.db')
		self.con.row_factory = lambda cursor, row: row[0]
		self.cur = self.con.cursor()
		self.cur.execute('CREATE TABLE IF NOT EXISTS ssong ' \
                    '(MovieName TEXT,SongName TEXT ,MP128 TEXT, MP320 TEXT, TimeStamp TEXT)')

	def process_item(self, item, spider):
		valid = True
		for data in item:
			if not data:
				valid = False
				raise DropItem("Missing{0}!".format(data))
		self.cur.execute("select SongName from ssong")
		result = self.cur.fetchall()	

		if item['SongName'] not in result:
			log.msg("Eligible to insert %s" % item['MovieName'], level=log.DEBUG)
			self.cur.execute("INSERT INTO ssong(MovieName,SongName,MP128,MP320,TimeStamp) VALUES( ?, ?, ?, ?, ?)",(item['MovieName'],item['SongName'],item['MP128'],item['MP320'],item['TimeStamp']))
			self.con.commit()
			log.msg("Inserted Successfully", level=log.DEBUG)

		else:
			log.msg("Not In", level=log.DEBUG)
		
		return item



#Left Work From Here So Please check and complite it
