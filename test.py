def count_the_one_num(num):
    num = num + 1
    count = 0
    for key in range(len(str(num))):
        res = int(str(num / (10 ** key))[-1])
        val_one = 10 ** key
        val_two = res * (key * 10 ** (key - 1))
        val_three = 0
        if key > 0 and int(str(num)[len(str(num)) - key-1]):
            val_three = int(str(num)[len(str(num)) - key:])
        val = (val_two + val_three) if res < 2 else (val_one + val_two)
        count += val
    return int(count)
