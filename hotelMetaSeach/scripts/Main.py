
import QueryGenerator as qg
import Scraping.Scraper_Hotels as sHotelsCom
import Scraping.Scraper_Booking as sBookingCom
import Scraping.Scraper_GetaRoom as sGetaroomCom
import json
from fuzzywuzzy import process

def search(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children):

    # Getting search urls using QueryGenerator
    
    HotelsComUrl = qg.getHotelscomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children)

    BookingComUrl = qg.getBookingcomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children)

    GetaRoomUrl = qg.getGetaroomcomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children)
    # Scraping and collecting hotel data

    HotelsComArr = sHotelsCom.Scrape(HotelsComUrl)
    BookingComArr = sBookingCom.Scrape(BookingComUrl)
    GetaroomComArr = sGetaroomCom.Scrape(GetaRoomUrl)

    # Combinig results

    CombinedResults = HotelsComArr + BookingComArr + GetaroomComArr

    # Execute Filtering and Ranking 
    #TODO
    FinalResults = CombinedResults
    arrayOfDicArray = []
    arrayOfDicArray.append(HotelsComArr)
    arrayOfDicArray.append(BookingComArr)
    arrayOfDicArray.append(GetaroomComArr)

    arrayOfDicArray.sort(key=len, reverse=True)

    TitleArray = []
    for dicArray in arrayOfDicArray:
        TitleArray.append([d['title'] for d in dicArray])
    # TitleArray=[['a','b','c'],['d','e','f'],['a','d','t'],['k','l','t']]
    res = ''

    indexArr = []

    nameArray = []
    nameIndexArray = []

    for i in range(len(TitleArray) - 1):
        for r in range(i + 1, len(TitleArray)):
            for k in range(len(TitleArray[i])):
                title = TitleArray[i][k]
                ans = (process.extractOne(title, TitleArray[r]))
                if (ans[1] > 89):
                    res += title + " ==>  " + ans[0] + "\n"

                    if ((title in nameArray) or (ans[0] in nameArray)):
                        if (title in nameArray):
                            indx = nameArray.index(title)
                        if (ans[0] in nameArray):
                            indx = nameArray.index(ans[0])
                        indArr = nameIndexArray[indx]
                        indArr[i] = k
                        indArr[r] = TitleArray[r].index(ans[0])
                        nameIndexArray[indx] = indArr

                    else:
                        nameArray.append(title)
                        indArr = ['x'] * len(TitleArray)
                        indArr[i] = k
                        indArr[r] = TitleArray[r].index(ans[0])
                        nameIndexArray.append(indArr)

    MultiDicArray = []

    for arr in nameIndexArray:
        title = ''
        link = []
        address = ''
        imageUrl = ''
        price = []
        origin = []
        for e in range(len(arr)):
            el = arr[e]
            if (el != 'x'):
                if (title == ''):
                    title = arrayOfDicArray[e][el]['title']
                link.append(arrayOfDicArray[e][el]['link'])
                if (address == ''):
                    address = arrayOfDicArray[e][el]['address']
                if (imageUrl == ''):
                    imageUrl = arrayOfDicArray[e][el]['imageUrl']
                price.append(arrayOfDicArray[e][el]['price'])
                origin.append(arrayOfDicArray[e][el]['origin'])
         

        DataDic = {
            "title": title,
            "link": link,
            "address": address,
            "imageUrl": imageUrl,
            "price": price,
            "origin": origin
        }
        MultiDicArray.append(DataDic)

    FinalArray = []
    FinalArray += MultiDicArray
    for darr in arrayOfDicArray:
        FinalArray += darr



    #Return Final Results
    #return json.dumps(FinalResults)
    return json.dumps(FinalArray)


#search('Kandy','2019','03','15','2019','03','25','2','2','2')


    




