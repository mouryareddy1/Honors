import requests
#import re
page=requests.get("http://dla.library.upenn.edu/dla/medren/record.html?id=MEDREN_9960163793503681&fq=collection_facet%3A%22Indic%20Manuscripts%22&");
#print page.status_code;
from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser');
print soup.prettify()
#with open("search.html?rows=100") as fp:
#    soup = BeautifulSoup(fp)
# soup = BeautifulSoup('search.html?rows=100', 'html.parser')
#print soup.prettify()
#ratio=soup.find_all('a');
# print ratio
#a = []
#for i in range(len(ratio)):
#	try:
#		temp = ratio[i]['xmlns:dla-tool']
#		tempo = ratio[i]['href']
#		a+=[tempo.split('_')[1]]
		# if(ratio[i]['class'][0]=="recordinfolabel"):
		# 	print ratio[i].text
		# elif(ratio[i]['class'][0]=="recordinfotext") :
		# 	print ratio[i].text
#	except:
#		pass
#print len(a)
#a = list(set(a))
#print len(a)
# for i in range(len(a)):
# 	print a[i]
#print soup.html.table.contents[3]
# print ratio
