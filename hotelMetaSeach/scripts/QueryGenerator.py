

# Generating search url for Hotels.com
def getHotelscomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children):

    #URL='https://www.hotels.com/search.do?&q-destination=Kandy&q-check-in=2019-03-01&q-check-out=2019-03-02&q-rooms=1&q-room-0-adults=2&q-room-0-children=0'

    #Creting string tail including room details with ages which will be added to the url
    members = ''
    for i in range(int(rooms)):
        #If no children no special string tail else create string tail
        if(children=='0'):
            members+= '&q-room-'+str(i)+'-adults=' + adults + '&q-room-'+str(i)+'-children='+children
        else:
            child = ''
            for k in range(int(children)):
                child +=  '&q-room-'+str(i)+'-child-'+str(k)+'-age=10'
            members+= '&q-room-'+str(i)+'-adults=' + adults + '&q-room-'+str(i)+'-children='+children + child

    #Create final url using user inputs
    URL = 'https://uk.hotels.com/search.do?&q-destination=' + search + '&q-check-in=' + checkinyear + '-' +checkinmonth + '-' + checkinday + '&q-check-out=' + checkoutyear + '-' +checkoutmonth + '-' + checkoutday + '&q-rooms=' + rooms + members +'&sort-order=BEST_SELLER'

    return URL




#Generating search url for Booking.com
def getBookingcomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children):

    #URL='https://www.booking.com/searchresults.en-gb.html?ss=colombo&checkin_year=2019&checkin_month=3&checkin_monthday=15&checkout_year=2019&checkout_month=3&checkout_monthday=22&group_adults=2&group_children=1&age=12&no_rooms=1'

    #If child available add age to the url
    if(children=='0'):
        URL = 'https://www.booking.com/searchresults.en-gb.html?ss='+search+'&checkin_year_month_monthday='+checkinyear+'-'+checkinmonth+'-'+ checkinday +'&checkout_year_month_monthday='+checkoutyear+'-'+checkoutmonth+'-'+ checkoutday +'&group_adults='+adults+'&group_children='+children+'&no_rooms='+rooms+'&rows=50&selected_currency=USD&changed_currency=1&top_currency=1&order=class'
    else:
        URL = 'https://www.booking.com/searchresults.en-gb.html?ss=' + search + '&checkin_year_month_monthday=' + checkinyear + '-' + checkinmonth + '-' + checkinday + '&checkout_year_month_monthday=' + checkoutyear + '-' + checkoutmonth + '-' + checkoutday + '&group_adults=' + adults + '&group_children=' + children + '&age=12&&no_rooms=' + rooms + '&rows=50&selected_currency=USD&changed_currency=1&top_currency=1&order=class'

    #Return final url with user inputs
    return URL

#print getBookingcomLink('Kandy','2019','03','15','2019','03','25','2','2','2')


#Generating search url for getaroom.com
def getGetaroomcomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children):

    #Creating room details string with ages of clients stay in the room.
    #Adult - age 18
    #Child - age 0-18
    if(children=="0"):
        roominfo ='[' + '[18],'*int(rooms)
        roominfo = roominfo[0:-1]+']'
    else:
        roominfo = '[' + '[18,10],' * int(rooms)
        roominfo = roominfo[0:-1] + ']'

    #Creating final url with user inputs
    URL = 'https://www.getaroom.com/search?destination='+search+'&page=1&per_page=50&rinfo='+roominfo+'&check_in='+checkinyear+'-'+checkinmonth+'-'+checkinday+'&check_out='+checkoutyear+'-'+checkoutmonth+'-'+checkoutday+'&sort_order=position'

    #return final url
    return URL

##For Testing pupose *******

#print getHotelscomLink("colombo","2019","06","05","2019","06","07","1","1","0")
#print getBookingcomLink("colombo","2019","06","05","2019","06","07","1","1","0")
#print getGetaroomcomLink("colombo","2019","06","05","2019","06","07","1","1","0")
