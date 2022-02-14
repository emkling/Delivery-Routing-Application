import csv
from hash_table import HashTable

# Imports package data through csv file
with open('data/package_data_input.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')

    # Instance of the HashTable class
    hash_table = HashTable()

    # Truck lists for loading packages
    first_truck = []
    second_truck = []
    extra_truck = []

    # Assigns elements from csv file to hash table = O(n)
    for row in read_csv:
        package_id_value = row[0]
        address_value = row[1]
        city_value = row[2]
        state_value = row[3]
        zip_value = row[4]
        delivery_deadline = row[5]
        weight_value = row[6]
        extra_note = row[7]
        truck_number = row[8]
        address_destination = ''
        delivery_start = ''
        status = 'At the Hub'
        time_delivered = ''

        # Loads values into package object
        package = [package_id_value, address_value,
                   city_value, state_value, zip_value,
                   delivery_deadline, weight_value,
                   extra_note, truck_number,
                   address_destination, delivery_start,
                   status, time_delivered]

        # Loads the package on their respective truck
        if '1' in package[8]:
            first_truck.append(package)

        if '2' in package[8]:
            second_truck.append(package)

        if '3' in package[8]:
            extra_truck.append(package)

        # Adds the package to hash_table
        hash_table.add(package_id_value, package)

    # Retrieves list of packages on the first truck = O(1)
    def get_first_truck_packages():
        return first_truck

    # Retrieves list of packages on the second truck = O(1)
    def get_second_truck_packages():
        return second_truck

    # Retrieves list of packages on the extra truck = O(1)
    def get_extra_truck_packages():
        return extra_truck

    # Retrieves the hash table = O(1)
    def get_map():
        return hash_table
