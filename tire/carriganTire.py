from tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        service = False
        sum_of_tires = 0
        for tire in self.tire_wear:
            sum_of_tires += tire
        service = (sum_of_tires >= 3)
        return service
