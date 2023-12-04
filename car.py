from abc import ABC, abstractmethod
from CarFactory import CarFactory

class Car(CarFactory):
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    @abstractmethod
    def needs_service(self):
        pass
