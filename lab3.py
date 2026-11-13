def find_single(numbers):
    result = 0

    for number in numbers:
        result = result ^ number

    return result


numbers = [4, 1, 2, 1, 2]

answer = find_single(numbers)

print("Самотнє число:", answer)

