class Conference:
    def __init__(self, name="Default Conference", participants_amount=0, ticket_price=0, venue="Unknown"):
        self.__name = name
        self.__participants_amount = participants_amount
        self.__ticket_price = ticket_price
        self.__venue = venue
        self.public_number = 2024
        self.public_string = "Public"

    def get_name(self):
        return self.__name

    def get_participants_amount(self):
        return self.__participants_amount

    def get_ticket_price(self):
        return self.__ticket_price

    def get_venue(self):
        return self.__venue

    def __str__(self):
        return (f"Conference name: {self.__name}, "
                f"Participants amount: {self.__participants_amount}, "
                f"Ticket price: {self.__ticket_price}, "
                f"Venue: {self.__venue}, "
                f"Public Number: {self.public_number}, "
                f"Public String: {self.public_string}")

    def __repr__(self):
        return (f"Conference({self.__name}, {self.__participants_amount}, "
                f"{self.__ticket_price}, {self.__venue}, "
                f"{self.public_number}, {self.public_string})")

    def __del__(self):
        """Destructor that is called when the object is about to be destroyed."""
        print(f"Conference '{self.__name}' is being deleted.")


def main():
    conference1 = Conference("Python Conference", 2000, 50, "online")
    conference2 = Conference("Django Conference", 1500, 40, "in-person")
    conference3 = Conference("Rust Conference", 1000, 30, "online")

    print(f"CONFERENCE1: {conference1}")
    print(f"CONFERENCE2: {conference2}")
    print(f"CONFERENCE3: {conference3}")


main()