import re

def extract_data(text):
    # 正規表現パターンを使用して、<データ名>:<値> の形式を抽出
    pattern = r'\b\w+:\w+\b'
    matches = re.findall(pattern, text)
    return matches

def better_extract_data(text):
    # 正規表現パターンを使用して、データ名と値をキャプチャグループで抽出
    pattern = r'\b(\w+):(\w+)\b'
    matches = re.findall(pattern, text)
    return matches

# Example usage:
text = "The subject has Age:25 and Height:180cm.Other details are not relevant.Weight:70kg was noted."
print(extract_data(text))  # Output: ['Age:25', 'Height:180cm', 'Weight:70kg']
print(better_extract_data(text))  # Output: [('Age', '25'), ('Height', '180cm'), ('Weight', '70kg')]