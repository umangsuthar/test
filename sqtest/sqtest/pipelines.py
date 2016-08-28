# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class SqtestPipeline(object):
	def __init__(self):
		self.con = sqlite3.connect('/home/sahajanand/Desktop/Crawlar/song.db')
		self.con.row_factory = lambda cursor, row: row[0]
		self.cur = self.con.cursor()
		self.cur.execute('CREATE TABLE IF NOT EXISTS msong ' \
                    '(MovieName TEXT, Zip128 TEXT, Zip320 TEXT, TimeStamp TEXT)')

	def process_item(self, item, spider):
		valid = True
		for data in item:
			if not data:
				valid = False
				raise DropItem("Missing{0}!".format(data))
		self.cur.execute("select MovieName from msong")
		result = self.cur.fetchall()
		

		if item['MovieName'] not in result:
			log.msg("Eligible to insert %s" % item['MovieName'], level=log.DEBUG)
			self.cur.execute("INSERT INTO msong(MovieName,Zip128,Zip320,TimeStamp) VALUES( ?, ?, ?,?)",(item['MovieName'],item['Zip128'],item['Zip320'],item['TimeStamp']))
			self.con.commit()
		else:
			log.msg("Not In", level=log.DEBUG)
		
		return item
