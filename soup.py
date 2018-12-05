import requests
page=requests.get("http://dla.library.upenn.edu/dla/medren/pageturn.html?fq=collection_facet%3A%22Indic%20Manuscripts%22&id=MEDREN_9969570713503681&");
#print page.status_code;
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
#print soup.prettify()
ratio=soup.find_all('td');
# print ratio
for i in range(len(ratio)):
	try:
		# print ratio[i]['class'][0] 
		if(ratio[i]['class'][0]=="recordinfolabel"):
			print ratio[i].text
		elif(ratio[i]['class'][0]=="recordinfotext") :
			print ratio[i].text
	except:
		pass
#print soup.html.table.contents[3]
# print ratio
