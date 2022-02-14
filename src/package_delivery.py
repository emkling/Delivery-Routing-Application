import datetime
import distance_algorithm
import distance_data
import package_data
import time_simulator

# Truck lists used for storing sorted packages
first_truck = []
second_truck = []
extra_truck = []


# Assigns departure times to all three trucks
def assign_departure_times():
    # Designates the departure times for the first truck = O(n)
    for index, j in enumerate(package_data.get_first_truck_packages()):
        package_data.get_first_truck_packages()[index][10] = time_simulator.get_first_truck_departure()[0]
        first_truck.append(package_data.get_first_truck_packages()[index])

    # Designates the departure times for the second truck = O(n)
    for index, j in enumerate(package_data.get_second_truck_packages()):
        package_data.get_second_truck_packages()[index][10] = time_simulator.get_second_truck_departure()[0]
        second_truck.append(package_data.get_second_truck_packages()[index])

    # Designates the departure times for the extra truck = O(n^2)
    for index, j in enumerate(package_data.get_extra_truck_packages()):
        package_data.get_extra_truck_packages()[index][10] = time_simulator.get_extra_truck_departure()[0]
        extra_truck.append(package_data.get_extra_truck_packages()[index])


# Compares addresses of all three trucks with address book
def assign_package_addresses():
    # Adds the address designator to the first truck deliveries = O(n^2)
    for index in range(len(package_data.get_first_truck_packages())):
        for j in range(len(distance_data.address_csv)):
            if distance_data.get_address(j, 2) == package_data.get_first_truck_packages()[index][1]:
                first_truck[index][9] = distance_data.get_address(j, 0)

    # Adds the address designator to the second truck deliveries list = O(n^2)
    for index in range(len(package_data.get_second_truck_packages())):
        for j in range(len(distance_data.address_csv)):
            if distance_data.get_address(j, 2) == package_data.get_second_truck_packages()[index][1]:
                second_truck[index][9] = distance_data.get_address(j, 0)

    # Adds the address designator to the extra truck deliveries list = O(n^2)
    for index in range(len(package_data.get_extra_truck_packages())):
        for j in range(len(distance_data.address_csv)):
            if distance_data.get_address(j, 2) == package_data.get_extra_truck_packages()[index][1]:
                extra_truck[index][9] = distance_data.get_address(j, 0)


# Assigns all three trucks with optimal paths
def assign_optimal_path():
    # Finds an optimal path for the deliveries in truck one
    distance_algorithm.set_delivery_route(first_truck, 0, 1)

    # Finds an optimal path for the deliveries in truck two
    distance_algorithm.set_delivery_route(second_truck, 0, 2)

    # Finds an optimal path for the deliveries in the extra truck
    distance_algorithm.set_delivery_route(extra_truck, 0, 3)


def calculate_total_distance():
    first_truck_mileage = 0.0
    second_truck_mileage = 0.0
    extra_truck_mileage = 0.0
    # Calculates the total distance for truck one = O(n)
    for index in range(len(distance_algorithm.get_first_truck_route())):
        if index < len(distance_algorithm.get_first_truck_route()) - 1:
            first_truck_mileage += distance_data.get_distance(
                int(distance_algorithm.get_first_truck_route()[index]),
                int(distance_algorithm.get_first_truck_route()[index + 1]))

    # Calculates the total distance for truck two = O(n)
    for index in range(len(distance_algorithm.get_second_truck_route())):
        if index < len(distance_algorithm.get_second_truck_route()) - 1:
            second_truck_mileage = second_truck_mileage + distance_data.get_distance(
                int(distance_algorithm.get_second_truck_route()[index]),
                int(distance_algorithm.get_second_truck_route()[index + 1]))

    # Calculates the total distance for the extra truck = O(n)
    for index in range(len(distance_algorithm.get_extra_truck_route())):
        if index < len(distance_algorithm.get_extra_truck_route()) - 1:
            extra_truck_mileage = extra_truck_mileage + distance_data.get_distance(
                int(distance_algorithm.get_extra_truck_route()[index]),
                int(distance_algorithm.get_extra_truck_route()[index + 1]))

    # Adds the mileage of all three trucks together = O(1)
    overall_mileage = first_truck_mileage + second_truck_mileage + extra_truck_mileage

    return overall_mileage


