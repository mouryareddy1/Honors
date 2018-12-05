import requests
import MySQLdb
from bs4 import BeautifulSoup
page=requests.get("http://dla.library.upenn.edu/dla/medren/record.html?id=MEDREN_9958067103503681&start=100&rows=100&fq=collection_facet%3A%22Indic%20Manuscripts%22&");
soup = BeautifulSoup(page.content, 'html.parser')
	#print fields["link"]
	#print soup.prettify()
ratio=soup.find_all('td');
#print ratio
for i in range(len(ratio)):
	fields = {
	"link" : "",
	"Author" : "" ,
"Title" : "" ,
"Physical" : "",
"Language(s)":"",
"Subject":"",
"Form/Genre":"", 
 "Notes":"",
 "Indexed/Referenced":"",
 "Other":"",
"Cite" : "",
"Contained" : "",
"Manuscript"  : "",
"Vernacular" : "",
"Origin": "",
"Facsimile":"",
"Illuminated":"",
"Illustrated":"",
"Notated":"",
"Date":"",
"Geography":""
}
	try:
		#print ratio[i]['class'][0]

		if(ratio[i]['class'][0]=="recordfacetstxt"):
			temp = ratio[i].text
			temp0 = temp.split(':')[0]
			temp1 = temp.split(':')[1]
			if temp0=="Facsimile" or temp0=="Illuminated" or temp0=="Illustrated" or temp0=="Notated" or temp0=="Date" or temp0=="Geography":
				fields[temp0]=temp1;
				print fields[temp0]	
		elif(ratio[i]['class'][0]=="recordinfolabel"):
			temp = ratio[i].text
			tempo = temp.split(' ')[0].split(':')[0]
				# print (tempo)
				# flag = tempo
				# if(temp[0] in fields):
				# 	flag = temp[0]
				# else:
				# 	tempo = temp[0][:-1]
				# 	if(tempo in fields):
			if(tempo in fields):
				flag = tempo 
		elif(ratio[i]['class'][0]=="recordinfotext") :
			fields[flag] = ratio[i].text
			print fields[flag]

				# flag = tempo
				# if(temp[0] in fields):
				# 	flag = temp[0]
				# else:
				# 	tempo = temp[0][:-1]
				# 	if(tempo in fields):
				#if(tempo in fields):
				#	flag = tempo 
			#elif(ratio[i]['class'][0]=="recordinfotext") :
			#	print ratio[i].text
		#print fields
				# print "hello"
	except:
		pass
