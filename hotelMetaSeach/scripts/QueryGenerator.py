


def getHotelscomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children):

    #URL='https://www.hotels.com/search.do?&q-destination=Kandy&q-check-in=2019-03-01&q-check-out=2019-03-02&q-rooms=1&q-room-0-adults=2&q-room-0-children=0'

    members = ''
    for i in range(int(rooms)):
        if(children=='0'):
            members+= '&q-room-'+str(i)+'-adults=' + adults + '&q-room-'+str(i)+'-children='+children
        else:
            child = ''
            for k in range(int(children)):
                child +=  '&q-room-'+str(i)+'-child-'+str(k)+'-age=10'
            members+= '&q-room-'+str(i)+'-adults=' + adults + '&q-room-'+str(i)+'-children='+children + child

    
    URL = 'https://uk.hotels.com/search.do?&q-destination=' + search + '&q-check-in=' + checkinyear + '-' +checkinmonth + '-' + checkinday + '&q-check-out=' + checkoutyear + '-' +checkoutmonth + '-' + checkoutday + '&q-rooms=' + rooms + members +'&sort-order=BEST_SELLER'

    return URL


def getBookingcomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children):

    #URL='https://www.booking.com/searchresults.en-gb.html?ss=colombo&checkin_year=2019&checkin_month=3&checkin_monthday=15&checkout_year=2019&checkout_month=3&checkout_monthday=22&group_adults=2&group_children=1&age=12&no_rooms=1'

    if(children=='0'):
        URL = 'https://www.booking.com/searchresults.en-gb.html?ss='+search+'&checkin_year_month_monthday='+checkinyear+'-'+checkinmonth+'-'+ checkinday +'&checkout_year_month_monthday='+checkoutyear+'-'+checkoutmonth+'-'+ checkoutday +'&group_adults='+adults+'&group_children='+children+'&no_rooms='+rooms+'&rows=50&selected_currency=USD&changed_currency=1&top_currency=1&order=class'
    else:
        URL = 'https://www.booking.com/searchresults.en-gb.html?ss=' + search + '&checkin_year_month_monthday=' + checkinyear + '-' + checkinmonth + '-' + checkinday + '&checkout_year_month_monthday=' + checkoutyear + '-' + checkoutmonth + '-' + checkoutday + '&group_adults=' + adults + '&group_children=' + children + '&age=12&&no_rooms=' + rooms + '&rows=50&selected_currency=USD&changed_currency=1&top_currency=1&order=class'
    return URL

#print getBookingcomLink('Kandy','2019','03','15','2019','03','25','2','2','2')


def getGetaroomcomLink(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children):

    if(children=="0"):
        roominfo ='[' + '[18],'*int(rooms)
        roominfo = roominfo[0:-1]+']'
    else:
        roominfo = '[' + '[18,10],' * int(rooms)
        roominfo = roominfo[0:-1] + ']'

    URL = 'https://www.getaroom.com/search?destination='+search+'&page=1&per_page=50&rinfo='+roominfo+'&check_in='+checkinyear+'-'+checkinmonth+'-'+checkinday+'&check_out='+checkoutyear+'-'+checkoutmonth+'-'+checkoutday+'&sort_order=position'
    return URL

print getHotelscomLink("colombo","2019","06","05","2019","06","07","1","1","0")
print getBookingcomLink("colombo","2019","06","05","2019","06","07","1","1","0")
print getGetaroomcomLink("colombo","2019","06","05","2019","06","07","1","1","0")
