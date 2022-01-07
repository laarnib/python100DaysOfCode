def add(first_num, second_num):
    if first_num == "Not a number":
        return "Not a number"
    return first_num + second_num

def subtract(first_num, second_num):
    if first_num == "Not a number":
        return "Not a number"
    return first_num - second_num

def multiply(first_num, second_num):
    if first_num == "Not a number":
        return "Not a number"
    return first_num * second_num

def divide(first_num, second_num):
    if first_num == "Not a number" or second_num == 0:
        return "Not a number"
    return first_num / second_num