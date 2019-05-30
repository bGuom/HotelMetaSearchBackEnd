from bs4 import BeautifulSoup
import requests


#URL='https://www.booking.com/searchresults.en-gb.html?ss=colombo&checkin_year=2019&checkin_month=6&checkin_monthday=15&checkout_year=2019&checkout_month=6&checkout_monthday=22&group_adults=2&group_children=1&age=12&no_rooms=1&rows=50&selected_currency=USD&changed_currency=1&top_currency=1&nflt='
#URL='https://www.booking.com/searchresults.en-gb.html?ss=colombo&checkin_year_month_monthday=2019-06-15&checkout_year_month_monthday=2019-06-20&group_adults=2&group_children=0&no_rooms=1&rows=50&selected_currency=USD&changed_currency=1&top_currency=1&nflt='


#Scrape method - link will be the generated search query url using QueryGenerator.
def Scrape(link):
    return getHotelData(link)

#Scraping the search results
def getHotelData(URL):
    HotelDataArray = []             #Create a temp array to store hotel data dictionaries

    # Create header for the request with user agent
    headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    # Get the WebPage by sending a request to the URL
    response = requests.get(URL,headers=headers)

    soup = BeautifulSoup(response.content,'lxml')           #Scraping search rsult using bs library

    hotelList = soup.findAll(class_="sr_item")              #Getting array of search results

    for hotel in hotelList:                                 #Scrape each hotel to get required data into the dictionary
        if(hotel.find(class_="sr-hotel__name")!=None):
            #Title of the hotel
            title =  hotel.find(class_="sr-hotel__name").get_text().encode('ascii', 'ignore').replace("\n","")
        else:
            title=""
        if(hotel.find(class_="hotel_name_link url")!=None):
            #Link to the hotel booking site
            link = hotel.find(class_="hotel_name_link url")['href'].encode('ascii', 'ignore').replace("\n","")
        else:
            link=""
        if(hotel.find(class_="address")!=None):
            #Address or the placement of the hotel
            address = hotel.find(class_="address").get_text().encode('ascii', 'ignore').replace("Show on map","").replace("\n","")
        else:
            address=""
        if(hotel.find(class_="sr_item_photo")!=None):
            #Link to the hotel image
            imageUrl = hotel.find(class_="sr_item_photo").find(class_="hotel_image")['src'].encode('ascii', 'ignore')
        else:
            imageUrl=""
        #Price of the hotel
        if (hotel.find(class_="sr_rooms_table_block") != None):
            if (hotel.find(class_="sr_rooms_table_block").find(class_="room_details") != None):
                if(hotel.find(class_="sr_rooms_table_block").find(class_="room_details").find(class_="bui-price-display__value")!=None):
                    price = hotel.find(class_="sr_rooms_table_block").find(class_="room_details").find(class_="bui-price-display__value").get_text()
                else:
                    price = ""
            else:
                price = ""
        else:
            price = ""

        price = price.replace('US$','')         # Remove USD symbol from the price

        if(title!=""):
            # Adding scrapped detials into a dictionary
            DataDic =	{
                            "title": title,
                            "link": 'https://www.booking.com'+link,
                            "address": address,
                            "imageUrl":imageUrl,
                            "price":price,
                            "origin":'booking.com'
                        }
            # Adding hotel data dictionary to hoteldata arry
            HotelDataArray.append(DataDic)

    # Return final hotel data array with list of scrapped hotel data
    return HotelDataArray


#print Scrape(URL)

        




