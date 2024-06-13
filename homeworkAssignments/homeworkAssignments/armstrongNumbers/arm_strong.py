import math

def armstrong(stop):
    armstrong_list = []
    
    for num in range(stop):
        total = 0
        arr = str(num)
        # Verify number is an armstrong number
        for number in arr:
            total += math.pow(int(number),len(arr))
        if total == num:
            armstrong_list.append(num)
    return armstrong_list

print(armstrong(999))
