from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd
from datetime import datetime

# Path templates diarahkan ke parent directory '../templates'
app = Flask(__name__, template_folder='../templates')

# URL Apps Script Web App milikmu
APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzMueGMxWfi80OVHeBj6YqA4dUBqQ1T9dqJ2aUP5Ge4d5jwBeXaEpVD2fYLkwA3bGmNng/exec'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/penjualan', methods=['GET'])
def get_penjualan():
    try:
        response = requests.get(APPS_SCRIPT_URL)
        records = response.json()
        
        if not records:
            return jsonify({'transaksi': [], 'tren': []})

        df = pd.DataFrame(records)
        
        # Konversi tipe data numerik
        df['Jumlah'] = pd.to_numeric(df['Jumlah'], errors='coerce').fillna(0)
        df['Harga_Satuan'] = pd.to_numeric(df['Harga_Satuan'], errors='coerce').fillna(0)
        df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0)
        
        # Rekap harian untuk grafik tren harian
        rekap_harian = df.groupby('Tanggal')['Total'].sum().reset_index().to_dict(orient='records')
        
        # Formatting data transaksi secara konsisten untuk dikirim ke frontend
        transaksi = []
        for _, row in df.iterrows():
            transaksi.append({
                'Tanggal': str(row.get('Tanggal', '')),
                'Nama_Pemesan': str(row.get('Nama_Pemesan', '-')),
                'Nama_Produk': str(row.get('Nama_Produk', '')),
                'Jumlah': int(row.get('Jumlah', 0)),
                'Harga_Satuan': int(row.get('Harga_Satuan', 0)),
                'Total': int(row.get('Total', 0))
            })

        return jsonify({
            'transaksi': transaksi,
            'tren': rekap_harian
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/penjualan', methods=['POST'])
def add_penjualan():
    try:
        data = request.json
        tanggal = data.get('tanggal') or datetime.now().strftime('%Y-%m-%d')
        pemesan = data.get('pemesan') or '-'
        produk = data.get('produk')
        harga = int(data.get('harga')) # Harga per pack otomatis dari frontend
        jumlah = int(data.get('jumlah')) # Jumlah pack
        total = jumlah * harga

        payload = {
            'tanggal': tanggal,
            'pemesan': pemesan,
            'produk': produk,
            'jumlah': jumlah,
            'harga': harga,
            'total': total
        }

        # Kirim data ke Google Sheets via Apps Script Webhook
        requests.post(APPS_SCRIPT_URL, json=payload)

        return jsonify({'status': 'success', 'message': 'Data berhasil dicatat ke Google Sheets!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)