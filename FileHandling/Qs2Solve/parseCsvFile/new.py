#parse the csv file into a dictionary in a format you like

#---------------------------------------------------------------------#
def parsingCsv(filename,saveToFileName):
    with open(filename,"r") as CsvFile:
        #get the header first & save to array
        header = next(CsvFile).strip().split(",")
        #now put the header with the respective detail i.e after 1st line
        details_dict = {}
        for idx,eachLine in enumerate(CsvFile,start=1):
            #put each lines words seperate by ,
            eachWordArray = eachLine.strip().split(",")
            #put now in a way that each value matches with header i.e
            #then put to dictionary
            details_dict[idx]=dict(zip(header,eachWordArray)) #understand this from chatgpt
            """
            zip(keys, values) pairs the elements of keys and values into tuples:
            i.e
			[('name', 'Alice'), ('age', 25), ('city', 'New York')]
			dict()-> converts these tuples into key-value pairs in a dictionary.

"""
        #now New function -
        save_to_File(details_dict,saveToFileName)
def save_to_File(details_dict,saveToFileName):
    with open(saveToFileName,"a") as newFile:
        newFile.write(f"{details_dict}\n")
        newFile.write("Formated Values\n---------------\n")
        for key,value in details_dict.items():
            newFile.write(f"{key} - {value}\n")
parsingCsv('details.csv','myNewDetails.txt')