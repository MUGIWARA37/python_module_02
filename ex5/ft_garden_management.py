class GardenManager:
    plant_list = []
    tank = 2

    def __init__(self, plant_name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

        if self.plant_name is None or self.plant_name == "":
            raise ValueError("Error adding plant: Plant name cannot be empty!")
        else:
            GardenManager.plant_list += [self]
            print(f"Added {self.plant_name} successfully")

    def tunk_status() -> None:
        if GardenManager.tank <= 0:
            raise ValueError("Caught GardenError: Not enough water in tank")
        else:
            GardenManager.tank -= 1

    def watering_plants() -> None:
        try:
            for plant in GardenManager.plant_list:
                GardenManager.tunk_status()
                print(f"Watering {plant.plant_name} - success")
        except Exception as e:
            print(f"{e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self) -> None:
        if self.water_level < 1:
            raise ValueError(
                f"Error  checking {self.plant_name}: "
                f"Water level {self.water_level} is too low (min 1)"
            )
        elif self.water_level > 10:
            raise ValueError(
                f"Error  checking {self.plant_name}:"
                f"Water level {self.water_level} is too high (max 10)")
        elif self.sunlight_hours < 2:
            raise ValueError(f"Error  checking {self.plant_name}:"
                             f"Sunlight hours {self.sunlight_hours} is "
                             "too low (min 2)")
        elif self.sunlight_hours > 12:
            raise ValueError(f"Error  checking {self.plant_name}:"
                             f" Sunlight hours {self.sunlight_hours} is "
                             "too high (max 12)")
        else:
            print(f"{self.plant_name}: healthy"
                  f"(water: {self.water_level}, sun: {self.sunlight_hours})")


def test_plant_checks():
    print("Adding plants to garden...")
    try:
        GardenManager("tomato", 5, 6)
        GardenManager("lettuce", 15, 6)
        GardenManager("",  6, 6)
    except Exception as e:
        print(f"{e}\n")
    print("Watering plants...")
    GardenManager.watering_plants()
    print("Checking plant health...")
    try:
        for plant in GardenManager.plant_list:
            plant.check_plant_health()
    except Exception as e:
        print(f"{e}")

    print("\nTesting error recovery...")
    try:
        raise ValueError("Caught GardenError: Not enough water in tank")
    except ValueError as v:
        print(v)
    finally:
        print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_plant_checks()
    print("\nGarden management system test complete!")
