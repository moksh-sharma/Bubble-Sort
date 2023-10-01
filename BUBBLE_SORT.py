def BUBBLE_SORT():
    # BUBBLE SORT
    m = []
    for i in range(int(input("Enter length of your list : "))):
        a = int(input(f"Enter element {i+1} : "))
        m.append(a)
    n = len(m)
    for i in range(n):
        for j in range(0, n-i-1):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]
    print(m)


BUBBLE_SORT()
