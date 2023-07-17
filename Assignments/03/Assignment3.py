# Leen Said 2220356194
import sys
#string result contains letters from A-Z
result = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
row_indicies = []
for i in result:
    row_indicies.append(i)
# list contans alphabet reversed Z-A
row_indicies = row_indicies[::-1]


input = sys.argv[1]
# read function reads the input from the text file using sys argument
def read():
    f0 = open(input, "r")
    read = f0.readlines()
    return read


#  Function to write the output to the output text file
def export():
    f1 = open("output.txt", "a")
    return f1

# this dictionary contains all the dictionaries that will be created by the program
dictionary_of_dictionares = {}

# fucntion checkkey checks if a key exists in the dictionary
def checkKey(dic, key):
    if key in dic.keys():
        return True
    else:
        return False


def create_category(line):
    e = export()
    # variable command splits the command line by white space
    command = line.split(" ")
    name_category = command[1]
    name_category=name_category.strip()
    # take the dimensions of the dictionary
    command_size = command[2]
    # split the row and column
    command_size = command_size.split("x")
    number_rows = int(command_size[0])
    number_columns = int(command_size[1])
    main_dictionary = {}
    # check if the dictionary to be created already exists in the dictionary of dictionaries
    if checkKey(dictionary_of_dictionares, name_category):
        print("Warning: Cannot create the category for the second time. The stadium has already",name_category,".")
        write_this = ("Warning: Cannot create the category for the second time. The stadium has already",name_category,".\n")
        e.writelines(write_this)
    else:
        # the keys of the dictionary are the letters from row_indicies starting from the end
        keys = row_indicies[-number_rows:]
        values = []
        # create a list(row) with empty seats X
        for k in range(0, number_columns + 1):
            values.append("X")
        # append the lists(rows) to dictionary
        for i in keys:
            main_dictionary[i] = values
        
        # append the new dictionary to the dictionary of dictionaries
        dictionary_of_dictionares[name_category] = main_dictionary
        print("The category '", name_category, "' having 300 seats has been created")
        write_this = ("The category '",name_category,"' having 300 seats has been created\n")
        e.writelines(write_this)

# function to sell tickets
def sell_ticket(line):
    # this function has 4 different if statemnets to check for different situations 
    e = export()
    command = line.split(" ")
    # find number of words in the command line
    num = len(command)
    customer_name = command[1]
    pricing_category = command[2]
    category_name = command[3].strip()
    # import the desired dictionary from dictionary of dictionaries
    dic = dictionary_of_dictionares[category_name]
    # find the number of columns in the dictionary
    for i in dic.values():
        num_columns_in_dic = len(i)
    # create a list which is going to contain the seats to be sold according the command
    list_of_seats = []
    for i in range(num - 4):
        # -4 is because the command line has 3 words before the number of seats starts
        seat = command[i + 4]
        seat=seat.strip()
        list_of_seats.append(seat)
    for element in list_of_seats:
        # check if the seat to be sold is a single seat or a range of seats
        if "-" in element:
            row = element[0]
            # inner is the range of seats
            inner = element[1:]
            indexing = inner.index("-")
            # find lower and upper range of seats
            lower_range = int(inner[0:indexing])
            upper_range = int(inner[indexing + 1 :])
            # make sure that the seats to be sold actually exist
            if upper_range > num_columns_in_dic:
                print("Error: The category ",category_name,"has less column than the specified index ",element)
                write_this =("Error: The category ",category_name," has less column than the specified index ",element,"\n")
                e.writelines(write_this)

            # if all the seats in range exist, sell according to specified pricing category    
            else:
                # make the sure the seat is already empty
                if dic[row][lower_range : upper_range + 1] == "X":
                    templist = dic[row]
                    if pricing_category == "full":
                        for i in range(lower_range, upper_range + 1):
                            templist[i] = "F"
                    elif pricing_category == "student":
                        for i in range(lower_range, upper_range + 1):
                            templist[i] = "S"
                    else:
                        for i in range(lower_range, upper_range + 1):
                            templist[i] = "G"

                    print("Success: ",customer_name," has bought ",seat," at ",category_name)
                    write_this = ("Success: ",customer_name," has bought ",seat," at ",category_name,"\n")
                    e.writelines(write_this)
                
                # if the seat isn't already empty
                else:
                    print("Warning: The seat ",seat," cannot be sold to ",customer_name," since it was already sold!")
                    write_this = ("Warning: The seat ",seat," cannot be sold to ",customer_name," since it was already sold!\n")
                    e.writelines(write_this)
        
        # if the seat to be sold is NOT a range
        else:
            row = element[0]
            column = int(element[1:])
            # check if the seat to be sold exists in the dictionary
            if column > num_columns_in_dic:
                print("Error: The category ",category_name," has less column than the specified index ",element)
                write_this = ("Error: The category ",category_name," has less column than the specified index ",element,"\n")
                e.writelines(write_this)
            else:
                # check if the seat is already empty
                if dic[row][column] == "X":
                    # templist is a list that contains the elements of a row in the dictionary
                    templist = dic[row]
                    if pricing_category == "full":
                        # locate the seat in the row and change its value accordingly
                        templist[column] = "F"
                    elif pricing_category == "student":
                        templist[column] = "S"
                    else:
                        templist[column] = "G"
                    print("Success:",customer_name,"has bought",seat,"at",category_name)
                    write_this = ("Success: ",customer_name," has bought ",seat," at ",category_name,"\n")
                    e.writelines(write_this)
                
                # if the seat isn't already empty
                else:
                    print("Warning: The seat ",seat," cannot be sold to ",customer_name," since it was already sold!")
                    write_this = ("Warning: The seat ",seat," cannot be sold to ",customer_name," since it was already sold!\n",)
                    e.writelines(write_this)


