from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

#linking with the website
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()



#html parsing
page_soup=soup(page_html,"html.parser")

#print(page_soup.body)
#print(page_soup.head)
#print(page_soup.title) 
#or
#print(page_soup.head.title)

#header of the page or the title
page_soup.h1


#not found on the page, could be a hidden tagline
page_soup.p

#converting into csv, traverse DOM elements of the HTML
page_soup.body.span

#use find method to access parts instead of aforementioned print(page_soup.body)

#gives the div ID of section 1, the first one it finds
containers=page_soup.find("div """",{"class":"item-container"}""" )


#get more than one
#find_all() or findAll()
containers=page_soup.findAll('div')[2]  #div with ID of section 2

containers=page_soup.find(id='section-1')
containers=page_soup.find(class_='item-container') #class is a reserved word so use class_ .

print(containers)


