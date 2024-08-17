def mystery_function(lst):
    result = []  # 空のリストを初期化
    for i in range(len(lst)):
        if lst[i] % 2 == 0:  # 偶数の要素をチェック
            result.append(lst[i] ** 2)  # 偶数の要素を2乗して追加
        else:
            result.append(lst[i])  # 奇数の要素はそのまま追加
    return result

# Example usage and tests:
print(mystery_function([1, 2, 3, 4, 5]))  # Output: [1, 4, 3, 16, 5]
print(mystery_function([4, 1, 6, 2, 10]))  # Output: [16, 1, 36, 4, 100]
print(mystery_function([0, 7, 8, 9]))  # Output: [0, 7, 64, 9]
print(mystery_function([]))  # Output: []