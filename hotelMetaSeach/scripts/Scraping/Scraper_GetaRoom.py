from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

#URL = 'https://www.getaroom.com/search?page=2&per_page=10&destination=colombo&rinfo=[[18,5,3],[18,4]]&amenities=&sort_order=position&check_in=2019-06-03&check_out=2019-06-05'
#URL = 'https://www.getaroom.com/search?destination=colombo&page=1&per_page=25&rinfo=%5B%5B18%2C5%2C3%5D%2C%5B18%2C4%5D%5D&check_in=2019-06-03&check_out=2019-06-05'
#url ='https://www.getaroom.com/search?destination=london&page=1&per_page=25&rinfo=[[18]]&check_in=2019-06-05&check_out=2019-06-07'

#Scrape method - link will be the generated search query url using QueryGenerator.
def Scrape(link):
    return getHotelData(link)


#Scraping the search results
def getHotelData(URL):
    HotelDataArray = []
    ua = UserAgent()
    # Create header for the request with user agent
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    headers = {'User-Agent':  ua.google }       # Using fake agent lib to send fake agent
    # Get the WebPage by sending a request to the URL
    response = requests.get(URL, headers=headers)

    soup = BeautifulSoup(response.content, 'lxml')          #Scraping search rsult using bs library

    hotelList = soup.findAll(class_="hotel-card")           #Getting array of search results


    for hotel in hotelList:                                 #Scrape each hotel to get required data into the dictionary
        #Body of the search rsults
        content = hotel.find(class_='content')
        if(content!=None):
            details = content.find(class_="details")
            #Hotel title
            if(details.find(class_="title").find(class_="name")!=None):
                title = details.find(class_="title").find(class_="name").get_text().encode('ascii', 'ignore').replace("\n", "")
            else:
                title=""
            #Link to the booking site of the hotel
            if(hotel.find(class_="click-target")!=None):
                link = hotel.find(class_="click-target")['href'].encode('ascii', 'ignore').replace("\n", "")
            else:
                link= ""
            #Address or the placement of the hotel
            if(details.find(class_="features")!=None):
                address = details.find(class_="features").get_text().encode('ascii', 'ignore').replace("\n", "")
            else:
                address=""
            #Link to the image of hotel
            if(content.find(class_='img-wrapper').find(class_='img')!=None):
                imageUrl = content.find(class_='img-wrapper').find(class_='img')['style'].replace("background-image:url(","").replace(")","")
            else:
                imageUrl=""
            #Hotel price
            if (details.find(class_="pricing").find(class_="price").find(class_="amount") != None):
                price = details.find(class_="pricing").find(class_="price").find(class_="amount").get_text().encode('ascii', 'ignore')
            else:
                price = ""
            price = price.replace('$', '')

            if (title != ""):
                # Adding scrapped detials into a dictionary
                DataDic = {
                    "title": title,
                    "link": 'https://www.getaroom.com' + link,
                    "address": address,
                    "imageUrl": imageUrl,
                    "price": price,
                    "origin": 'getaroom.com'
                }
                # Adding hotel data dictionary to hoteldata arry
                HotelDataArray.append(DataDic)

    # Return final hotel data array with list of scrapped hotel data
    return HotelDataArray


#print Scrape(url)

