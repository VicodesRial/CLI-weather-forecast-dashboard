def show_menu():
    while True:
        print("========== Weather Dashboard ==========")
        print("1. Current Weather")
        print("2. 3-Day Forecast")
        print("3. Search History")
        print("4. Clear Search History")
        print("5. Exit")
        print("=======================================")

        try:
            choice = int(input("Choose an option: "))

            if 1 <= choice <= 5:
                return choice
            print()
            print("Please enter a number between 1 and 5.")
            print()

        except ValueError:
            print()
            print("Invalid input. Please enter a number.")
            print()