from duration_enum import Duration as duration


class RentScooter:

    # constructor to initialize the shop with available vehicles
    def __init__(self, available):
        self.available = available

    # calculate rental based on number of vehicles and duration
    def calculate_rental(self, quantity, duration):
        if self.available > quantity:
            if duration.ONE_HOUR:
                self.available = self.available - quantity
                return quantity * 5
            elif duration.ONE_DAY:
                self.available = self.available - quantity
                return quantity * 20
            elif duration.ONE_WEEK:
                self.available = self.available - quantity
                return quantity * 50
        else:
            raise Exception("Sorry, no more vehicles available!")

    # apply discount if applicable
    def apply_discount(self, quantity):
        if 3 <= quantity <= 5:
            return 0.7 * self.calculate_rental(quantity, duration)
        if quantity >= 6:
            return 0.6 * self.calculate_rental(quantity, duration)
        else:
            print("No discount applied")
            return self.calculate_rental(quantity, duration)

    def available_now(self):
        return self.available
