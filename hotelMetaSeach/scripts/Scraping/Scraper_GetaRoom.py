from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

#URL = 'https://www.getaroom.com/search?page=2&per_page=10&destination=colombo&rinfo=[[18,5,3],[18,4]]&amenities=&sort_order=position&check_in=2019-06-03&check_out=2019-06-05'
#URL = 'https://www.getaroom.com/search?destination=colombo&page=1&per_page=25&rinfo=%5B%5B18%2C5%2C3%5D%2C%5B18%2C4%5D%5D&check_in=2019-06-03&check_out=2019-06-05'
#url ='https://www.getaroom.com/search?destination=london&page=1&per_page=25&rinfo=[[18]]&check_in=2019-06-05&check_out=2019-06-07'
HotelDataArray = []

def Scrape(link):
    return getHotelData(link)


# Scraping
def getHotelData(URL):
    ua = UserAgent()
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    headers = {'User-Agent':  ua.google }


    response = requests.get(URL, headers=headers)

    soup = BeautifulSoup(response.content, 'lxml')



    hotelList = soup.findAll(class_="hotel-card")


    for hotel in hotelList:
        content = hotel.find(class_='content')
        if(content!=None):
            details = content.find(class_="details")

            if(details.find(class_="title").find(class_="name")!=None):
                title = details.find(class_="title").find(class_="name").get_text().encode('ascii', 'ignore').replace("\n", "")
            else:
                title=""
            if(hotel.find(class_="click-target")!=None):
                link = hotel.find(class_="click-target")['href'].encode('ascii', 'ignore').replace("\n", "")
            else:
                link= ""
            if(details.find(class_="features")!=None):
                address = details.find(class_="features").get_text().encode('ascii', 'ignore').replace("\n", "")
            else:
                address=""
            if(content.find(class_='img-wrapper').find(class_='img')!=None):
                imageUrl = content.find(class_='img-wrapper').find(class_='img')['style'].replace("background-image:url(","").replace(")","")
            else:
                imageUrl=""
            if (details.find(class_="pricing").find(class_="price").find(class_="amount") != None):
                price = details.find(class_="pricing").find(class_="price").find(class_="amount").get_text().encode('ascii', 'ignore')
            else:
                price = ""
            price = price.replace('$', '')

            DataDic = {
                "title": title,
                "link": 'https://www.getaroom.com' + link,
                "address": address,
                "imageUrl": imageUrl,
                "price": price,
                "origin": 'getaroom.com'
            }
            HotelDataArray.append(DataDic)

    return HotelDataArray


#print Scrape(url)

