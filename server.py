from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Konfigurasi database MySQL
db = pymysql.connect(
    host="localhost",
    user="root",       # Ganti dengan username MySQL Anda
    password="",       # Ganti dengan password MySQL Anda
    database="aplikasi_db" # Database yang sudah Anda buat
)

# API untuk mendapatkan semua aplikasi
@app.route('/applications', methods=['GET'])
def get_applications():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM aplikasi")
        applications = cursor.fetchall()
        result = []
        for app in applications:
            result.append({
                'id': app[0],
                'nama': app[1],          # Ganti name menjadi nama
                'genre': app[2],         # Ganti description menjadi genre
                'harga': app[3]          # Ganti price menjadi harga
            })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API untuk menambahkan aplikasi baru
@app.route('/applications', methods=['POST'])
def add_application():
    try:
        data = request.json
        cursor = db.cursor()
        sql = "INSERT INTO aplikasi (nama, genre, harga) VALUES (%s, %s, %s)"  # Ganti nama, genre, harga
        cursor.execute(sql, (data['nama'], data['genre'], data['harga']))
        db.commit()
        return jsonify({'message': 'Application added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API untuk memperbarui aplikasi
@app.route('/applications/<int:app_id>', methods=['PUT'])
def update_application(app_id):
    try:
        data = request.json
        cursor = db.cursor()
        sql = "UPDATE aplikasi SET nama=%s, genre=%s, harga=%s WHERE id=%s"  # Ganti nama, genre, harga
        cursor.execute(sql, (data['nama'], data['genre'], data['harga'], app_id))
        db.commit()
        return jsonify({'message': 'Application updated successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API untuk menghapus aplikasi
@app.route('/applications/<int:app_id>', methods=['DELETE'])
def delete_application(app_id):
    try:
        cursor = db.cursor()
        sql = "DELETE FROM aplikasi WHERE id=%s"
        cursor.execute(sql, (app_id,))
        db.commit()
        return jsonify({'message': 'Application deleted successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
