import datetime

# First departure times
import PackageData
import PackageDelivery

first_truck_departure = ['08:00:00']
second_truck_departure = ['09:29:00']
extra_truck_departure = ['09:05:00']


# Returns time values relative to the distance traveled = O(n)
def get_current_time(miles, time_list):
    time_output = datetime.timedelta()
    calculated_time = miles / 18

    formatted_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(calculated_time * 60, 60)) + ':00'
    time_list.append(formatted_time)

    for index in time_list:
        (hours, minutes, seconds) = index.split(':')
        time_output = time_output + datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
    return time_output


# Displays all package statuses at a chosen time by the user = O(n)
def output_all_package_statuses(user_choice):
    # Converts time chosen by user from string to a timedelta object
    (hours, minutes, seconds) = user_choice.split(':')
    reference_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

    # Converts update time from string to a timedelta objec
    update_time = "10:20:00"
    (hours, minutes, seconds) = update_time.split(':')
    revision_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

    # Checks if updated information is required based on time chosen by user
    if reference_time >= revision_time:
        PackageDelivery.update_delivery_information()

    print("\nShowing the status of packages at: " + str(reference_time) + "\n")
    for index in range(1, 41):

        # Converts the truck departure time from string to a timedelta object
        (hours, minutes, seconds) = PackageData.get_map().get(str(index))[10].split(':')
        start_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

        try:
            # Checks if time chosen by user is between the departure time and before delivery
            if start_time <= reference_time <= PackageData.get_map().get(str(index))[12]:
                PackageData.get_map().get(str(index))[11] = "En Route   "

                print("Package ID: " + PackageData.get_map().get(str(index))[0]
                      + "\t\t Status: " + str(PackageData.get_map().get(str(index))[11]
                                              + " (Departed at: " + str(PackageData.get_map().get(str(index))[10] + ")"
                                                                        + "\t\t Delivery Deadline: " +
                                                                        PackageData.get_map().get(str(index))[5]
                                                                        + "\t\t Package Weight " +
                                                                        PackageData.get_map().get(str(index))[6]
                                                                        + "\t\t Address: " +
                                                                        PackageData.get_map().get(str(index))[1]
                                                                        + " " + PackageData.get_map().get(str(index))[2]
                                                                        + ", " + PackageData.get_map().get(str(index))[3]
                                                                        + " " + PackageData.get_map().get(str(index))[4])))

            # Checks if time chosen by user is past the delivery time
            elif reference_time >= PackageData.get_map().get(str(index))[12]:
                PackageData.get_map().get(str(index))[11] = "Delivered  "

                print("Package ID: " + PackageData.get_map().get(str(index))[0]
                      + "\t\t Status: " + str(PackageData.get_map().get(str(index))[11]
                                                                      + " (Completed at: " + str(
                                                                      PackageData.get_map().get(str(index))[12]) + ")"
                                                                      + "\t\t Delivery Deadline: " +
                                                                      PackageData.get_map().get(str(index))[5]
                                                                      + "\t\t Package Weight " +
                                                                      PackageData.get_map().get(str(index))[6]
                                                                      + "\t\t Address: " +
                                                                      PackageData.get_map().get(str(index))[1]
                                                                      + " " + PackageData.get_map().get(str(index))[2]
                                                                      + ", " + PackageData.get_map().get(str(index))[3]
                                                                      + " " + PackageData.get_map().get(str(index))[4]))

            # Checks if time chosen by user is before the departure time
            elif start_time >= reference_time:
                PackageData.get_map().get(str(index))[11] = "At the Hub"

                print("Package ID: " + PackageData.get_map().get(str(index))[0]
                      + "\t\t Status: " + str(PackageData.get_map().get(str(index))[11]
                                              + " (To Depart at: " + str(PackageData.get_map().get(str(index))[10] + ")"
                                                                         + "\t\t Delivery Deadline: " +
                                                                         PackageData.get_map().get(str(index))[5]
                                                                         + "\t\t Package Weight " +
                                                                         PackageData.get_map().get(str(index))[6]
                                                                         + "\t\t Address: " +
                                                                         PackageData.get_map().get(str(index))[1]
                                                                         + " " + PackageData.get_map().get(str(index))[2]
                                                                         + ", " + PackageData.get_map().get(str(index))[3]
                                                                         + " " + PackageData.get_map().get(str(index))[4])))
        except ValueError:
            pass


