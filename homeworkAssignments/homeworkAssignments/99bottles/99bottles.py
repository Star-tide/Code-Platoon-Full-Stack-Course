def song(bottles_left):
    bottle_reset = bottles_left
    while bottles_left >= 2:
        print(f'{bottles_left} bottles of beer on the wall, {bottles_left} bottles of beer.')
        bottles_left -= 1
        print(f'Take one down and pass it around, {bottles_left} bottles of beer on the wall.')
    print(f'{bottles_left} bottle of beer on the wall, {bottles_left} bottle of beer.')
    bottles_left -= 1
    print(f'No more bottles of beer on the wall, No more bottles of beer.')
    print(f'Go to the store and buy some more, {bottle_reset} bottles of beer on the wall.')

song(10)