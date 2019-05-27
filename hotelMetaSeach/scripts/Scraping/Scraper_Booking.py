from bs4 import BeautifulSoup
import requests


#URL='https://www.booking.com/searchresults.en-gb.html?ss=colombo&checkin_year=2019&checkin_month=6&checkin_monthday=15&checkout_year=2019&checkout_month=6&checkout_monthday=22&group_adults=2&group_children=1&age=12&no_rooms=1&rows=50&selected_currency=USD&changed_currency=1&top_currency=1&nflt='
#URL='https://www.booking.com/searchresults.en-gb.html?ss=colombo&checkin_year_month_monthday=2019-06-15&checkout_year_month_monthday=2019-06-20&group_adults=2&group_children=0&no_rooms=1&rows=50&selected_currency=USD&changed_currency=1&top_currency=1&nflt='

HotelDataArray = []

def Scrape(link):
    return getHotelData(link)

def getHotelData(URL):


    headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    response = requests.get(URL,headers=headers)

    soup = BeautifulSoup(response.content,'lxml')



    hotelList = soup.findAll(class_="sr_item")

    for hotel in hotelList:
        title =  hotel.find(class_="sr-hotel__name").get_text().encode('ascii', 'ignore').replace("\n","")
        link = hotel.find(class_="hotel_name_link url")['href'].encode('ascii', 'ignore').replace("\n","")
        address = hotel.find(class_="address").get_text().encode('ascii', 'ignore').replace("Show on map","").replace("\n","")
        #print title , "\n"

        imageUrl = hotel.find(class_="sr_item_photo").find(class_="hotel_image")['src'].encode('ascii', 'ignore')
        #print hotel
        #print hotel.find(class_="sr_rooms_table_block").find(class_="room_details").find(class_="roomrow").find(class_="roomPrice")
        if(hotel.find(class_="sr_rooms_table_block").find(class_="room_details").find(class_="bui-price-display__value")!=None):
            price = hotel.find(class_="sr_rooms_table_block").find(class_="room_details").find(class_="bui-price-display__value").get_text()
        else:
            price = ""
        price = price.replace('US$','')
        
        DataDic =	{
                        "title": title,
                        "link": 'https://www.booking.com'+link,
                        "address": address,
                        "imageUrl":imageUrl,
                        "price":price,
                        "origin":'booking.com'
                    }
        HotelDataArray.append(DataDic)
                
    return HotelDataArray


#print Scrape(URL)

        




