from fuzzywuzzy import process      # FuzzyWuzzy For string comparing

#Method to find matching results from array of arrays of hotel data dictionaries
#Arg is a Array including arrays which include hotel data dictionaries
def Match(arrayOfDicArray):


    arrayOfDicArray.sort(key=len, reverse=True)                 # Sort the array according to the length of the element arrays

    TitleArray = []                                             #Create an empty array to hold arrays of hotel titles
    for dicArray in arrayOfDicArray:
        TitleArray.append([d['title'] for d in dicArray])       # Extract titles from hotel data and add them to Title array
    #res = ''       #For testing hotel matching pairs



    nameArray = []              #names of found hotel pairs will used to check whether pair is alredy found if third match is found
    nameIndexArray = []         #Array of Arrays which keeps index of hotel dictionary
                                #For each name in the NameArray here we keep a array that has length of number of arrays in the arrayOfDicArray
                                # or in other ways the number of scraped websites. Initially it will be filled with 'x' and later replace
                                # with the index of the array that has a match

    for i in range(len(TitleArray) - 1):                        # Get one array by array from arrayOfDicArray
        for r in range(i + 1, len(TitleArray)):                 # Compare with each arrays after the selected array
            for k in range(len(TitleArray[i])):                 # Go through each element of the selected array
                title = TitleArray[i][k]                        # select a Title from the selected array
                ans = (process.extractOne(title, TitleArray[r]))# Find the best match in arrays next to it
                if (ans != None):
                    if (ans[1] > 89):                           #If matching score higher than 89% select
                        #res += title + " ==>  " + ans[0] + "\n"    #For testing hotel matching pairs

                        if ((title in nameArray) or (ans[0] in nameArray)):     #Check  whether name already in nameArray
                            if (title in nameArray):
                                indx = nameArray.index(title)                   #If yes find the index of the title
                            if (ans[0] in nameArray):
                                indx = nameArray.index(ans[0])                  #If yes find the index of the title
                            indArr = nameIndexArray[indx]                       # Get respective array from indArr
                            indArr[i] = k                                       # add the found pair's parent array index to indArr
                            indArr[r] = TitleArray[r].index(ans[0])             # add the found pair's parent array index to indArr
                            nameIndexArray[indx] = indArr                       #Replace the cuurent array from indArr with new one

                        else:                                                   # If not found already
                            nameArray.append(title)                             # add the name to nameArray
                            indArr = ['x'] * len(TitleArray)                    # create a indArr which filled with 'x'
                            indArr[i] = k                                       # add dictionary index to indarr
                            indArr[r] = TitleArray[r].index(ans[0])             # add dictionary index to indarr of the other match
                            nameIndexArray.append(indArr)                       # add indArr to nameIndexArray

    MultiDicArray = []                      #Create a empty array to hold results with comparable data

    for arr in nameIndexArray:              # For each index array in nameIndexArray
        title = ''
        link = []
        address = ''
        imageUrl = ''
        price = []
        origin = []
        for e in range(len(arr)):           # for each index
            el = arr[e]
            if (el != 'x'):                 # if index not 'x' get matching hotel data dictionaries and bind them together
                if (title == ''):
                    title = arrayOfDicArray[e][el]['title']
                link.append(arrayOfDicArray[e][el]['link'])
                if (address == ''):
                    address = arrayOfDicArray[e][el]['address']
                if (imageUrl == ''):
                    imageUrl = arrayOfDicArray[e][el]['imageUrl']
                price.append(arrayOfDicArray[e][el]['price'])
                origin.append(arrayOfDicArray[e][el]['origin'])

        DataDic = {                         # Create a new dictionary with comparable data
            "title": title,
            "link": link,
            "address": address,
            "imageUrl": imageUrl,
            "price": price,
            "origin": origin
        }
        MultiDicArray.append(DataDic)       #Add dictionary to the MultiDicArray

    FinalArray = []                         # Create an empty array to hold all results
    FinalArray += MultiDicArray             # Firstly add rsults with multiple data
    for darr in arrayOfDicArray:            # Then add all the single search results
        FinalArray += darr

    return  FinalArray                      # Return the array containing all search results
