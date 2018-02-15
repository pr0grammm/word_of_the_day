import requests
from bs4 import BeautifulSoup
from playsound import playsound

#url of page to download content from
url = "https://wordsmith.org/words/today.html"

page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

word = soup.find('h3').get_text()

divs_list = soup.find_all('div')

#print all text contained in div tags between PRONUNCIATION and USAGE
for div in divs_list:
	if div.get_text().strip().startswith("PRONUNCIATION"):
		start = divs_list.index(div)
	elif div.get_text().strip().startswith("A THOUGHT"):
		stop = divs_list.index(div)



link = str(divs_list[start+1].find('a').get('href'))

print("*" * 40)
print(word)
for tag in divs_list[start:stop]:
	print(tag.get_text())
print("*"*40)

print(link)
playsound(link)
	
	

