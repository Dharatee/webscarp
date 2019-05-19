from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

#linking with the website
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
soup(page_html,"html.parser")


