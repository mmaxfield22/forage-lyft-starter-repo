from tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        service = False
        for tire in self.tire_wear:
            if tire >= 0.9:
                service = True
        return service
