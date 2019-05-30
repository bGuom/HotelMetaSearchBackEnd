
import QueryGenerator as qg                     ## Query Generator for generating  search queries for search engines
import Scraping.Scraper_Hotels as sHotelsCom    ## WebScraper for Scrping Hotels.com
import Scraping.Scraper_Booking as sBookingCom  ## WebScraper for Scrping Bookings.com
import Scraping.Scraper_GetaRoom as sGetaroomCom## WebScraper for Scrping GetaRoom.com
import json                                     ## JSON for converting response
import Matcher as HotelMatcher                  ## Hotel Matcher for finding similar hotels and compare

def search(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children):

    # Getting search urls using QueryGenerator

    #Hotels.com search query - this is the url used to get data from hotels.com website
    HotelsComUrl = qg.getHotelscomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children)

    ## WebScraper for Scrping Booking.com - this is the url used to get data from booking.com website
    BookingComUrl = qg.getBookingcomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children)

    ## WebScraper for Scrping Getaroom.com - this is the url used to get data from getaroom.com website
    GetaRoomUrl = qg.getGetaroomcomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children)

    # Scraping and collecting hotel data

    HotelsComArr = sHotelsCom.Scrape(HotelsComUrl)      ## Scraping hotels.com search result and  get results array
    BookingComArr = sBookingCom.Scrape(BookingComUrl)   ## Scraping booking.com search result and  get results array
    GetaroomComArr = sGetaroomCom.Scrape(GetaRoomUrl)   ## Scraping getaroom.com search result and  get results array

    # Combinig results - Adding all results from multiple search engine to one array before matching process
    arrayOfDicArray = [[],[],[]]
    arrayOfDicArray[0]=(HotelsComArr)
    arrayOfDicArray[1]=(BookingComArr)
    arrayOfDicArray[2]=(GetaroomComArr)

    # Comparing hotels
    FinalArray = HotelMatcher.Match(arrayOfDicArray)    # Sending combined results array to Macher to match simmiler hotels for comparing purpose.

    #return arrayOfDicArray
    return json.dumps(FinalArray)                       #Convert final result to JSON and return



    




