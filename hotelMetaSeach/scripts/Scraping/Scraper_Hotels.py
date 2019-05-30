from bs4 import BeautifulSoup
import requests

#URL='https://www.hotels.com/search.do?&q-destination=colombo&q-check-in=2019-06-15&q-check-out=2019-06-22&q-rooms=1&q-room-0-adults=2&q-room-0-children=0'


#Scrape method - link will be the generated search query url using QueryGenerator.
def Scrape(link):
    return getHotelData(link)


#Scraping the search results
def getHotelData(URL):
    HotelDataArray = []                         #Create a temp array to store hotel data dictionaries
    for pageno in range(1,7):                   #Loop through few pages of search results

        #Create header for the request with user agent
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        # Get the WebPage by sending a request to the URL
        response = requests.get(URL+"&pn="+str(pageno),headers=headers) #Page number is added as 'pn'

        soup = BeautifulSoup(response.text,'lxml')      #Scraping search rsult using bs library

        hotelList = soup.findAll(class_="hotel")        #Getting array of search results

        for hotel in hotelList:                         #Scrape each hotel to get required data into the dictionary
            #Title of the hotel
            title =  hotel.find(class_="p-name").get_text().encode('ascii', 'ignore')
            #Link to the hotel booking
            link = hotel.find(class_="p-name").find('a')['href'].encode('ascii', 'ignore')
            #Address or the placement information
            address = hotel.find(class_="location-info").get_text().encode('ascii', 'ignore')
            #Hotel image
            if(hotel.find(class_="u-photo")!=None):
                imageUrl = hotel.find(class_="u-photo")['style'][hotel.find(class_="u-photo")['style'].find('\'')+1:-2].encode('ascii', 'ignore')
            else:
                imageUrl = ""
            #Hotel price
            if(hotel.find(class_="price")!=None):

                if (hotel.find(class_="price").find('strong')!=None):
                    price = hotel.find(class_="price").find('strong').get_text().encode('ascii', 'ignore')
                else:
                    price = hotel.find(class_="price").find('ins').get_text().encode('ascii', 'ignore')
                price = price.replace('USD', '')

                #Adding scrapped detials into a dictionary
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

                #Adding hotel data dictionary to hoteldata arry
                HotelDataArray.append(DataDic)

    #Return final hotel data array with list of scrapped hotel data
    return HotelDataArray

     
    

#print Scrape(URL)


