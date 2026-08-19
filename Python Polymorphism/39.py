class HomeDelivery:
    def deliver(self):
        print("Home delivery")
class CourierDelivery:
    def deliver(self):
        print("Courier delivery")
class BikeDelivery:
    def deliver(self):
        print("Bike delivery")
def process_delivery(delivery):
    delivery.deliver()
process_delivery(HomeDelivery())
process_delivery(CourierDelivery())
process_delivery(BikeDelivery())