for n in range(100, 334):
    left_part = set(str(n))
    right_part = set(str(n*3))
    overall_digits = left_part.union(right_part)
    
    if len(overall_digits) == 6:
        print(f'{n}+{n}+{n}={3*n}')
