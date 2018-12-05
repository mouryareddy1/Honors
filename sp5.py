import requests
import MySQLdb
 
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="",     # password
                     db="mydatabase",
                     charset='utf8',
                     use_unicode=True)   # name of the database

cur = db.cursor()
from bs4 import BeautifulSoup
#with open("search.html?rows=100") as fp:
#    soup = BeautifulSoup(fp)
page1=requests.get("http://dla.library.upenn.edu/dla/medren/search.html?rows=100&fq=collection_facet%3A%22Indic%20Manuscripts%22&start=100")
soup=BeautifulSoup(page1.content,'html.parser')

ratio=soup.find_all('a');

a = []
for i in range(len(ratio)):
	try:
		temp = ratio[i]['xmlns:dla-tool']
		tempo = ratio[i]['href']
		a+=[tempo.split('_')[2]]
		# if(ratio[i]['class'][0]=="recordinfolabel"):
		# 	print ratio[i].text
		# elif(ratio[i]['class'][0]=="recordinfotext") :
		# 	print ratio[i].text
	except:
		pass

a = list(set(a))
#print len(a);
fields = {
	"link" : "",
	"Author" : "" ,
"Title" : "" ,
"Physical" : "",
"Language":"",
"Summary":"",
"Subject":"",
"Form":"", 
 "Notes":"",
 "Indexed":"",
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
temp_dict = fields
array = []
#print a[0]
cnt=0;
out=open('out.html','a+');

#print a[0];
for i in range(0,len(a)):
	fields = {
	"link" : "",
	"Author" : "" ,
"Title" : "" ,
"Physical" : "",
"Language":"",
"Summary":"",
"Subject":"",
"Form":"", 
 "Notes":"",
 "Indexed":"",
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
	flag = ""
	page=requests.get("http://dla.library.upenn.edu/dla/medren/record.html?id=MEDREN_"+ str(a[i])+"start=100&rows=100&fq=collection_facet%3A%22Indic%20Manuscripts%22&");
	fields["link"]="http://dla.library.upenn.edu/dla/medren/record.html?id=MEDREN_"+ str(a[i])+"start=100&rows=100&fq=collection_facet%3A%22Indic%20Manuscripts%22&";
	soup = BeautifulSoup(page.content, 'html.parser')
	#print fields["link"]
	#print soup.prettify()
	ratio=soup.find_all('td');
	# print ratio
	for i in range(len(ratio)):
		try:
			#print ratio[i]['class'][0]

			if(ratio[i]['class'][0]=="recordinfolabel"):
				temp = ratio[i].text
				#print temp;
				tempo = temp.split(' ')[0].split(':')[0];
				print (tempo)
				# flag = tempo
				# if(temp[0] in fields):
				# 	flag = temp[0]
				# else:
				# 	tempo = temp[0][:-1]
				# 	if(tempo in fields):
				if tempo=="Language(s)":
					#print "saddas"
					tempo=tempo.split('(')[0];
					#print tempo;
				elif tempo=="Indexed/Referenced":
					tempo=tempo.split('/')[0];
					print tempo
				elif tempo == "Form/Genre":
					tempo=tempo.split('/')[1];
				if(tempo in fields):
					flag = tempo 
			elif(ratio[i]['class'][0]=="recordinfotext") :
				fields[flag] = ratio[i].text
				#print fields[flag];
			
			elif(ratio[i]['class'][0]=="recordfacetstxt"):
				temp = ratio[i].text
				temp0 = temp.split(':')[0]
				temp1 = temp.split(':')[1]
				if temp0=="Facsimile" or temp0=="Illuminated" or temp0=="Illustrated" or temp0=="Notated" or temp0=="Date" or temp0=="Geography":
					fields[temp0]=temp1;
					#print fields[temp0]
				

		except:
			pass
	t =[]
	t+=[fields["link"].replace("'","''")]

	#print fields["link"];
	out.write('<!DOCTYPE> \n<html>\n <head> \n</head> \n<body> \n</body\n> </html>\n')	
	# for link in fields["link"]:
	st='<p><a href='+fields["link"]+'>'+str(cnt)+'</a></p>';
	out.write(st)
	cnt=cnt+1;

	t+= [fields["Author"].replace("'","''")]
	t+= [fields["Title"].replace("'","''")]
	t+= [fields["Physical"].replace("'","''")]
	t+= [fields["Language"].replace("'","''")]
	t+= [fields["Summary"].replace("'","''")]
	t+= [fields["Subject"].replace("'","''")]
	t+= [fields["Form"].replace("'","''")]
	t+= [fields["Notes"].replace("'","''")]
	t+= [fields["Indexed"].replace("'","''")]
	t+= [fields["Other"].replace("'","''")]
	t+= [fields["Cite"].replace("'","''")]
	t+= [fields["Contained"].replace("'","''")]
	t+= [fields["Manuscript"].replace("'","''")]
	t+= [fields["Vernacular"].replace("'","''")]
	t+= [fields["Origin"].replace("'","''")]
	t+= [fields["Facsimile"].replace("'","''")]
	t+= [fields["Illuminated"].replace("'","''")]
	t+= [fields["Illustrated"].replace("'","''")]
	t+= [fields["Notated"].replace("'","''")]
	t+= [fields["Date"].replace("'","''")]
	t+= [fields["Geography"].replace("'","''")]

	variables = tuple(t)
	# t += []
	#print t	
	array += [t]
	#fields['Summary']=fields['Summary'].replace("'","''")
	#q = ['a','a','a','a','a','u' ,'a','a','a','a']
	#print fields['Author'];
	sql = """INSERT INTO final_data3 VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
	#cur.execute("set names utf8;")
	cur.execute(sql%tuple(t))
	
	# print (i + " inserted!!") 
	db.commit()
	#print "inserted"
db.close()
#for i in range(len(array)):
#	print (array[i])

out.close();