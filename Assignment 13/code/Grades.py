def total(value):
    sum = 0
    for i in value:
        sum += i
    return sum

def average(values):
        sum = 0
        for i in values:
            sum += i
        length = len(values)
        total = sum / length
        return total