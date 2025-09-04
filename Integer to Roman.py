class IntegerToRoman:
    def __init__(self, number: int):
        if not (1 <= number <= 3999):
            raise ValueError("Number must be between 1 and 3999")
        self.number = number
    def convert(self) -> str:
        """Convert the integer to a Roman numeral."""
        value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I"),
        ]
        result = ""
        n = self.number
        for value, symbol in value_map:
            while n >= value:
                result += symbol
                n -= value
        return result
if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        roman_converter = IntegerToRoman(number)
        print(f"{number} in Roman numerals is {roman_converter.convert()}")
    except ValueError as e:
        print("Error:", e)