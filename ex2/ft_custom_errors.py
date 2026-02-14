class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_water_tank(liters: int) -> None:
    if liters <= 0:
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    print("Water level looks good.")


def check_plant(plant_name: str) -> None:
    if plant_name == "tomato":
        raise PlantError(f"Caught PlantError: The {plant_name}"
                         "plant is wilting!")
    print(f"{plant_name} is alive and growing.\n")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        check_plant("tomato")
    except GardenError as e:
        print(f"{e}\n")

    try:
        print("Testing WaterError...")
        check_water_tank(0)
    except WaterError as e:
        print(f"{e}\n")

    print("Testing catching all garden errors...")
    try:
        check_water_tank(0)
        check_plant("tomato")
    except (WaterError, PlantError) as e:
        print(f"{e}\n")

    print("All custom error types work correctly!")
