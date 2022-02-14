from DistanceData import get_distance

# First truck lists used for storing sorted data
sorted_first_truck_packages = []
first_truck_route = [0]

# Second truck lists used for storing sorted data
sorted_second_truck_packages = []
second_truck_route = [0]

# Extra truck lists used for storing sorted data
sorted_extra_truck_packages = []
extra_truck_route = [0]


# Greedy Algorithm
def set_delivery_route(package_address_list, current_address, truck_designator):
    shortest_distance = 20
    next_address = 0

    # Halts the function and returns an empty list when all packages have been sorted
    if len(package_address_list) == 0:
        return package_address_list

    # Finds the next closest location available from the package list
    for index in package_address_list:
        package_address = int(index[9])
        if get_distance(current_address, package_address) <= shortest_distance:
            shortest_distance = get_distance(current_address, package_address)
            next_address = package_address

    # Determines what truck list the package is sorted into
    for index in package_address_list:
        if get_distance(current_address, int(index[9])) == shortest_distance:

            if truck_designator == 1:
                sorted_first_truck_packages.append(index)  # Copies all package data to its respective sorted list
                first_truck_route.append(index[9])  # Copies only the location order to its respective sorted list
                package_address_list.pop(package_address_list.index(index))
                set_delivery_route(package_address_list, next_address, 1)

            elif truck_designator == 2:
                sorted_second_truck_packages.append(index)  # Copies all package data to its respective sorted list
                second_truck_route.append(index[9])  # Copies only the location order to its respective sorted list
                package_address_list.pop(package_address_list.index(index))
                set_delivery_route(package_address_list, next_address, 2)

            elif truck_designator == 3:
                sorted_extra_truck_packages.append(index)  # Copies all package data to its respective sorted list
                extra_truck_route.append(index[9])  # Copies only the location order to its respective sorted list
                package_address_list.pop(package_address_list.index(index))
                set_delivery_route(package_address_list, next_address, 3)


# Retrieves a list of sorted packages within the first truck = O(1)
def get_first_truck_sorted():
    return sorted_first_truck_packages


# Retrieves the first truck's delivery order = O(1)
def get_first_truck_route():
    return first_truck_route


# Retrieves a list of sorted packages within the second truck = O(1)
def get_second_truck_sorted():
    return sorted_second_truck_packages


# Retrieves the second truck's delivery order = O(1)
def get_second_truck_route():
    return second_truck_route


# Retrieves a list of sorted packages within the extra truck = O(1)
def get_extra_truck_sorted():
    return sorted_extra_truck_packages


# Retrieves the extra truck's delivery order = O(1)
def get_extra_truck_route():
    return extra_truck_route
