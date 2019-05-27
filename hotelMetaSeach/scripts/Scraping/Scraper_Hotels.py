from bs4 import BeautifulSoup
import requests

#URL='https://www.hotels.com/search.do?&q-destination=colombo&q-check-in=2019-06-15&q-check-out=2019-06-22&q-rooms=1&q-room-0-adults=2&q-room-0-children=0'

HotelDataArray = []

def Scrape(link):
    return getHotelData(link)


#Scraping
def getHotelData(URL):
    for pageno in range(1,7):

        #Get the WebPage by sending a request to the URL
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        response = requests.get(URL+"&pn="+str(pageno),headers=headers)

        soup = BeautifulSoup(response.text,'lxml')

        hotelList = soup.findAll(class_="hotel")

        for hotel in hotelList:
            title =  hotel.find(class_="p-name").get_text().encode('ascii', 'ignore')
            link = hotel.find(class_="p-name").find('a')['href'].encode('ascii', 'ignore')
            address = hotel.find(class_="location-info").get_text().encode('ascii', 'ignore')
            if(hotel.find(class_="u-photo")!=None):
                imageUrl = hotel.find(class_="u-photo")['style'][hotel.find(class_="u-photo")['style'].find('\'')+1:-2].encode('ascii', 'ignore')
            else:
                imageUrl = ""

            if(hotel.find(class_="price")!=None):

                if (hotel.find(class_="price").find('strong')!=None):
                    price = hotel.find(class_="price").find('strong').get_text().encode('ascii', 'ignore')
                else:
                    price = hotel.find(class_="price").find('ins').get_text().encode('ascii', 'ignore')
                price = price.replace('USD', '')
                DataDic =	{
                            "title": title,
                            "link": 'https://www.hotels.com/'+link,
                            "address": address,
                            "imageUrl":imageUrl,
                            "price":price,
                            "origin":'hotels.com'
                            }

                tempArr = []
                tempArr.append(title)
                tempArr.append(link)
                tempArr.append(address)
                tempArr.append(imageUrl)
                tempArr.append(price)   
                HotelDataArray.append(DataDic)
                
    return HotelDataArray

     
    

#print Scrape(URL)


