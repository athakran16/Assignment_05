#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Arti Thakran, 2021-Nov-12, Created File
#------------------------------------------#

# Declare variabls
strChoice = '' # User input
DictTbl = {}  # list of lists to hold data

# TODO replace list of lists with list of dicts
DictRow = {} 
strFileName = 'CDInventory.txt' 
objFile = None 
lstTbl=[]
lstrow = []
strrow = ''


# Get user Input
print('The Magic CD Inventory\n')
while True:

    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for strrow in objFile:
               lstRow = strrow.strip().split(',')
               DictRow = {'ID': int(lstRow[0]), 'CD title': lstRow[1], 'Artist Name': lstRow[2]}
               print(DictRow)
               print()
               lstTbl.append(DictRow)
        objFile.close()

      
    elif strChoice == 'a': 
        # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        DictRow = {'id':intID, 'title': strTitle,'artist': strArtist}
        lstTbl.append(DictRow)
        
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
       print('ID, CD Title, Artist')
       for strrow in lstTbl:
           print(*strrow.values(), sep = ', ')
           
            
    elif strChoice == 'd':
    # TODO Add functionality of deleting an entry
    # Read from file into memory
        
        strdelid = input('Enter ID that needs to be deleted:')
        objFile = open(strFileName ,'r+')
        for row in lstTbl:
            if row['ID'] == int(strdelid):
                print('found it')
                lstTbl.remove(row)
                print('id deleted'+'\n')    
        objFile.close()       

    elif strChoice == 's':
    # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            for key,val in row.items():
                strrow =  strrow + str(val) + ','
            strrow = strrow[:-1] + '\n'
        objFile.write(strrow)
        print(strrow)
        objFile.close()
 
    else:
    # Choose a valid option
        print('Please choose either l, a, i, d, s or x!')

