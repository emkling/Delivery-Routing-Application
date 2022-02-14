import PackageDelivery
import TimeSimulator


# Starts the UI for the user
def start():
    user_choice = input(

        """\nPlease enter one of the following options:
    
        1. View the end of day report (total mileage, end of deliveries, all packages)
        2. View status of all packages at a specific time
        3. View individual package by ID at a specific time
        4. Type 'exit' to close the program
        """)

    while user_choice != 'exit':

        if user_choice == '1':
            try:
                print("End of the day report:\n")

                print("Total Mileage: " + str(PackageDelivery.calculate_total_distance()))
                print("All packages delivered by: " + str(PackageDelivery.find_final_delivery()))
                PackageDelivery.view_deliveries(4)

                return_input = input("Enter 'b' to go back to the main menu or 'exit' to close the program: ")

                if return_input == 'b':
                    start()
                elif return_input == 'exit':
                    exit()
            except ValueError:
                print("Please try another entry")

        elif user_choice == 'exit':
            exit()

        elif user_choice == '2':
            try:
                time_choice = input("""
                Enter a time in 24 hour notation (HH:MM:SS): 
                or enter 'b' to go back to the main menu 
                 """)
                if time_choice == 'b':
                    start()
                elif time_choice == 'exit':
                    exit()
                else:
                    TimeSimulator.output_all_package_statuses(time_choice)
            except ValueError:
                print("Please try another entry")

        elif user_choice == '3':
            try:
                package_id = input("""
                Enter a package ID : 
                or enter 'b' to go back to the main menu 
                 """)
                if package_id == 'b':
                    start()
                elif package_id == 'exit':
                    exit()
                else:
                    time_choice = input("Enter a time in 24 hour notation (HH:MM:SS): ")

                    if time_choice == 'b':
                        start()
                    elif time_choice == 'exit':
                        exit()
                    else:
                        TimeSimulator.output_individual_package_status(package_id, time_choice)
            except ValueError:
                print("There was an error. Please ensure entry is valid")

        else:
            print("Invalid input")
            start()


# Main class of the program
# Loads the initial data needed and calls the start method for the GUI
class Main:
    # Initializes the elements of the program
    PackageDelivery.load_data()
    # Starts the GUI
    start()
