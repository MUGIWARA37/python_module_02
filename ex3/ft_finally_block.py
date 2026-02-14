def water_plants(plant_list: str) -> None:
    print("Opening watering system")
    for plant in plant_list:
        if plant is None:
            raise ValueError("Error: Cannot water None - invalid plant!")
        print(f"Watering {plant}")


def test_watering_system() -> None:
    print("Testing normal watering...")
    try:
        good_input = ["tomato", "lettuce", "carrots"]
        water_plants(good_input)
        print("Watering completed successfully!")
    except Exception as e:
        print(f"{e}\n")
    print()
    print("Testing with error...")
    try:
        bad_input = ["tomato", None, "carrots"]
        water_plants(bad_input)
    except ValueError as e:
        print(f"{e}")
    finally:
        print("Closing watering system (cleanup)")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
