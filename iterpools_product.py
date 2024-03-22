def cartesian(list_one, list_two):
    print(
        *[
            (int(x), int(y)) for x in list_one for y in list_two
        ]
    )
    

if __name__ == "__main__":
    a = list(input().strip().split(" "))
    b = list(input().strip().split(" "))
    cartesian(a, b)
