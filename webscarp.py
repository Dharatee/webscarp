from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

#linking with the website
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()



#html parsing
page_soup=soup(page_html,"html.parser")

print(page_soup.body)
print(page_soup.head)
print(page_soup.title)

"""#header of the page
page_soup.h1


#not found on the page, could be a hidden tagline
page_soup.p

#converting into csv, traverse DOM elements of the HTML
page_soup.body.span

containers=page_soup.findAll("div",{"class":"item-container"})
len(containers)

containers[0]  #should see HTML for this index"""




