from typing import List
from icecream import ic


def increment(decimal_encoded_array: List[int]) -> List[int]:
    # start with incrementing the last indexed element in the array
    decimal_encoded_array[-1] += 1
    # check if the number has become double digit
    for i in reversed(range(1, len(decimal_encoded_array))):
        # start from the end of the array
        # then check if the array has become more than 10 at any index
        if decimal_encoded_array[i] != 10:
            break
        decimal_encoded_array[i], decimal_encoded_array[i - 1] = (
            0,
            decimal_encoded_array[i - 1] + 1,
        )

    # if the First index has become 10 then we would need to increase the size of the array to accomodate that
    if decimal_encoded_array[0] == 10:
        decimal_encoded_array[0] = 1
        decimal_encoded_array.append(0)

    return decimal_encoded_array


if __name__ == "__main__":
    DEA = input(
        "Please enter the space seperated integer array that represent the decimal encoded number: \n\n"
    )
    DEA = DEA.split()
    DEA = [int(num) for num in DEA]

    ic(increment(DEA))
