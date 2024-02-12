for n in range(100, 334):
    left_part = set(str(n))
    right_part = set(str(n*3))
    left_part.update(right_part)

    if len(left_part) == 6:
        print(f'{n}+{n}+{n}={3*n}')
