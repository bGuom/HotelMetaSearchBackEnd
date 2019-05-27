from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

URL='http://www2.hotelsearchengines.net/Hotels/Search?languageCode=EN&checkin=2019-06-06&checkout=2019-06-07&Rooms=1&Adults_1=2&destination=place%3Acolombo'
HotelDataArray = []

def Scrape(link):
    return getHotelData(link)


#Scraping
def getHotelData(URL):
    ua = UserAgent()
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    headers = {'User-Agent': ua.random}
    response = requests.get(URL,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    print response.content

    hotelList = soup.findAll(class_="hotel")
    print soup.find(class_="resultsContainer")


                
    return ""

     
    

print Scrape(URL)