def cancel_ticket(line):
    # This function has 4 if statements to check for different situations
    e = export()
    command = line.split(" ")
    num = len(command)
    category_name = command[1].strip()
    list_of_seats = []
    dic = dictionary_of_dictionares[category_name]
    for i in dic.values():
        num_columns_in_dic = len(i)
    for i in range(num - 2):
        # -2 is because the command line has 2 words before the number of seats start
        seat = command[i + 2]
        seat=seat.strip()
        list_of_seats.append(seat)
        for element in list_of_seats:
            if "-" in element:
                row = element[0]
                inner = element[1:]
                indexing = inner.index("-")
                lower_range = int(inner[0:indexing])
                upper_range = int(inner[indexing + 1 :])
                if upper_range > num_columns_in_dic:
                    print("Error: The category ",category_name,"has less column than the specified index ",element)
                    write_this =("Error: The category ",category_name," has less column than the specified index ",element,"\n")
                else:
                    # check if the seat is already full
                    if dic[row][lower_range : upper_range + 1] == "X":
                        print("Error: The seat ",seat," at ",category_name," has already been free! Nothing to cancel")
                        write_this = ("Error: The seat ",seat," at ",category_name," has already been free! Nothing to cancel\n")
                        e.writelines(write_this)

                    # if the seat was full make it empty
                    else:
                        dic[row][lower_range, upper_range + 1] = "X"
                        print("Success: The seat ",seat," at ",category_name," has been canceled and now ready to sell again")
                        write_this = ("Success: The seat ",seat," at ",category_name," has been canceled and now ready to sell again\n")
                        e.writelines(write_this)

            else:
                row = element[0]
                column = int(element[1:])
                if column > num_columns_in_dic:
                    print("Error: The category ",category_name," has less column than the specified index ",element)
                    write_this=("Error: The category ",category_name," has less column than the specified index ",element,"\n")
                    e.writelines(write_this)
                else:
                    if dic[row][column] == "X":
                        print("Error: The seat ",seat," at",category_name," has already been free! Nothing to cancel")
                        write_this = ("Error: The seat ",seat," at ",category_name," has already been free! Nothing to cancel\n")
                        e.writelines(write_this)
                    else:
                        dic[row][column] = "X"
                        print("Success: The seat ",seat," at ",category_name," has been canceled and now ready to sell again")
                        write_this = ("Success: The seat ",seat," at ",category_name," has been canceled and now ready to sell again\n")
                        e.writelines(write_this)


def balance(line):
    e = export()
    command = line.split(" ")
    category_name = command[1]
    list_values = []
    students_sum = 0
    full_sum = 0
    season_sum = 0
    # locate the required cateogory 
    dic=dictionary_of_dictionares[category_name[:-1]]
    # put the dictionary values in a list
    for i in dic.values():
        list_values.append(i)
    # check for S, F,and G in the list
    for k in list_values:
        count_student = k.count("S")
        students_sum += count_student
        count_full = k.count("F")
        full_sum += count_full
        count_season = k.count("G")
        season_sum += count_season
    # calculate the revenue
    revenue = (students_sum * 10) + (full_sum * 20) + (season_sum * 250)
    print("Category report of ",category_name,"\n--------------------------------\nSum of students =",students_sum,", Sum of full pay =",full_sum,", Sum of season ticket=",season_sum,", and Revenues =",revenue,"Dollars")
    write_this = ("Category report of ",str(category_name),"\n--------------------------------\nSum of students =",str(students_sum),", Sum of full pay =",str(full_sum),", Sum of season ticket=",str(season_sum),", and Revenues =",str(revenue),"Dollars\n")
    e.writelines(write_this)


def showcategory(line):
    e=export()
    command = line.split(" ")
    category_name = command[1]
    print("Printing category layout of ", category_name)
    dic=dictionary_of_dictionares[category_name[:-1]]
    list_of_columns=[]
    for i in dic.values():
        num_columns = len(i)
        # for q in range(11,len(i)):
        #     i[q] = " "+i[q]
    for key, value in dic.items():
        print(key, *value)
        write_this=(key,"\t")
        e.writelines(write_this)
        write_this=(*value,'\t')
        e.writelines(write_this)
        write_this="\n"
        e.writelines(write_this)
    print("  ",end='')
    write_this=" ",'\t'
    e.writelines(write_this)
    for f in range(num_columns):
        list_of_columns.append(f)
    for c in list_of_columns:
        print(c,end=' ')
        write_this=(str(c),'\t')
        e.writelines(write_this)
    print('\n')

# for statement to read the lines
for lines in read():
    if lines.startswith("CREATECATEGORY"):
        create_category(lines)
    elif lines.startswith("SELLTICKET"):
        sell_ticket(lines)
    elif lines.startswith("CANCELTICKET"):
        cancel_ticket(lines)
    elif lines.startswith("BALANCE"):
        balance(lines)
    elif lines.startswith("SHOWCATEGORY"):
        showcategory(lines)