# -*- coding: utf-8 -*-
import scrapy
import requests
import random
from time import sleep
import os.path

directory = 'ScriptsDL/'  #Change the location according to your server or PC

def saveFile(url, name, ext):
    r = requests.get(url)
    print('\n\n\n\nDownloading ' + name +
          ' from ==> ' + url + ' ...\n\n\n\n')
    with open(directory + name + ext, 'wb') as f:
        f.write(r.content)

def sleepRandom():
    sleep(random.randint(1, 3))

def sleepRandomLong():
    sleep(random.randint(13, 30))

class MoviescriptSpider(scrapy.Spider):
    name = 'movieScript'
    # handle_httpstatus_list = [404, 502, 302, 307, 503, 504, 500]  #If there are too many redirects
    allowed_domains = ['dailyscript.com']
    start_urls = ['http://www.dailyscript.com/movie.html',
                  'http://www.dailyscript.com/movie_n-z.html']

    def parse(self, response):
        tableNodes = response.css('table ul p')
        #this is for testing purpose to iterate top 5 moviews from each page
        # for tblNode in tableNodes[: 5]:
        #This is for production
        for tblNode in tableNodes:
            movieName = tblNode.css('a::text').extract_first()
            movieLink = tblNode.css('a::attr(href)').extract_first()
            scriptLink = response.urljoin(movieLink)
            sleepRandom()
            yield scrapy.Request(scriptLink, callback=self.dlScripts, meta={'movieName':movieName})


    def dlScripts(self, response):

        movieName = response.meta['movieName']
        movieLink = response.url
        extension = os.path.splitext(movieLink)[1]
        if extension != None:
            saveFile(movieLink, movieName, extension)