# Designates delivery times for all packages
def assign_package_times():
    # Designates delivery statuses and times for packages delivered by truck one = O(n)
    for index in range(len(distance_algorithm.get_first_truck_route())):
        if index < len(distance_algorithm.get_first_truck_route()) - 1:
            delivery_time = time_simulator.get_current_time(
                distance_data.get_distance(int(distance_algorithm.get_first_truck_route()[index]),
                                          int(distance_algorithm.get_first_truck_route()[index + 1])),
                time_simulator.get_first_truck_departure())

            distance_algorithm.get_first_truck_sorted()[index][11] = "Delivered"  # status of truck
            distance_algorithm.get_first_truck_sorted()[index][12] = delivery_time  # time delivery was made

    # Designates delivery statuses and times for packages delivered by the second truck = O(n)
    for index in range(len(distance_algorithm.get_second_truck_route())):
        if index < len(distance_algorithm.get_second_truck_route()) - 1:
            delivery_time = time_simulator.get_current_time(
                distance_data.get_distance(int(distance_algorithm.get_second_truck_route()[index]),
                                          int(distance_algorithm.get_second_truck_route()[index + 1])),
                time_simulator.get_second_truck_departure())

            distance_algorithm.get_second_truck_sorted()[index][11] = "Delivered" # status of truck
            distance_algorithm.get_second_truck_sorted()[index][12] = delivery_time # time delivery was made

    # Designates delivery statuses and times for packages delivered by the extra truck O(n)
    for index in range(len(distance_algorithm.get_extra_truck_route())):
        if index < len(distance_algorithm.get_extra_truck_route()) - 1:
            delivery_time = time_simulator.get_current_time(
                distance_data.get_distance(int(distance_algorithm.get_extra_truck_route()[index]),
                                          int(distance_algorithm.get_extra_truck_route()[index + 1])),
                time_simulator.get_extra_truck_departure())

            distance_algorithm.get_extra_truck_sorted()[index][11] = "Delivered" # status of truck
            distance_algorithm.get_extra_truck_sorted()[index][12] = delivery_time # time delivery was made


# Outputs all the deliveries made by each truck
def view_deliveries(selection):
    update_delivery_information()

    # Cycles through and prints deliveries carried out by the first truck = O(n)
    if selection == 1:
        print("First Truck Packages:")
        for index in distance_algorithm.get_first_truck_sorted():
            print(
                "Package ID " + index[0] + "\t\t Status: " + index[11] + "\t\t Deadline: " + index[5]
                + "\t\t" + "Time Delivered: " + str(index[12]) + "\t\t Special Notes: " + index[7])

    # Cycles through and prints deliveries carried out by the second truck = O(n)
    if selection == 2:
        print("\nSecond Truck Packages:")
        for index in distance_algorithm.get_second_truck_sorted():
            print(
                "Package ID " + index[0] + "\t\t Status: " + index[11] + "\t\t Deadline: " + index[5]
                + "\t\t" + "Time Delivered: " + str(index[12]) + "\t\t Special Notes: " + index[7])

    # Cycles through and prints deliveries carried out by the extra truck = O(n)
    if selection == 3:
        print("\nExtra Truck Packages:")
        for index in distance_algorithm.get_extra_truck_sorted():
            print(
                "Package ID " + index[0] + "\t\t Status: " + index[11] + "\t\t Deadline: " + index[5]
                + "\t\t" + "Time Delivered: " + str(index[12]) + "\t\t Special Notes: " + index[7])

    # Utilizes recursion to display information for all trucks
    if selection == 4:
        print("\nDeparture Times: ")
        print("First Truck: " + time_simulator.get_first_truck_departure()[0])
        print("Second Truck: " + time_simulator.get_second_truck_departure()[0])
        print("Extra Truck: " + time_simulator.get_extra_truck_departure()[0] + "\n")

        view_deliveries(1)
        view_deliveries(2)
        view_deliveries(3)


# Locates the last delivery of the day
def find_final_delivery():
    (hours, minutes, seconds) = time_simulator.get_first_truck_departure()[0].split(':')
    final_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

    for index in range(1, 41):
        if package_data.get_map().get(str(index))[12] >= final_time:
            final_time = package_data.get_map().get(str(index))[12]

    return final_time


# Updates truck hash table with changes = 0(1)
def update_delivery_information():
    package_data.get_map().get(str(9))[1] = "410 S State St"
    package_data.get_map().get(str(9))[7] = "Wrong address listed; fixed at 10:20 AM"


# Loads the methods above for the program
def load_data():
    assign_departure_times()
    assign_package_addresses()
    assign_optimal_path()
    assign_package_times()
