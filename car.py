from abc import ABC, abstractmethod
from CarFactory import CarFactory
from serviceable import Serviceable


class Car(CarFactory, Serviceable):
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    @abstractmethod
    def needs_service(self):
        pass
