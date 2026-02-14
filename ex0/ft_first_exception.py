def check_temperature(temp_str: str) -> None:
    try:
        number = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if number < 0:
        raise ValueError(f"{number}°C is too cold for plants (min 0°C)")
    elif number > 40:
        raise ValueError(f"{number}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {number}°C is perfect for plants!")


def test_temperature_input() -> None:
    temperatures = ["40", "abc", "100", "-50"]

    for temp in temperatures:
        print(f"Testing temperature: {temp}")
        try:
            check_temperature(temp)
        except ValueError as e:
            print(f"Error: {e}")
        print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
    print("All tests completed - program didn't crash!")
