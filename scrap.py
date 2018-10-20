from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os
import requests
from amazon.api import AmazonAPI
import bottlenose.api
from selenium import webdriver
from lxml.html import fromstring
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class GamePriceComparator:

	HEADS={
		"fnac":"https://www.fnac.es/SearchResult/ResultList.aspx?SCat=0%211&Search=",
		"amazon":"https://www.amazon.es/s/ref=nb_sb_noss?field-keywords=",
		"game":"https://www.game.es/buscar/",
		"instant gaming":"https://www.instant-gaming.com/es/busquedas/?q=",
		"corte ingles":"https://www.elcorteingles.es/videojuegos/search/?s=",
	}

	SEPARATORS={
		"fnac":"+",
		"amazon":"+",
		"game":"-",
		"instant gaming":"+",
		"corte ingles":"+",
	}

	def get_response(self,url):
		ua=UserAgent()
		header={'User-Agent':ua.random}
		r = requests.get(url,headers=header)
		return r

	def get_url(self,site,search):
		search=search.replace(" ",self.SEPARATORS[site])
		head=self.HEADS[site]
		return head+search
	'''
	Returns (price, url, name)
	'''
	def get_price_fnac(self,search):
		url=self.get_url("fnac",search)
		try:
			response=self.get_response(url)
			soup=BeautifulSoup(response.text,'html.parser')
			first_price=soup.find_all("a", {"class": "userPrice"})[0].text
			first_url=soup.find_all("a", {"class": "userPrice"})[0].attrs["href"]
			first_name=soup.find_all("a",{"class":"js-minifa-title"})[0].text
			return (first_price,first_url,first_name)
		except:
			return ("No se ha podido conseguir el precio",url,search)

	def get_price_instant_gaming(self,search):
		url=self.get_url("instant gaming",search)
		try:
			response=self.get_response(url)
			soup=BeautifulSoup(response.text,'html.parser')
			first_price=soup.find_all("div",{"class":"item mainshadow"})[0].attrs["data-price"]
			first_price=first_price.replace(".",",")+"€"
			first_url=soup.find_all("a",{"class":"cover"})[0].attrs["href"]
			first_name=soup.find_all("div",{"class":"name"})[0].text
			return (first_price,first_url+"?igr=morive02-21",first_name)
		except:
			return ("No se ha podido conseguir el precio",url,search)

	def get_price_corte_ingles(self,search):
		url=self.get_url("corte ingles",search)
		try:
			response=self.get_response(url)
			soup=BeautifulSoup(response.text,'html.parser')
			first_price=soup.find_all("span",{"class":"current sale"})[0].text
			first_url=soup.find_all("a",{"class":"event"})[0].attrs["href"]
			first_name=soup.find_all("a",{"class":"js-product-click event "})[0].text
			return (first_price,"https://www.elcorteingles.es"+first_url,first_name)
		except:
			return ("No se ha podido conseguir el precio",url,search)

	def get_price_amazon(self,search):
		url=self.get_url("amazon",search)
		try:	
			amazon = AmazonAPI("Your amazon key", "Your amazon secret", "Your amazon vendor user", region="ES")
			region_options = bottlenose.api.SERVICE_DOMAINS.keys()
			products = amazon.search_n(1,Keywords=search, SearchIndex='VideoGames')
			price=products[0].price_and_currency
			if price[0]==None:
				return ("No se ha podido conseguir el precio",url,search)
			else:
				price=str(price[0]).replace(".",",") + "€"

			return (price,products[0].offer_url,products[0].title)
		except Exception as e:
			print("Error precio amazon: --- ",e)
			return ("No se ha podido conseguir el precio",url,search)


	def get_price_game(self,search):
		#export PATH=$PATH:/path/to/geckodriver
		#or Put geckodriver in usr/local/bin
		search_url=self.get_url("game",search)
		os.system("export PATH=$PATH:/home/marcos/geckodriver")
		fails=0
		while True:
			try:	
				ua=UserAgent()
				options=Options()
				options.add_argument("--headless")
				driver = webdriver.Firefox(firefox_options=options)
				driver.implicitly_wait(10)
				driver.get(search_url)
				body=driver.find_element_by_tag_name("body")
				soup=BeautifulSoup(body.get_attribute('innerHTML'),'html.parser')
				game_page=soup.find_all("a",{"class":"a cm-txt"})[0].attrs["href"]
				game_name=soup.find_all("a",{"class":"a cm-txt"})[0].text
				break
			except Exception as e:
				fails=fails+1
				if(fails>15):
					return ("No se ha podido conseguir el precio",search_url,search)
		product_url=""
		while True:
			try:
				product_url="https://game.es"+game_page
				fails=0
				ua=UserAgent()
				options=Options()
				options.add_argument("--headless")
				driver = webdriver.Firefox(firefox_options=options)
				driver.implicitly_wait(10)
				driver.get(product_url)
				body=driver.find_element_by_tag_name("body")
				soup=BeautifulSoup(body.get_attribute('innerHTML'),'html.parser')
				price=soup.find_all("span",{"class":"buy--info"})[0].text
				break
			except Exception as e:
				fails=fails+1
				if(fails>15):
					return ("No se ha podido conseguir el precio",product_url,search)
		return (price[25:33],product_url,game_name)






