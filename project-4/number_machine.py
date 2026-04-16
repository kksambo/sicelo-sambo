from typing import Tuple


class NumberMachine:
    """
    Performs operations on a five-digit number:
    - Reverse the number
    - Calculate sum of digits
    - Increment each digit
    """

    def process(self, input_number: int) -> Tuple[int, int, int]:
        reversed_number: int = 0
        sum_of_digits: int = 0
        incremented_number: int = 0
        place_value: int = 1

        temp_number: int = input_number

        while temp_number > 0:
            digit: int = temp_number % 10

            # Reverse number
            reversed_number = reversed_number * 10 + digit

            # Sum of digits
            sum_of_digits += digit

            # Increment digit
            incremented_digit: int = (digit + 1) % 10
            incremented_number += incremented_digit * place_value

            place_value *= 10
            temp_number //= 10

        return reversed_number, sum_of_digits, incremented_number


#DEMO

if __name__ == "__main__":
    machine: NumberMachine = NumberMachine()

    number: int = 12391
    reversed_num, digit_sum, incremented_num = machine.process(number)

    print(f"Reversed: {reversed_num}")
    print(f"Sum of digits: {digit_sum}")
    print(f"Incremented digits: {incremented_num}")