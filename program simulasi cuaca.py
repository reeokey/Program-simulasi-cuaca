import random # modul ini digunakan untuk menghasilkan angka acak dari daftar
import datetime # modul ini digunakan untuk menampilkan waktu saat ini

def simulasi_cuaca(): # fungsi untuk mensimulasikan kondisi cuaca
    
    # daftar pilihan untuk setiap parameter cuaca
    hari = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
    cuaca = ["Cerah","Berawan","Gerimis","Hujan Deras","Badai Petir"]
    suhu_celcius = random.randint(20, 40)
    # suhu dalam derajat celcius yang menghasilkan angka 20 sampai 40 derajat celcius
    kelembapan = random.randint(50, 90)
    # kelembapan dengan angka acak antara 50 sampai 90 persen
    
    # konversi suhu celcius ke farenheit
    suhu_fahrenheit =  (suhu_celcius * 9/5) + 32
    
    # membuat data cuaca
    '''
    random.choice digunakan untuk memilih secara acak satu elemen
    dari daftar hari dan cuaca sedangkan datetime.datetime.now()
    digunakan untuk mendapatkan waktu saat ini.
    '''
    data_cuaca = {
        "hari":random.choice(hari),
        "cuaca":random.choice(cuaca),
        "suhu_celcius":suhu_celcius,
        "suhu_fahrenheit":suhu_fahrenheit,
        "kelembapan":kelembapan,
        "waktu":datetime.datetime.now()
    }
    
    return data_cuaca

def tampilkan_cuaca(data_cuaca):
    '''
    fungsi untuk menampilkan informasi cuaca dalam
    format yang mudah dibaca. menerima data 
    cuaca sebagai input.
    '''
    print("=== Simulasi Cuaca ===")
    print(f"Hari\t\t: {data_cuaca['hari']}")
    print(f"Cuaca\t\t: {data_cuaca['cuaca']}")
    print(f"Suhu\t\t: {data_cuaca['suhu_celcius']} °C / {data_cuaca['suhu_fahrenheit']:.2f} °F")
    print(f"Kelembapan\t: {data_cuaca['kelembapan']}%")
    print(f"Waktu\t\t: {data_cuaca['waktu'].strftime('%Y-%m-%d %H:%M:%S')}")
    
    # prediksi cuaca selanjutnya 
    if data_cuaca["cuaca"] == "Hujan Lebat":
        print("Perkiraan\t: Hujan akan berlanjut selama beberapa jam.")
    elif data_cuaca["cuaca"] == "Badai Petir":
        print("Perkiraan\t: Badai petir perkiraan akan mereda dalam 1-2 jam.") 
    else:
        print("Perkiraan\t: Cuaca diperkiran setabil.")
    
# jalankan code diatas
data_cuaca = simulasi_cuaca()
tampilkan_cuaca(data_cuaca)
