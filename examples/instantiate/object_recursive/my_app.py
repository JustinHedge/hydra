# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from typing import List

from omegaconf import DictConfig

import hydra


class Driver:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Wheel:
    def __init__(self, radius: int, width: int) -> None:
        self.radius = radius
        self.width = width


class Car:
    def __init__(self, driver: Driver, wheels: List[Wheel]):
        self.driver = driver
        self.wheels = wheels

    def drive(self) -> None:
        print(f"Driver : {self.driver.name}, {len(self.wheels)} wheels")


@hydra.main(config_name="config")
def my_app(cfg: DictConfig) -> None:
    car: Car = hydra.utils.instantiate_recursive(cfg.car)
    car.drive()


if __name__ == "__main__":
    my_app()
