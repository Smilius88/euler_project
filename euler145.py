def reversible(num):
    if num % 10 == 0:
        return False
    j = num + int(str(num)[::-1])
    s = str(j)
    l = len(s)
    while l:
        d = int(s[l-1])
        if d % 2 == 0:
            return False
        l -= 1
    return True

s = []
for i in xrange(1, 100):
    if reversible(i):
        s.append(str(i))

[12, 14, 16, 18, 21, 23, 25, 27, 32, 34, 36, 41, 43, 45, 52, 54, 61, 63, 72, 81]
[209, 219, 229, 239, 249, 308, 318, 328, 338, 348, 407, 409, 417, 419, 427, 429, 437, 439, 447, 449, 506, 508, 516, 518, 526, 528, 536, 538, 546, 548, 605, 607, 609, 615, 617, 619, 625, 627, 629, 635, 637, 639, 645, 647, 649, 704, 706, 708, 714, 716, 718, 724, 726, 728, 734, 736, 738, 744, 746, 748, 803, 805, 807, 809, 813, 815, 817, 819, 823, 825, 827, 829, 833, 835, 837, 839, 843, 845, 847, 849, 902, 904, 906, 908, 912, 914, 916, 918, 922, 924, 926, 928, 932, 934, 936, 938, 942, 944, 946, 948]
>>> B
[12, 14, 16, 18, 21, 23, 25, 27, 32, 34, 36, 41, 43, 45, 52, 54, 61, 63, 72, 81]

2 02 0 90 9
 v-----number less than 5, inc. 0.
2 9
3 8
4 7
4 9
5 6
5 8
6 5
6 7
6 9
7 8
7 6
7 4
8 3
8 5
8 7
8 9
9 2
9 4
9 6
9 8

2094409
2 09 4 68 9

 249
 942
1191


209
 c-c-c-c
 2094409
 9044902
11139311

while 
    0n-((11-10*n) to 98 by 2's)
