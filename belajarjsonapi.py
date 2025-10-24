import json

data = {"nama": "Khonsa", "umur": 18}
json_str = json.dumps(data)
print(json_str)

python_obj = json.loads(json_str)
print(python_obj["nama"])

#utk *import json hrs tau json yang mana yg mau diimpor, kita hrs mengubah nama json yg lain biar ga ketuker