from rent_scooter import RentScooter


def main():
    print("Welcome to Scooter Rentals LTD!")
    print("Enter the number of scooters you want to rent: ")
    rent = RentScooter(10)
    print(RentScooter.calculate_rental(rent, 1, 1))
    print(RentScooter.available_now(rent))
    print(RentScooter.calculate_rental(rent, 2, 1))
    print(RentScooter.available_now(rent))


main()