# Displays individual package statuses chosen by the user = O(n)
def output_individual_package_status(package_id, user_choice):
    try:

        # Converts time chosen by user from string to a timedelta object
        (hours, minutes, seconds) = user_choice.split(':')
        reference_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

        # Converts update time from string to a timedelta object
        update_time = "10:20:00"
        (hours, minutes, seconds) = update_time.split(':')
        revision_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

        # Converts the truck departure time from string to a timedelta object
        (hours, minutes, seconds) = PackageData.get_map().get(str(package_id))[10].split(':')
        start_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

        # Checks to see if update to information is necessary
        if reference_time >= revision_time:
            PackageDelivery.update_delivery_information()

        print("\nShowing status of package ID: " + "'" + package_id + "'" + " at " + str(reference_time) + "\n")

        # Checks if time chosen by user is between the departure time and before delivery
        if start_time <= reference_time <= PackageData.get_map().get(str(package_id))[12]:
            PackageData.get_map().get(str(package_id))[11] = "En Route  "
            print("Package ID: " + PackageData.get_map().get(str(package_id))[0]
                  + "\t Status: " + str(PackageData.get_map().get(str(package_id))[11]
                                        + " (Departed at: " + str(PackageData.get_map().get(str(package_id))[10] + ")"
                                                                 + "\t Delivery Deadline: " +
                                                                 PackageData.get_map().get(str(package_id))[5]
                                                                 + "\t Package Weight " +
                                                                 PackageData.get_map().get(str(package_id))[6]
                                                                 + "\t Address: " +
                                                                 PackageData.get_map().get(str(package_id))[1]
                                                                 + " " + PackageData.get_map().get(str(package_id))[2]
                                                                 + ", " + PackageData.get_map().get(str(package_id))[3]
                                                                 + " " + PackageData.get_map().get(str(package_id))[
                                                                      4])))

        # Checks if time chosen by user is past the delivery time
        elif reference_time >= PackageData.get_map().get(str(package_id))[12]:
            PackageData.get_map().get(str(package_id))[11] = "Delivered  "

            print("Package ID: " + PackageData.get_map().get(str(package_id))[0]
                  + "\t Status: " + str(PackageData.get_map().get(str(package_id))[11]
                                                                 + "(Completed at: " + str(
                                                                 PackageData.get_map().get(str(package_id))[12]) + ")"
                                                                 + "\t Delivery Deadline: " +
                                                                 PackageData.get_map().get(str(package_id))[5]
                                                                 + "\t Package Weight " +
                                                                 PackageData.get_map().get(str(package_id))[6]
                                                                 + "\t Address: " +
                                                                 PackageData.get_map().get(str(package_id))[1]
                                                                 + " " + PackageData.get_map().get(str(package_id))[2]
                                                                 + ", " + PackageData.get_map().get(str(package_id))[3]
                                                                 + " " + PackageData.get_map().get(str(package_id))[4]))

        # Checks if time chosen by user is before the departure time
        elif start_time >= reference_time:
            PackageData.get_map().get(str(package_id))[11] = "At the Hub"
            print("Package ID: " + PackageData.get_map().get(str(package_id))[0]
                  + "\t Status: " + str(PackageData.get_map().get(str(package_id))[11]
                                        + " (To Depart at: " + str(PackageData.get_map().get(str(package_id))[10] + ")"
                                                                 + "\t Delivery Deadline: " +
                                                                 PackageData.get_map().get(str(package_id))[5]
                                                                 + "\t Package Weight " +
                                                                 PackageData.get_map().get(str(package_id))[6]
                                                                 + "\t Address: " +
                                                                 PackageData.get_map().get(str(package_id))[1]
                                                                 + " " + PackageData.get_map().get(str(package_id))[2]
                                                                 + ", " + PackageData.get_map().get(str(package_id))[3]
                                                                 + " " + PackageData.get_map().get(str(package_id)[4]))))
    except ValueError:
        pass


# Retrieves first truck departure time = O(1)
def get_first_truck_departure():
    return first_truck_departure


# Retrieves second truck departure time = O(1)
def get_second_truck_departure():
    return second_truck_departure


# Retrieves extra truck departure time = 0(1)
def get_extra_truck_departure():
    return extra_truck_departure
