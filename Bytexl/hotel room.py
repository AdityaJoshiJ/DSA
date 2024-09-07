from abc import ABC, abstractmethod

class Customer:
    count = 1

    def __init__(self, customer_name, address, no_of_days):
        self.customer_id = Customer.count
        Customer.count += 1
        self.customer_name = customer_name
        self.address = address
        self.no_of_days = no_of_days

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def set_address(self, address):
        self.address = address

    def set_no_of_days(self, no_of_days):
        self.no_of_days = no_of_days

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_customer_id(self):
        return self.customer_id

    def get_customer_name(self):
        return self.customer_name

    def get_address(self):
        return self.address

    def get_no_of_days(self):
        return self.no_of_days

class Room(ABC):
    count = 1

    def __init__(self, price):
        self.room_id = Room.count
        Room.count += 1
        self.price = price
        self.customer = None

    def get_room_id(self):
        return self.room_id

    def get_price(self):
        return self.price

    def get_customer(self):
        return self.customer

    def set_room_id(self, room_id):
        self.room_id = room_id

    def set_price(self, price):
        self.price = price

    def set_customer(self, customer):
        self.customer = customer

    @abstractmethod
    def calculate_room_rent(self, no_of_days):
        pass

class LuxuryRoom(Room):
    def __init__(self, price, free_wifi):
        super().__init__(price)
        self.free_wifi = free_wifi

    def get_free_wifi(self):
        return self.free_wifi

    def set_free_wifi(self, free_wifi):
        self.free_wifi = free_wifi

    def calculate_room_rent(self, no_of_days):
        return self.price * no_of_days

class StandardRoom(Room):
    def __init__(self, price, comfortable_desk):
        super().__init__(price)
        self.comfortable_desk = comfortable_desk

    def get_comfortable_desk(self):
        return self.comfortable_desk

    def set_comfortable_desk(self, comfortable_desk):
        self.comfortable_desk = comfortable_desk

    def calculate_room_rent(self, no_of_days):
        return self.price * no_of_days

class Hotel:
    def __init__(self, room_list, location):
        self.room_list = room_list
        self.location = location

    def get_room_list(self):
        return self.room_list

    def get_location(self):
        return self.location

    def set_room_list(self, room_list):
        self.room_list = room_list

    def set_location(self, location):
        self.location = location

    def check_in(self, customer, room_type):
        for room in self.room_list:
            if isinstance(room, room_type) and room.get_customer() is None:
                room.set_customer(customer)
                return room
        return None

    def check_out(self, customer):
        for room in self.room_list:
            if room.get_customer() == customer:
                room.set_customer(None)
                return room
        return None

if __name__ == "__main__":
    rooms = [
        LuxuryRoom(200, True),
        StandardRoom(100, True),
        StandardRoom(80, False)
    ]

    hotel = Hotel(rooms, "Porbander")
    customer1 = Customer("Aditya", "123 Chaya", 5)

    checked_in_room = hotel.check_in(customer1, LuxuryRoom)
    if checked_in_room:
        print(f"Checked in {customer1.get_customer_name()} to room {checked_in_room.get_room_id()}")

    checked_out_room = hotel.check_out(customer1)
    if checked_out_room:
        print(f"Checked out {customer1.get_customer_name()} from room {checked_out_room.get_room_id()}")
        print(f"no of days {customer1.get_no_of_days()}")
