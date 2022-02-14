import csv
import datetime

# Imports address data through a csv file
with open('./Data/AddressData.csv') as address_file:
    address_csv = csv.reader(address_file, delimiter=',')
    address_csv = list(address_csv)

# Imports distance data through a csv file
with open('./Data/DistanceData.csv', encoding='utf-8-sig') as distance_file:
    distance_csv = (csv.reader(distance_file, delimiter=','))
    distance_csv = list(distance_csv)


# Retrieves the distance values given a row and column = 0(1)
def get_distance(row, column):
    value = distance_csv[row][column]
    if value == '':
        return float(distance_csv[column][row])

    else:
        return float(value)


# Retrieves the address value given a row and column = O(1)
def get_address(row, column):
    address = address_csv[row][column]

    return address
