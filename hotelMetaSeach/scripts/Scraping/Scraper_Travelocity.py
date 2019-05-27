from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

## BOT DETECTION
## BOT DETECTION
## BOT DETECTION
## BOT DETECTION

URL = 'https://www.travelocity.com/Hotel-Search?destination=kandy&startDate=06%2F02%2F2019&endDate=06%2F03%2F2019&rooms=2&adults=2,3&children=1_10,2_8%,2_10,2_11'

HotelDataArray = []

def Scrape(link):
    return getHotelData(link)


# Scraping
def getHotelData(URL):
    ua = UserAgent()
    #headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    headers = {'User-Agent':  ua.google }


    response = requests.get(URL, headers=headers)

    soup = BeautifulSoup(response.content, 'lxml')

    print response.content

    hotelList = soup.findAll(class_="hotel")



    for hotel in hotelList:
        title = hotel.find(class_="hotelTitle").get_text().encode('ascii', 'ignore').replace("\n", "")
        link = hotel.find(class_="flex-link")['href'].encode('ascii', 'ignore').replace("\n", "")
        if(hotel.find(class_="neighborhood secondary")!=None):
            address = hotel.find(class_="neighborhood secondary").get_text().encode('ascii', 'ignore').replace("Show on map", "").replace("\n", "")
        else:
            address=""
        imageUrl = hotel.find('flex-figure thumbnail-container').find(class_="hotel-thumbnail")
        if (hotel.find(class_="hotel-price").find(class_="actualPrice") != None):
            price = hotel.find(class_="hotel-price").find(class_="actualPrice").get_text()
        else:
            price = ""
        price = price.replace('$', '')

        DataDic = {
            "title": title,
            "link": 'https://www.homeaway.com' + link,
            "address": address,
            "imageUrl": imageUrl,
            "price": price,
            "origin": 'homeaway.com'
        }
        HotelDataArray.append(DataDic)

    return HotelDataArray

print Scrape(URL)


