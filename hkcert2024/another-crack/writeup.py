import struct

array = [
    9, 10, 11, 12, 13, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
    56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
    85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
    111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126
]
array2 = [
    58, 38, 66, 88, 78, 39, 80, 125, 64, 106, 48, 49, 98, 32, 42, 59, 126, 93, 33, 56, 112, 120, 60, 117, 111, 45, 87,
    35, 10, 68, 61, 77, 11, 55, 121, 74, 107, 104, 65, 63, 46, 110, 34, 41, 102, 97, 81, 12, 47, 51, 103, 89, 115, 75,
    54, 92, 90, 76, 113, 122, 114, 52, 72, 70, 50, 94, 91, 73, 84, 95, 36, 82, 124, 53, 108, 101, 9, 13, 44, 96, 67,
    85, 116, 123, 100, 37, 43, 119, 71, 105, 118, 69, 99, 79, 86, 109, 62, 83, 40, 57
]
array3 = [
    16684662107559623091,
    13659980421084405632,
    11938144112493055466,
    17764897102866017993,
    11375978084890832581,
    14699674141193569951
]
num = 14627333968358193854

inverse_dict = {v: k for k, v in zip(array, array2)}

list2 = [num ^ val for val in array3]

flag = ""
for val in list2:
    bytes_val = val.to_bytes(8, byteorder='little')
    for byte in bytes_val:
        if byte in inverse_dict:
            flag += chr(inverse_dict[byte])

print(flag)

