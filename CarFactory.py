from car import Car
from engine import Engine
from battery import Battery


class CarFactory():

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = Battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = Engine.Sternman(warning_light_on)
        battery = Battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = Battery.NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = Battery.NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
