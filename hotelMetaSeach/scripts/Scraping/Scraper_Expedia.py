from bs4 import BeautifulSoup
import requests


## BOT DETECTION
## BOT DETECTION
## BOT DETECTION
## BOT DETECTION


URL='http://www.expedia.com/Hotel-Search?adults=2&children=1_10&destination=Kandy%2C%20Sri%20Lanka&endDate=14%2F06%2F2019&regionId=178045&rooms=1&startDate=04%2F06%2F2019'
HotelDataArray = []



#Get the WebPage by sending a request to the URL        
headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
response = requests.get(URL,headers=headers)


soup = BeautifulSoup(response.text,'html.parser')

print response.text

hotelList = soup.findAll(class_="results")

for hotel in hotelList:

    title =  hotel.find(class_="uitk-card-content").find(class_="uitk-grid").find(class_="uitk-cell").find(class_="uitk-type-400").get_text().encode('ascii', 'ignore').replace("\n","")
    
    link = hotel.find(class_="listing__link")['href'].encode('ascii', 'ignore').replace("\n","")
    address = hotel.find(class_="listing__neighborhood ").get_text().encode('ascii', 'ignore').replace("\n","")
    #print title , "\n"
    imageUrl = hotel.find(class_="uitk-image")['style'].encode('ascii', 'ignore')
    price = hotel.find(class_="content-hotel-lead-price--a11y").get_text()


    
    DataDic =	{
                    "title": title,
                    "link": link,
                    "address": address,
                    "imageUrl":imageUrl,
                    "price":price
                }
    HotelDataArray.append(DataDic)
            




     
    




