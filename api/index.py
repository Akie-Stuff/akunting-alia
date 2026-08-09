<!DOCTYPE html>
<html lang="id">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Penjualan - Risol Alia</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'brand-primary': '#4F46E5',    // Indigo-600
                        'brand-hover': '#4338CA',      // Indigo-700
                        'brand-light': '#EEF2FF',      // Indigo-50
                        'accent-success': '#10B981',   // Emerald-500
                        'surface-card': '#FFFFFF',
                        'surface-bg': '#F8FAFC'        // Slate-50
                    },
                    fontFamily: {
                        'sans': ['"Inter"', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #F8FAFC;
        }

        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }

        ::-webkit-scrollbar-track {
            background: #F1F5F9;
        }

        ::-webkit-scrollbar-thumb {
            background: #CBD5E1;
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #94A3B8;
        }
    </style>
</head>

<body class="p-4 md:p-8 text-slate-800">

    <div class="max-w-7xl mx-auto space-y-6">

        <!-- Header -->
        <header class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
                <h1 class="text-2xl font-bold text-slate-900 tracking-tight">
                    Dashboard Penjualan Risol Alia
                </h1>
                <p class="text-slate-500 text-sm mt-1">Sistem pencatatan transaksi dan analisis pendapatan harian.</p>
            </div>
            <div class="text-xs text-slate-400 bg-slate-50 px-3 py-2 rounded-lg border border-slate-100 self-start md:self-auto">
                Status Sistem: <span class="text-emerald-600 font-semibold">● Terhubung</span>
            </div>
        </header>

        <!-- Form Input -->
        <section class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <div class="flex items-center gap-2 mb-5 pb-3 border-b border-slate-100">
                <svg class="w-5 h-5 text-brand-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <h2 class="text-lg font-semibold text-slate-900">Input Transaksi Baru</h2>
            </div>
            
            <form id="salesForm" class="space-y-5">
                <!-- Informasi Transaksi Utama -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-1">Tanggal Transaksi</label>
                        <input type="date" id="tanggal" required
                            class="w-full p-2.5 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-primary focus:border-brand-primary bg-white">
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-1">Nama Pemesan</label>
                        <input type="text" id="pemesan" placeholder="Masukkan nama pelanggan" required
                            class="w-full p-2.5 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-primary focus:border-brand-primary bg-white">
                    </div>
                </div>

                <!-- Container Item Pesanan Dynamic -->
                <div class="bg-slate-50 p-4 rounded-lg border border-slate-200 space-y-3">
                    <label class="block text-xs font-semibold text-slate-600 uppercase tracking-wider">Rincian Item Pesanan</label>
                    <div id="itemsContainer" class="space-y-2">
                        <!-- Row pesanan item pertama -->
                        <div class="item-row grid grid-cols-1 md:grid-cols-12 gap-2 items-center">
                            <div class="md:col-span-7">
                                <select class="produkSelect w-full p-2.5 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-primary bg-white" required>
                                    <option value="" data-harga="0">-- Pilih Varian Produk --</option>
                                    <option value="Matcha Cheese (Isi 5)" data-harga="20000">Matcha Cheese (Rp 20.000)</option>
                                    <option value="Choco Cheese (Isi 5)" data-harga="20000">Choco Cheese (Rp 20.000)</option>
                                    <option value="Ragout Ayam (Isi 5)" data-harga="20000">Ragout Ayam (Rp 20.000)</option>
                                    <option value="Beef Bolognese (Isi 5)" data-harga="20000">Beef Bolognese (Rp 20.000)</option>
                                    <option value="Mix Manis (6 Pcs)" data-harga="24000">Mix Manis 6 Pcs (Rp 24.000)</option>
                                    <option value="Mix Asin (6 Pcs)" data-harga="24000">Mix Asin 6 Pcs (Rp 24.000)</option>
                                    <option value="Mix All Varian (8 Pcs)" data-harga="32000">Mix All Varian 8 Pcs (Rp 32.000)</option>
                                </select>
                            </div>
                            <div class="md:col-span-4">
                                <div class="relative">
                                    <input type="number" class="jumlahInput w-full p-2.5 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-primary bg-white pr-12" min="1" value="1" placeholder="Jumlah" required>
                                    <span class="absolute right-3 top-2.5 text-xs text-slate-400 font-medium pointer-events-none">Pack</span>
                                </div>
                            </div>
                            <div class="md:col-span-1 text-center">
                                <button type="button" class="removeItemBtn text-slate-400 hover:text-red-500 font-bold p-1 transition hidden" title="Hapus Item">
                                    <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Button Tambah Varian -->
                    <button type="button" id="addItemBtn" class="mt-2 text-xs bg-white text-slate-700 font-medium px-3 py-2 rounded-md hover:bg-slate-100 border border-slate-300 transition shadow-sm inline-flex items-center gap-1">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                        Tambah Varian Lain
                    </button>
                </div>

                <div class="pt-2 flex justify-end">
                    <button type="submit" id="submitBtn"
                        class="w-full md:w-auto bg-brand-primary text-white font-medium py-2.5 px-6 rounded-lg hover:bg-brand-hover transition shadow-sm inline-flex items-center justify-center gap-2 text-sm">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4"></path></svg>
                        Simpan Transaksi
                    </button>
                </div>
            </form>
        </section>

        <!-- Grafik & Ringkasan -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <section class="lg:col-span-2 bg-white p-6 rounded-xl shadow-sm border border-slate-200">
                <div class="flex items-center justify-between mb-4 pb-2 border-b border-slate-100">
                    <h2 class="text-base font-semibold text-slate-900">Tren Penjualan Harian</h2>
                    <span class="text-xs text-slate-400">7 Hari Terakhir</span>
                </div>
                <div class="relative w-full h-64 md:h-72">
                    <canvas id="salesChart"></canvas>
                </div>
            </section>

            <section class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between mb-4 pb-2 border-b border-slate-100">
                        <h2 class="text-base font-semibold text-slate-900">Pendapatan Hari Ini</h2>
                        <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-emerald-50 text-emerald-700 border border-emerald-200">
                            Terbaru
                        </span>
                    </div>
                    <div class="py-6 px-4 bg-slate-50 rounded-lg border border-slate-100 text-center my-2">
                        <p class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Total Omset</p>
                        <p id="todayRevenue" class="text-3xl font-bold text-slate-900 mt-2">Rp 0</p>
                    </div>
                </div>
                <p class="text-xs text-slate-400 text-center">Kalkulasi berdasarkan data transaksi tanggal paling baru.</p>
            </section>
        </div>

        <!-- Tabel Riwayat -->
        <section class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <div class="flex items-center justify-between mb-4 pb-2 border-b border-slate-100">
                <h2 class="text-base font-semibold text-slate-900">Riwayat Transaksi</h2>
                <span class="text-xs text-slate-500">Tergabung per Pemesan</span>
            </div>
            <div class="overflow-x-auto rounded-lg border border-slate-200">
                <table class="w-full text-left table-auto text-sm">
                    <thead>
                        <tr class="bg-slate-50 text-slate-600 font-semibold border-b border-slate-200 text-xs uppercase tracking-wider">
                            <th class="p-3.5">Tanggal</th>
                            <th class="p-3.5">Nama Pemesan</th>
                            <th class="p-3.5">Rincian Varian</th>
                            <th class="p-3.5 text-center">Total Volume</th>
                            <th class="p-3.5 text-right">Total Pembayaran</th>
                        </tr>
                    </thead>
                    <tbody id="tableBody" class="divide-y divide-slate-100 text-slate-700">
                        <tr>
                            <td colspan="5" class="p-8 text-center text-slate-400 bg-white">
                                Memuat data transaksi...
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

    </div>

    <script>
        let chartInstance = null;
        document.getElementById('tanggal').valueAsDate = new Date();

        function formatRupiah(angka) {
            return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', minimumFractionDigits: 0 }).format(angka).replace('IDR', 'Rp');
        }

        // Fungsi Menambah Field Varian
        document.getElementById('addItemBtn').addEventListener('click', () => {
            const container = document.getElementById('itemsContainer');
            const firstRow = container.querySelector('.item-row');
            const newRow = firstRow.cloneNode(true);
            
            // Reset input values
            newRow.querySelector('.produkSelect').selectedIndex = 0;
            newRow.querySelector('.jumlahInput').value = 1;
            
            // Tampilkan tombol hapus
            const removeBtn = newRow.querySelector('.removeItemBtn');
            removeBtn.classList.remove('hidden');
            removeBtn.addEventListener('click', () => newRow.remove());

            container.appendChild(newRow);
        });

        async function loadData() {
            try {
                const res = await fetch('/api/penjualan');
                const data = await res.json();

                const tableBody = document.getElementById('tableBody');
                tableBody.innerHTML = '';

                if (!data.transaksi || data.transaksi.length === 0) {
                    tableBody.innerHTML = `<tr><td colspan="5" class="p-8 text-center text-slate-400">Belum ada transaksi tercatat.</td></tr>`;
                    document.getElementById('todayRevenue').innerText = 'Rp 0';
                } else {
                    // Grouping berdasarkan Tanggal + Nama Pemesan
                    const groupedMap = new Map();

                    data.transaksi.forEach(item => {
                        const dateFormatted = item.Tanggal ? String(item.Tanggal).split('T')[0] : '-';
                        const pemesanName = (item.Nama_Pemesan || '-').trim();
                        const key = `${dateFormatted}_${pemesanName.toLowerCase()}`;

                        if (!groupedMap.has(key)) {
                            groupedMap.set(key, {
                                Tanggal: dateFormatted,
                                Nama_Pemesan: pemesanName,
                                items: [],
                                totalPack: 0,
                                totalHarga: 0
                            });
                        }

                        const group = groupedMap.get(key);
                        const qty = Number(item.Jumlah) || 0;
                        const total = Number(item.Total) || 0;

                        group.items.push({
                            produk: item.Nama_Produk || '-',
                            jumlah: qty,
                            total: total
                        });
                        group.totalPack += qty;
                        group.totalHarga += total;
                    });

                    const sortedGroups = Array.from(groupedMap.values()).sort((a, b) => new Date(b.Tanggal) - new Date(a.Tanggal));

                    sortedGroups.forEach((group, index) => {
                        const tr = document.createElement('tr');
                        tr.className = 'hover:bg-slate-50 transition-colors';

                        // Format list varian
                        const itemListHtml = group.items.map(i => 
                            `<div class="text-xs leading-relaxed"><span class="font-medium text-slate-800">• ${i.produk}</span> <span class="text-slate-400">(${i.jumlah} pack - ${formatRupiah(i.total)})</span></div>`
                        ).join('');

                        tr.innerHTML = `
                            <td class="p-3.5 font-mono text-xs text-slate-500 align-top">${group.Tanggal}</td>
                            <td class="p-3.5 font-semibold text-slate-800 align-top">${group.Nama_Pemesan}</td>
                            <td class="p-3.5 align-top">${itemListHtml}</td>
                            <td class="p-3.5 text-center font-medium text-slate-700 align-top">${group.totalPack} pack</td>
                            <td class="p-3.5 text-right font-semibold text-slate-900 align-top">${formatRupiah(group.totalHarga)}</td>
                        `;
                        tableBody.appendChild(tr);
                    });

                    const latestDate = sortedGroups[0]?.Tanggal;
                    const latestRevenue = data.tren?.find(t => String(t.Tanggal).split('T')[0] === latestDate)?.Total || 0;
                    document.getElementById('todayRevenue').innerText = formatRupiah(latestRevenue);
                }

                // Handling Grafik
                if (data.tren) {
                    const limitedTren = data.tren.slice(-7);
                    const labels = limitedTren.map(t => t.Tanggal ? String(t.Tanggal).split('T')[0] : '');
                    const totals = limitedTren.map(t => t.Total);

                    if (chartInstance) chartInstance.destroy();

                    const ctx = document.getElementById('salesChart').getContext('2d');
                    let gradient = ctx.createLinearGradient(0, 0, 0, 300);
                    gradient.addColorStop(0, 'rgba(79, 70, 229, 0.2)');
                    gradient.addColorStop(1, 'rgba(79, 70, 229, 0.0)');

                    chartInstance = new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: labels,
                            datasets: [{
                                label: 'Pendapatan (Rp)',
                                data: totals,
                                borderColor: '#4F46E5',
                                borderWidth: 2.5,
                                backgroundColor: gradient,
                                pointBackgroundColor: '#4F46E5',
                                fill: true,
                                tension: 0.3
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: { legend: { display: false } },
                            scales: { 
                                y: { 
                                    beginAtZero: true,
                                    grid: { color: '#F1F5F9' },
                                    ticks: { font: { family: 'Inter', size: 11 } }
                                },
                                x: {
                                    grid: { display: false },
                                    ticks: { font: { family: 'Inter', size: 11 } }
                                }
                            }
                        }
                    });
                }
            } catch (err) {
                console.error("Gagal memuat data:", err);
            }
        }

        // Submit Form Handler
        document.getElementById('salesForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = document.getElementById('submitBtn');
            submitBtn.disabled = true;

            const tanggalVal = document.getElementById('tanggal').value;
            const inputPemesan = document.getElementById('pemesan').value.trim() || "-";
            
            const itemRows = document.querySelectorAll('.item-row');
            const requests = [];

            itemRows.forEach(row => {
                const selectEl = row.querySelector('.produkSelect');
                const selectedOption = selectEl.options[selectEl.selectedIndex];
                const produkNama = selectEl.value;
                const produkHarga = Number(selectedOption.getAttribute('data-harga')) || 0;
                const jumlahPack = Number(row.querySelector('.jumlahInput').value) || 1;

                if (produkNama) {
                    const payload = {
                        tanggal: tanggalVal,
                        pemesan: inputPemesan,
                        produk: produkNama,
                        jumlah: jumlahPack,
                        harga: produkHarga,
                        total: produkHarga * jumlahPack
                    };

                    requests.push(
                        fetch('/api/penjualan', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify(payload)
                        })
                    );
                }
            });

            try {
                await Promise.all(requests);

                // Reset Form
                document.getElementById('pemesan').value = '';
                const container = document.getElementById('itemsContainer');
                container.innerHTML = `
                    <div class="item-row grid grid-cols-1 md:grid-cols-12 gap-2 items-center">
                        <div class="md:col-span-7">
                            <select class="produkSelect w-full p-2.5 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-primary bg-white" required>
                                <option value="" data-harga="0">-- Pilih Varian Produk --</option>
                                <option value="Matcha Cheese (Isi 5)" data-harga="20000">Matcha Cheese (Rp 20.000)</option>
                                <option value="Choco Cheese (Isi 5)" data-harga="20000">Choco Cheese (Rp 20.000)</option>
                                <option value="Ragout Ayam (Isi 5)" data-harga="20000">Ragout Ayam (Rp 20.000)</option>
                                <option value="Beef Bolognese (Isi 5)" data-harga="20000">Beef Bolognese (Rp 20.000)</option>
                                <option value="Mix Manis (6 Pcs)" data-harga="24000">Mix Manis 6 Pcs (Rp 24.000)</option>
                                <option value="Mix Asin (6 Pcs)" data-harga="24000">Mix Asin 6 Pcs (Rp 24.000)</option>
                                <option value="Mix All Varian (8 Pcs)" data-harga="32000">Mix All Varian 8 Pcs (Rp 32.000)</option>
                            </select>
                        </div>
                        <div class="md:col-span-4">
                            <div class="relative">
                                <input type="number" class="jumlahInput w-full p-2.5 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-brand-primary bg-white pr-12" min="1" value="1" placeholder="Jumlah" required>
                                <span class="absolute right-3 top-2.5 text-xs text-slate-400 font-medium pointer-events-none">Pack</span>
                            </div>
                        </div>
                        <div class="md:col-span-1 text-center">
                            <button type="button" class="removeItemBtn text-slate-400 hover:text-red-500 font-bold p-1 transition hidden" title="Hapus Item">
                                <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                                </svg>
                            </button>
                        </div>
                    </div>
                `;

                await loadData();
            } catch (err) {
                alert('Gagal mengirim data ke server!');
            } finally {
                submitBtn.disabled = false;
            }
        });

        loadData();
    </script>
</body>

</html>