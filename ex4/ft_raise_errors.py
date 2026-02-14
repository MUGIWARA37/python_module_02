def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if plant_name is None or plant_name == "":
        raise ValueError(f"Error: Plant name '{plant_name}' is invalid!")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level} "
                         "is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level} "
                         "is too high (max 10)")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         "is too high (max 12)")


def test_plant_checks() -> None:
    test_type = ["Testing good values...", "Testing empty plant name...",
                 "Testing bad water level...", "Testing bad sunlight hours..."]
    plant_name = ["tomato", None, "sunflower", "a7sen nass"]
    water_level = [9, 15, 15, 9]
    sunlight_hours = [6, 6, 6, 0]

    for i in range(0, 4):
        print(test_type[i])
        try:
            check_plant_health(plant_name[i], water_level[i],
                               sunlight_hours[i])
            print(f"Plant '{plant_name[i]}' is healthy!\n")
        except Exception as e:
            print(f"{e}\n")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("All error raising tests completed!")
