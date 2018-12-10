def merge(arr1, ps, pm, pe):
    result = []
    totalNum = pe - ps
    n1 = pm - ps
    j1 = ps
    j2 = pm + 1
    for i in range(totalNum):
        if arr1[j1] < arr1[j2] and j1 < n1:
            result.append(arr1[j1])
            j1 += 1
        elif j2 < pe:
            result.append(arr1[j2])
            j2 += 1
        if j1 >= n1:
            if j2 <= pe:
                result.append(arr1[j2])
                j2 += 1
        if j2 >= pe:
            if j1 <= n1:
                result.append(arr1[j1])
                j1 += 1
    return result


def mergesort(arr, ps, pe):
    # ps~pm, pm+1~pe
    print(arr[ps] + arr[pe])
    if ps < pe:
        pm = (ps + pe) / 2
        mergesort(arr, ps, pm)
        mergesort(arr, pm + 1, pe)
    return


oriList = [6, 8, 12, 5, 8, 9, 10, 11]
result = merge(oriList, 0, 3, 7)
print(oriList)
mergesort(oriList, 0, len(oriList) - 1)
