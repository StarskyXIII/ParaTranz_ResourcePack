import json
import requests
import os
import sys

## ParaTranz Settings
project_id = os.environ.get("PROJECT_ID")
file_id = os.environ.get("FILE_ID")
auth_key = os.environ.get("PARATRANZ_TOKEN")

## Converted File Path
output_file = 'assets/kubejs/lang/zh_tw.json'

# Main Start!
paratranz_responsed = requests.get(f"https://paratranz.cn/api/projects/{project_id}/files/{file_id}/translation", headers={'Authorization': f'{auth_key}'})

if paratranz_responsed.status_code == 200:
    paratranz_content = paratranz_responsed.content
else:
    print("Error, no content!!")
    sys.exit(1)

json_data = json.loads(paratranz_content)

# 轉換資料格式
converted_data = {}
for entry in json_data:
    key = entry.get('key', '')
    translation = entry.get('translation', '')
    original = entry.get('original', '')

    # 若 translation 為空，則略過
    if not translation:
        continue

    # 加入到轉換後的資料中
    converted_data[key] = translation

# 輸出檔案
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(converted_data, f, indent=2, ensure_ascii=False, sort_keys=True)

print(f'檔案 {output_file} 已成功產生！')
