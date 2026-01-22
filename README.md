# 🎬 YouTube Video Downloader & Clipper

Script Python untuk mendownload video YouTube dengan kualitas tertinggi dan memotong video sesuai kebutuhan.

## ✨ Fitur

- ✅ Download video YouTube dengan **kualitas tertinggi**
- ✂️ Potong video (hanya download bagian yang diperlukan - **hemat bandwidth**)
- 📁 Pilih folder penyimpanan sendiri
- ⚡ Download cepat dengan yt-dlp
- 🎨 Interface CLI yang user-friendly

---

## 📋 Persyaratan Sistem

Sebelum menggunakan script ini, pastikan sistem Anda sudah terinstall:
- Python 3.7 atau lebih baru
- pip (package manager Python)

---

## 🔧 Instalasi

### 1️⃣ Install Python Dependencies

```bash
pip install yt-dlp
```

### 2️⃣ Install FFmpeg

FFmpeg diperlukan untuk memproses video.

#### **Windows:**

**Cara 1: Menggunakan Chocolatey (Recommended)**
```bash
choco install ffmpeg
```

**Cara 2: Manual Download**
1. Download FFmpeg dari [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract file zip
3. Tambahkan folder `bin` ke System PATH
4. Restart terminal/command prompt

**Cara 3: Menggunakan Scoop**
```bash
scoop install ffmpeg
```

#### **macOS:**

```bash
brew install ffmpeg
```

#### **Linux (Ubuntu/Debian):**

```bash
sudo apt update
sudo apt install ffmpeg
```

#### **Linux (Fedora):**

```bash
sudo dnf install ffmpeg
```

---

## 🚀 Cara Menggunakan

### 1️⃣ Download Script

Simpan script Python dengan nama `youtube_downloader.py`

### 2️⃣ Jalankan Script

```bash
python youtube_downloader.py
```

### 3️⃣ Ikuti Petunjuk

#### **Contoh 1: Download Video Full**

```
🔗 Masukkan URL YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ

📺 Judul  : Never Gonna Give You Up
⏱ Durasi : 03:32 (mm:ss)

📁 PILIH LOKASI PENYIMPANAN:
1️⃣  Folder saat ini
2️⃣  Pilih folder lain

Masukkan pilihan (1/2): 1
✅ File akan disimpan di: C:\Users\YourName\Videos

PILIH MENU:
1️⃣  Download video FULL (kualitas tertinggi)
2️⃣  Download + POTONG video (hanya bagian yang dipilih)

Masukkan pilihan (1/2): 1

⬇  Mendownload video dengan kualitas tertinggi...

✅ Selesai!
📁 File: C:\Users\YourName\Videos\Never Gonna Give You Up.mp4
```

#### **Contoh 2: Download & Potong Video**

```
🔗 Masukkan URL YouTube: https://www.youtube.com/watch?v=dQw4w9WgXcQ

📺 Judul  : Never Gonna Give You Up
⏱ Durasi : 03:32 (mm:ss)

📁 PILIH LOKASI PENYIMPANAN:
1️⃣  Folder saat ini
2️⃣  Pilih folder lain

Masukkan pilihan (1/2): 2

📂 Masukkan path folder: C:/Downloads
✅ File akan disimpan di: C:/Downloads

PILIH MENU:
1️⃣  Download video FULL (kualitas tertinggi)
2️⃣  Download + POTONG video (hanya bagian yang dipilih)

Masukkan pilihan (1/2): 2

✂  Waktu MULAI (mm:ss): 0:30
✂  Waktu AKHIR (mm:ss): 1:30

⬇  Mendownload bagian video yang diperlukan...
💡 Ini lebih cepat karena tidak download seluruh video
✂  Memproses video...

✅ Selesai!
📁 File hasil: C:/Downloads/CLIP_Never Gonna Give You Up.mp4
```

---

## 📖 Format Input

### URL YouTube
Masukkan URL lengkap video YouTube, contoh:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`

### Format Waktu (mm:ss)
- Gunakan format menit:detik
- Contoh: `0:30` (30 detik), `1:45` (1 menit 45 detik), `12:05` (12 menit 5 detik)

### Path Folder
- Windows: `C:/Downloads` atau `C:\Users\NamaUser\Videos`
- macOS/Linux: `/home/username/Videos` atau `~/Downloads`

---

## ⚙️ Konfigurasi Kualitas Video

Script ini otomatis mendownload video dengan **kualitas tertinggi yang tersedia**:
- Video: Resolusi tertinggi (4K, 1080p, 720p, dll)
- Audio: Bitrate tertinggi (192kbps)
- Encoding: H.264 dengan CRF 18 (kualitas tinggi)

---

## 🛠️ Troubleshooting

### ❌ Error: "yt-dlp tidak ditemukan di PATH"
**Solusi:** Install yt-dlp dengan `pip install yt-dlp`

### ❌ Error: "ffmpeg tidak ditemukan di PATH"
**Solusi:** 
1. Install FFmpeg sesuai petunjuk di atas
2. Restart terminal/command prompt
3. Verifikasi instalasi: `ffmpeg -version`

### ❌ Video tidak bisa didownload
**Solusi:**
1. Pastikan URL valid dan video bisa diakses
2. Cek koneksi internet
3. Update yt-dlp: `pip install --upgrade yt-dlp`

### ❌ Error saat memotong video
**Solusi:**
1. Pastikan format waktu benar (mm:ss)
2. Waktu akhir tidak boleh melebihi durasi video
3. Waktu mulai harus lebih kecil dari waktu akhir

### ❌ Folder tidak ditemukan
**Solusi:**
1. Cek path folder yang diinput
2. Pilih opsi untuk membuat folder baru (y)
3. Atau gunakan folder saat ini (pilih opsi 1)

---

## 💡 Tips & Trik

1. **Download Cepat**: Gunakan opsi 2 (potong video) jika hanya butuh bagian tertentu - lebih cepat dan hemat bandwidth!

2. **Organisasi File**: Buat folder khusus untuk setiap jenis video, misalnya:
   - `C:/Videos/Musik` untuk video musik
   - `C:/Videos/Tutorial` untuk tutorial
   - `C:/Videos/Klip` untuk video yang sudah dipotong

3. **Batch Download**: Untuk download banyak video, jalankan script berkali-kali atau modifikasi script untuk loop

4. **Nama File**: Script otomatis membersihkan karakter ilegal dari nama file, sehingga aman untuk semua sistem operasi

---

## 📝 Catatan Penting

- ⚖️ **Hak Cipta**: Gunakan script ini hanya untuk video yang Anda miliki hak downloadnya atau untuk penggunaan pribadi yang sah
- 🌐 **Koneksi Internet**: Pastikan koneksi internet stabil untuk hasil terbaik
- 💾 **Ruang Penyimpanan**: Pastikan ada cukup ruang disk untuk video yang akan didownload
- 🔄 **Update**: Selalu update yt-dlp ke versi terbaru untuk kompatibilitas optimal

---

## 🔄 Update yt-dlp

yt-dlp sering diupdate untuk menjaga kompatibilitas dengan YouTube. Update secara berkala:

```bash
pip install --upgrade yt-dlp
```

---

## 📄 Lisensi

Script ini gratis untuk digunakan dan dimodifikasi sesuai kebutuhan Anda.

---

## 🤝 Kontribusi

Jika menemukan bug atau ingin menambahkan fitur:
1. Fork repository ini
2. Buat branch baru
3. Commit perubahan
4. Submit pull request

---

## 📧 Support

Jika mengalami masalah:
1. Cek bagian Troubleshooting di atas
2. Pastikan semua dependencies terinstall dengan benar
3. Update semua tools ke versi ter
