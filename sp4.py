import requests
import MySQLdb
 
db = MySQLdb.connect(host="localhost",  # your host 
                     user="mouryareddy",       # username
                     passwd="Mourya@123",     # password
                     db="mydatabase",
                     charset='utf8',
                     use_unicode=True)   # name of the database

cur = db.cursor()
from bs4 import BeautifulSoup
#with open("search.html?rows=100") as fp:
#    soup = BeautifulSoup(fp)
page1=requests.get("http://dla.library.upenn.edu/dla/medren/search.html?rows=100&fq=collection_facet%3A%22Indic%20Manuscripts%22&start=100")
soup=BeautifulSoup(page1.content,'html.parser')
#print soup.prettify()
ratio=soup.find_all('a');
#print len(ratio);

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
print len(a);
#print len(a);
fields = {
"link" : "",
"Author" : "" ,
"Title" : "" , 
"Physical" : "", 
"Summary" : "" ,
"Notes" : "" ,
"Cite" : "",
"Contained" : "",
"Manuscript"  : "",
"Vernacular" : "",
"Origin": ""}
temp_dict = fields
array = []
print a[0]
cnt=0;
out=open('out.html','a+');

#print a[0];
for i in range(0,len(a)):
	fields = {
	"link" : "",
	"Author" : "" ,
"Title" : "" , 
"Physical" : "", 
"Summary" : "" ,
"Notes" : "" ,
"Cite" : "",
"Contained" : "",
"Manuscript"  : "",
"Vernacular" : "",
"Origin": "",
}
	flag = ""
	page=requests.get("http://dla.library.upenn.edu/dla/medren/pageturn.html?fq=collection_facet%3A%22Indic%20Manuscripts%22&id=MEDREN_" + str(a[i]));
	fields["link"]="http://dla.library.upenn.edu/dla/medren/pageturn.html?fq=collection_facet%3A%22Indic%20Manuscripts%22&id=MEDREN_" + str(a[i]);
	soup = BeautifulSoup(page.content, 'html.parser')
	#print fields["link"]
	#print soup.prettify()
	ratio=soup.find_all('td');
	# print ratio
	for i in range(len(ratio)):
		try:
			# print ratio[i]['class'][0]

			if(ratio[i]['class'][0]=="recordinfolabel"):
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
				# print fields
				# print "hello"
		except:
			pass
	t =[]
	t+=[fields["link"].replace("'","''")]

	print fields["link"];
	out.write('<!DOCTYPE> \n<html>\n <head> \n</head> \n<body> \n</body\n> </html>\n')	
	# for link in fields["link"]:
	st='<p><a href='+fields["link"]+'>'+str(cnt)+'</a></p>';
	out.write(st)
	cnt=cnt+1;

	t+= [fields["Author"].replace("'","''")]
	t+= [fields["Title"].replace("'","''")]
	t+= [fields["Physical"].replace("'","''")]
	t+= [fields["Summary"].replace("'","''")]
	t+= [fields["Notes"].replace("'","''")]
	t+= [fields["Cite"].replace("'","''")]
	t+= [fields["Contained"].replace("'","''")]
	t+= [fields["Manuscript"].replace("'","''")]
	t+= [fields["Vernacular"].replace("'","''")]
	t+= [fields["Origin"].replace("'","''")]
	variables = tuple(t)
	# t += []
	#print t	
	array += [t]
	#fields['Summary']=fields['Summary'].replace("'","''")
	#q = ['a','a','a','a','a','u' ,'a','a','a','a']
	#print fields['Author'];
	sql = """INSERT INTO finaldata VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
	#cur.execute("set names utf8;")
	cur.execute(sql%tuple(t))
	
	# print (i + " inserted!!") 
	db.commit()
	print "inserted"
db.close()
for i in range(len(array)):
	print (array[i])

out.close();