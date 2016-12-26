from bs4 import BeautifulSoup
from urllib.request import urlopen
import os, time, re

#Function that will return sites html file
def get_html(url):
	response = urlopen(url)
	return response.read()
#
#Parsing privat24 with the best deal for currency exchange
#
def parse_privat(html):
	soup = BeautifulSoup(html)
	currency_table = soup.find('tbody', id='selectByCard')
	currency = currency_table.find_all('tr')
	price = currency[3].text.split()
	price = float(price[1])
	return price
#
#Parsing qiwi with the best deal for currency exchange
#
def parse_qiwi(html):
	soup = BeautifulSoup(html)
	currency_table = soup.find('table', id='content_table')
	current_html = currency_table.find_all('div','pa')
	htmls = re.findall('href="(.*?)"', str(current_html))
	currency_list = currency_table.find_all('td', 'bi')
	prices = []

	#List with prices
	#ITS NOT FORMATED INF, IT LOOKS LIKE THIS 0000 UAH PRIVAT24
	for item in currency_list:
		if 'UAH' in item.text:
			prices.append(item.text.split())
	#NOW THIS LIST WILL KEEP ONLY NUMBERS
	formated_prices = []
	for price in prices:
		formated_prices.append(float(price[0]))
	
	return max(formated_prices), htmls[0]

#Calculate money with privat
def money_with_privat(money, privat):
	total_money = (money - 100 -(money*0.02))*privat
	print("2. Through the PRIVAT24: you will receive - {0:.4f} UAH, exchange currency: {1:.4f}\n".format(total_money, privat))

#Calculate money with qiwi
def money_with_qiwi(money, qiwi, name):
	total_money = money*qiwi
	print("1. Through the QIWI: you will receive - {0:.4f} UAH, exchange currency: {1:.4f}\n".format(total_money, qiwi))
	print("HTML: {0}\n".format(name))
#Main function =) 
def main():
	active = True
	while active:
		try:
			money = int(input("Enter the sum that you want to exchange: "))
			active = False
		except ValueError:
			print("Not text, just a number")
			time.sleep(2)
			try:
				os.system('clear')
			except:
				os.system('cls')
	qiwi, name_of_site = parse_qiwi(get_html('http://www.bestchange.ru/index.php?sort=to&range=desc&mt=&from=63&to=56'))
	privat = parse_privat(get_html('https://privatbank.ua'))

	money_with_qiwi(money, qiwi, name_of_site)
	money_with_privat(money, privat)
	


if __name__ == '__main__':
	main()
