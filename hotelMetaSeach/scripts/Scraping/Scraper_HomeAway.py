from bs4 import BeautifulSoup
import requests

URL = 'https://www.homeaway.com/search/keywords:kandy/arrival:2019-06-03/departure:2019-06-05/minBedrooms/2?petIncluded=false&adultsCount=1&childrenCount=1'

HotelDataArray = []

def Scrape(link):
    return getHotelData(link)


# Scraping
def getHotelData(URL):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    response = requests.get(URL, headers=headers)

    soup = BeautifulSoup(response.content, 'lxml')

    hotelList = soup.findAll(class_="Hit")



    for hotel in hotelList:
        title = hotel.find(class_="HitInfo__headline").get_text().encode('ascii', 'ignore').replace("\n", "")
        link = hotel.find(class_="HitInfo__headline")['href'].encode('ascii', 'ignore').replace("\n", "")
        if(hotel.find(class_="GeoDistance")!=None):
            address = hotel.find(class_="GeoDistance").get_text().encode('ascii', 'ignore').replace("Show on map", "").replace("\n", "")
        else:
            address=""
        imageUrl = hotel.find('a').find(class_="HitCarousel")['style']##[hotel.find('a').find(class_="HitCarousel")['style'].find(':')+1::]
        if (hotel.find(class_="PriceSummary__amount") != None):
            price = hotel.find(class_="PriceSummary__amount").get_text()
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


