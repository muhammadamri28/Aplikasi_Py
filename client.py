import requests

BASE_URL = "http://127.0.0.1:5000"

def get_applications():
    response = requests.get(f"{BASE_URL}/applications")
    print(f"Status Code: {response.status_code}")  # Log status code
    if response.status_code == 200:
        applications = response.json()
        print("\nDaftar Aplikasi:")
        for app in applications:
            print(f"ID: {app['id']}, Nama: {app['nama']}, Genre: {app['genre']}, Harga: {app['harga']}")
    else:
        print(f"Error: {response.text}")

def add_application():
    nama = input("Masukkan nama aplikasi: ")
    genre = input("Masukkan genre aplikasi: ")
    harga = float(input("Masukkan harga aplikasi: "))
    data = {"nama": nama, "genre": genre, "harga": harga}
    print(f"Data yang dikirim: {data}")  # Log data yang dikirim
    response = requests.post(f"{BASE_URL}/applications", json=data)
    print(f"Status Code: {response.status_code}")  # Log status code
    print(f"Response Text: {response.text}")  # Log respons

def update_application():
    app_id = int(input("Masukkan ID aplikasi yang ingin diperbarui: "))
    nama = input("Masukkan nama aplikasi baru: ")
    genre = input("Masukkan genre aplikasi baru: ")
    harga = float(input("Masukkan harga aplikasi baru: "))
    data = {"nama": nama, "genre": genre, "harga": harga}
    print(f"Data yang dikirim: {data}")  # Log data yang dikirim
    response = requests.put(f"{BASE_URL}/applications/{app_id}", json=data)
    print(f"Status Code: {response.status_code}")  # Log status code
    print(f"Response Text: {response.text}")  # Log respons

def delete_application():
    app_id = int(input("Masukkan ID aplikasi yang ingin dihapus: "))
    response = requests.delete(f"{BASE_URL}/applications/{app_id}")
    print(f"Status Code: {response.status_code}")  # Log status code
    print(f"Response Text: {response.text}")  # Log respons

def menu():
    while True:
        print("\nMenu:")
        print("1. Lihat Aplikasi")
        print("2. Tambah Aplikasi")
        print("3. Perbarui Aplikasi")
        print("4. Hapus Aplikasi")
        print("5. Keluar")
        choice = input("Pilih menu: ")
        if choice == "1":
            get_applications()
        elif choice == "2":
            add_application()
        elif choice == "3":
            update_application()
        elif choice == "4":
            delete_application()
        elif choice == "5":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()
