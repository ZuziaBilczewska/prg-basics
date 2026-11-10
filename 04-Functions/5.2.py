def cm_to_inches(cm):
    """Convert centimeters to inches."""
    return cm / 2.54


def feet_inches_to_cm(feet, inches):
    """Convert feet and inches to centimeters."""
    total_inches = feet * 12 + inches
    return total_inches * 2.54


def main():
    # Test the conversion functions
    print("Centimeters to inches conversion:")
    print(f"10 cm = {cm_to_inches(10):.2f} in")
    print(f"25.4 cm = {cm_to_inches(25.4):.2f} in")

    print("\nFeet and inches to centimeters conversion:")
    print(f"5 ft 8 in = {feet_inches_to_cm(5, 8):.2f} cm")
    print(f"6 ft 2 in = {feet_inches_to_cm(6, 2):.2f} cm")


if __name__ == "__main__":
    main()
