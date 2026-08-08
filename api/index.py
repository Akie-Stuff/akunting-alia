from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd
from datetime import datetime

# Arahkan folder templates karena index.py berada di dalam folder api/
app = Flask(__name__, template_folder='../templates')

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
        df['Jumlah'] = pd.to_numeric(df['Jumlah'], errors='coerce').fillna(0)
        df['Harga_Satuan'] = pd.to_numeric(df['Harga_Satuan'], errors='coerce').fillna(0)
        df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0)
        
        rekap_harian = df.groupby('Tanggal')['Total'].sum().reset_index().to_dict(orient='records')
        
        return jsonify({
            'transaksi': df.to_dict(orient='records'),
            'tren': rekap_harian
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/penjualan', methods=['POST'])
def add_penjualan():
    try:
        data = request.json
        tanggal = data.get('tanggal') or datetime.now().strftime('%Y-%m-%d')
        produk = data.get('produk')
        jumlah = int(data.get('jumlah'))
        harga = int(data.get('harga'))
        total = jumlah * harga

        payload = {
            'tanggal': tanggal,
            'produk': produk,
            'jumlah': jumlah,
            'harga': harga,
            'total': total
        }

        requests.post(APPS_SCRIPT_URL, json=payload)

        return jsonify({'status': 'success', 'message': 'Data berhasil dicatat ke Google Sheets!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Wajib untuk running lokal jika diperlukan
if __name__ == '__main__':
    app.run(debug=True, port=5000)