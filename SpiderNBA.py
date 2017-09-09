#coding=utf-8
import urllib
import re
from bs4 import BeautifulSoup

res_str = r'</div>(.*?)</div>'

def get_content_from_url(url):
	try:
		opener = urllib.urlopen(url)
		html_doc = opener.read()
		soup = BeautifulSoup(html_doc,"lxml")
		play_basic_info = soup.find_all("div", class_="row")
		count = 0
		info_list = []
		for info in play_basic_info:
			#print info
			content = re.findall(res_str,str(info),re.S|re.M)
			for x in content:
				if (x.__contains__("<a")):
					x = x.split("<a")[0].rstrip()
				if (x.strip() == ''):
					x = '--'	
				info_list.append(x.strip())
			count+=1
			if (count == 7):
				break
		image = soup.find_all("div", class_="image")
		for x in image:
			info_list.append('http://www.stat-nba.com'+x.img['src'])
		return "#".join(info_list)
	except Exception as e:
		raise e


def get_all_players(url):
	try:
		opener = urllib.urlopen(url)
		html_doc = opener.read()
		soup = BeautifulSoup(html_doc,"lxml")
		result = {}
		play_basic_info = soup.select('a[href^="./player/"]')
		for makeup in play_basic_info:
			result[makeup.span.contents[0]] = makeup['href']
		return result
	except Exception as e:
		raise e

#result = get_content_from_url('http://stats.nba.com/players/traditional/#!?sort=PLAYER_NAME&dir=-1&Season=2012-13&SeasonType=Regular%20Season&PerMode=Totals')

#result = get_content_from_url('http://www.stat-nba.com/player/116.html')
#print result

with open('play_info.txt', 'a+') as f:
 	start = [chr(i) for i in range(65,91)]
 	for i in start:
 		result = get_all_players('http://www.stat-nba.com/playerList.php?il='+i+'&lil=0')
 		for x in result:
 			url = 'http://www.stat-nba.com/'+result[x].split("./")[1]
 			res = get_content_from_url(url)
 			strconcat = '%s#%s\n' % ("".join(x).strip().encode('utf-8'), res)
 			f.write(strconcat)
 	f.close()
