import json
import zipfile

output_file = 'assets/kubejs/lang/zh_tw.json'

archive = zipfile.ZipFile("artifacts.zip", "r")
json_raw_data = archive.open("utf8/en_us.json")

json_data = json.load(json_raw_data)

# 轉換資料格式
converted_data = {}
for entry in json_data:
    key = entry.get('key', '')
    translation = entry.get('translation', '')
    original = entry.get('original', '')

    # 如果 translation 為空，則使用 original
    if not translation:
        translation = original

    # 加入到轉換後的資料中
    converted_data[key] = translation

# 輸出檔案
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(converted_data, f, indent=2, ensure_ascii=False)

print(f'檔案 {output_file} 已成功產生！')
