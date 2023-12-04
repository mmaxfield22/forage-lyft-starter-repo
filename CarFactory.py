from car import Car
from engine import Engine

class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine.Capulet(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine.Willoughby(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = Engine.Sternman(warning_light_on)
        battery = Spindler(last_service_date, current_date)
        return Car(engine, battery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine.Willoughby(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine.Capulet(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)
        return Car(engine, battery)