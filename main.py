import requests

#koordinat lokasi (misal Jakarta)
latitude = -6.2088
longitude = 106.8456

#URL API ramadhan
url = f"https://api.aladhan.com/v1/timings?latitude={latitude}&longitude={longitude}&method=20"

#ambil data dari API
response = requests.get(url)

#cek status response
if response.status_code == 200:
    data = response.json()
    timings = data["data"]["timings"]
    date = data["data"]["date"]["readable"]

    print(f"Jadwal Salat untuk Tanggal {date}")
    print("-" * 40)
    print(f"Imsak  : {timings['Imsak']}")
    print(f"Subuh  : {timings['Fajr']}")
    print(f"Terbit : {timings['Sunrise']}")
    print(f"Dzuhur : {timings['Dhuhr']}")
    print(f"Ashar : {timings['Asr']}")
    print(f"Magrib : {timings['Maghrib']}")
    print(f"Isya : {timings['Isha']}")
    print("-" * 40)
else:
    print(f"Gagal ambil data dari API. Status code: {response.status_code}")
        
