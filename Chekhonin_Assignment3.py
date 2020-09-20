import sys, csv


companiesList = []

"""Executes function according to choosen option.
      Args:11
          action: The option number.
      Returns:
          Output from choosen function.
    """
def main():
    while(True):
        printHeader()
        option = promptInput()
        if (option == 1):
            # downloadFiles()
            exportFiles()
        elif(option == 2):
            searchBySymbolinput()
        elif (option ==3):
            display15Companies()
        elif (option ==4):
            terminate()
            
"""Load data from 3 existing files, merge and sort by symbol"""
def exportFiles():
    
    files = ['NASDAQ.csv','NYSE.csv' ,'AMEX.csv']
    
    for file in files:
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                companiesList.append(row)
                line_count += 1
          
    companiesList.sort(key = lambda i: i['Symbol'])
    print(f'\t Total number of companies is {len(companiesList)}')
    keys= companiesList[0].keys()    

    with open('Chekhonin_Assignment3_out.csv', 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(companiesList)
  
"""Download files from URL"""
# TODO: does not download      
# =============================================================================
# def downloadFiles():
#     csv_url = 'https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download'
#     req = requests. get(csv_url)
#     url_content = req.content
#     csv_file = open('NASDAQ.csv', 'wb')
#     csv_file. write(url_content)
#     csv_file. close()
# =============================================================================

"""Ask user to enter company stock symbol to display associated info"""
def searchBySymbolinput():
    isValidInput=False
    while isValidInput==False:
        symbol = input("Enter company stock sybol to fetch info (enter $E for exit):\n")
        
        if (symbol== "$E"):
            break
        res = searchBySymbol(symbol)
        if(res==None):
            print("No such company in list")
        else:
            print(f'Company info {res[0]["Symbol"]} {res[0]["Name"]},LastSale on {res[0]["LastSale"]},MarketCap: {res[0]["MarketCap"]}, IPOyear: {res[0]["IPOyear"]},Sector: {res[0]["Sector"]} , industry: {res[0]["industry"]}')

"""Search existing [] by symbol, then display associated info
        Returns:
            [] with associated info about company
"""
def searchBySymbol(a: str()):
    res = list(filter(lambda i: i['Symbol'] == a, companiesList))
    return res

"""Filters existing [] by MarketCap and displays it """
def display15Companies():
    res = list(filter(lambda i: i['MarketCap'] != "n/a", companiesList))
    res.sort(reverse=True,key = lambda x: x['MarketCap'])
    for i in range(1,16):
        print(f'{i}. {res[i]["Symbol"]} {res[i]["Name"]},LastSale on {res[i]["LastSale"]},MarketCap: {res[i]["MarketCap"]}, IPOyear: {res[i]["IPOyear"]},Sector: {res[i]["Sector"]} , industry: {res[i]["industry"]}')

"""Terminates the application"""
def terminate():
    sys.exit()

"""Asks user to choose option.
      Returns:
          Choosen option.
"""
def promptInput():
    
    isValidInput=False
    while isValidInput==False:
        option = input("Waiting for your option:\n")
        option = int(option)
        if option>=1 and option <=4 and type(option)==int:
            isValidInput = True
        else:
            print("Wrong option!")
    return option


"""Prints header to console"""
def printHeader():
    mes = "Chekhonin’s CompanyList Data Analyzer:"
    mes2 = "----------------------------------------"
    print("=====================================================")
    print(mes.center(53))
    print("=====================================================")
    print("1. Export to merged/sorted(by stock symbol) CSV file")
    print("2. Search by stock symbol")
    print("3. Display 15 companies with the highest MarketCap value")
    print("4. Exit")
    print("   "+mes2)
    print("   Please choose one of the above:")


"""If file imported then main will not executed"""
if __name__=='__main__':
    main()