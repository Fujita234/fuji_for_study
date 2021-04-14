
def quick_sort(list):
    if len(list) <= 1:
        return list

    ref = list[0]
    ref_count = 0
    right = []
    left = []

    for i in list:
        if i < ref:
            left.append(i)
        elif i > ref:
            right.append(i)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)

    return left + [ref] * ref_count + right


a = 1234567891
list = str(a)
list_1 = []
for i in range(len(list)):
  print(list[i])
  list_1.append(list[i])
print(quick_sort(list_1))



print(quick_sort([1, 4, 9, 10, 8, 2, 3, 6, 5, 7]))