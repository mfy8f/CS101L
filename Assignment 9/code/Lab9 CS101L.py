import csv
#list of dates in the month set as a dict

month_lst = {'1':'Jan', '2':'Feb', '3':'March', '4':'April', '5':'May', '6':'June', '7':'July', '8':'Aug', '9':'September',
'10':'October', '11':'November', '12':'December'}

#temp lists and dicts
list1 = []
temp_dict = {}
temp_dict2 = {}
temp_dict3 = {}
temp_dict4 = {}

def month_from_number(month):
    #use a while loop to loop until correct
    while True:
        try:
            #check to see if month is correct
            if month < 1 or month > 12: 
                print('please input a number that is between 1 and 12')
                continue
            else:
                return month_lst(str[month])
        except:
            pass

def read_in_file(user_input_file):
    try:
        #open file and read it
        with open(user_input_file,'r', encoding='UTF-8') as open_file:
            #use csv.reader to read open_file
            read = csv.reader(open_file)
            #added each value to a list
            for value in read:
                list1.append(value)
            #close file
            open_file.close()
        return list1
    except FileNotFoundError:
        pass

def create_offense_dict(user_file_list: list):
    #grab line 7 from each line
    for line in user_file_list[1:]:
        #strip line 7
        offense = line[7].strip()
        temp_dict[offense] = temp_dict.get(offense, 0) + 1 
    #return the dict for offenses
    return temp_dict

def create_offense_by_zip(zip_file):
    #read through each line and take value and add it to the dict.
    for value in zip_file[1:]:
        #isolate values 13 and 7
        zip_code = value[13]
        offense = value[7]
        #filter out incorrect enteries in the dict
        if offense not in temp_dict2:
            temp_dict2[offense] = {}
        #add both values into a new dict
        temp_dict2[offense][zip_code] = temp_dict2[offense].get(zip_code,0) +1
    return temp_dict2


def create_reported_month_dict(user_file: list): 
    #create and return a dictionary with month value
    for value in user_file[1:]:
        offense = value[1][0:2]
        if offense in temp_dict3:
            temp_dict3[offense] += 1
        return temp_dict3


if __name__=="__main__":
    invalid_file = True
    while invalid_file == True:
        try:
            file_name = input("Enter the name of the crime data file ==>  ")
            lst = read_in_file(file_name)
            print(lst)
            invalid_file = False
        except FileNotFoundError:
            print("Could not find the file specified. {} not found".format(file_name))

    print()
    months = create_reported_month_dict(lst)
    offense_by_zip = create_offense_by_zip(lst)

    print()
    invalid_key = True
    while invalid_key:
        offense_key = input('Enter an offense')
        if offense_key in offense_by_zip:
            invalid_key = False
        else:
            print("Not a valid offense found, please try again")
    print()

    print("{} offenses by Zip Code".format(offense_key))
    print("{:20}{:10}".format("Zip Code", "# Offenses"))
    print("="*30)
    a = offense_by_zip[offense_key].items()
    for key,value in a:
        print("{:20}{:>10}".format(key, value))

temp_dict.clear
temp_dict2.clear
temp_dict3.clear