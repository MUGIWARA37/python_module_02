def garden_operations(input_val: str) -> None:
    if input_val == "ValueError":
        int("abc")

    elif input_val == "ZeroDivisionError":
        1 / 0

    elif input_val == "FileNotFoundError":
        open("missing.txt")

    elif input_val == "KeyError":
        empty_dict = {}
        empty_dict["not_in_dict"]

    else:
        raise Exception("Caught an error, but program continues!")


def test_error_types() -> None:
    test_inputs = ["ValueError", "ZeroDivisionError", "FileNotFoundError",
                   "KeyError", "multiple errors together..."]

    for item in test_inputs:
        print(f"\nTesting {item}...")
        try:
            garden_operations(item)

        except ValueError as e:
            print(f"Caught ValueError:{e}")

        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError{e}")

        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'")

        except KeyError:
            print("Caught KeyError: Key not found in dictionary")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    test_error_types()
