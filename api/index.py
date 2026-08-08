from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd
from datetime import datetime

app = Flask(__name__, template_folder='../templates')

# APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzMueGMxWfi80OVHeBj6YqA4dUBqQ1T9dqJ2aUP5Ge4d5jwBeXaEpVD2fYLkwA3bGmNng/exec'
APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzKWoKDJcszLfMqjOFKJg3so8aV4UCcv--qqQxE-XehhS2tRB7TkJV7rIKIrdeQmBtF/exec'

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
        
        # Konversi numerik dengan aman
        df['Jumlah'] = pd.to_numeric(df.get('Jumlah', 0), errors='coerce').fillna(0)
        df['Harga_Satuan'] = pd.to_numeric(df.get('Harga_Satuan', 0), errors='coerce').fillna(0)
        df['Total'] = pd.to_numeric(df.get('Total', 0), errors='coerce').fillna(0)
        
        # Grouping rekap harian untuk grafik
        rekap_harian = df.groupby('Tanggal')['Total'].sum().reset_index().to_dict(orient='records')
        
        transaksi = []
        for _, row in df.iterrows():
            transaksi.append({
                'Tanggal': str(row.get('Tanggal', '')),
                'Nama_Pemesan': str(row.get('Nama_Pemesan', '-')),
                'Nama_Produk': str(row.get('Nama_Produk', '-')),
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
        data = request.get_json(force=True) or {}
        
        tanggal = str(data.get('tanggal', '')) or datetime.now().strftime('%Y-%m-%d')
        pemesan = str(data.get('pemesan', '')).strip()
        if not pemesan:
            pemesan = '-'  # Wajib ada string isi agar Apps Script tidak menggeser kolom!
            
        produk = str(data.get('produk', '-')).strip()
        
        try:
            jumlah = int(data.get('jumlah', 1))
        except (ValueError, TypeError):
            jumlah = 1

        try:
            harga = int(data.get('harga', 0))
        except (ValueError, TypeError):
            harga = 0

        # Jika total tidak dikirim dari frontend, hitung manual
        total = int(data.get('total', harga * jumlah))

        payload = {
            'tanggal': tanggal,
            'pemesan': pemesan,
            'produk': produk,
            'jumlah': jumlah,
            'harga': harga,
            'total': total
        }

        # Kirim JSON ke Google Apps Script
        res = requests.post(APPS_SCRIPT_URL, json=payload, headers={'Content-Type': 'application/json'})

        return jsonify({'status': 'success', 'message': 'Data tersimpan!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)