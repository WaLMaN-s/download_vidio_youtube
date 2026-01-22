import yt_dlp
import shutil
import subprocess
import sys
import re
import os

# =============================
# UTIL
# =============================
def cek_dep():
    for cmd in ["yt-dlp", "ffmpeg"]:
        if shutil.which(cmd) is None:
            print(f"❌ {cmd} tidak ditemukan di PATH")
            sys.exit(1)

def valid_time(t):
    return re.match(r"^\d{1,2}:\d{2}$", t)

def sec_to_mmss(sec):
    return f"{sec//60:02d}:{sec%60:02d}"

def safe_filename(name):
    return re.sub(r'[\\/:*?"<>|]', '', name)

def pilih_folder():
    """Meminta user memilih folder penyimpanan"""
    print("\n📁 PILIH LOKASI PENYIMPANAN:")
    print("1️⃣  Folder saat ini")
    print("2️⃣  Pilih folder lain")
    
    pilih = input("\nMasukkan pilihan (1/2): ").strip()
    
    if pilih == "1":
        folder = os.getcwd()
        print(f"✅ File akan disimpan di: {folder}")
        return folder
    elif pilih == "2":
        folder = input("\n📂 Masukkan path folder (contoh: C:/Downloads atau /home/user/Videos): ").strip()
        
        # Bersihkan tanda kutip jika ada
        folder = folder.strip('"').strip("'")
        
        # Cek apakah folder ada
        if not os.path.exists(folder):
            print(f"\n⚠️  Folder tidak ditemukan. Buat folder baru? (y/n): ", end="")
            buat = input().strip().lower()
            if buat == 'y':
                try:
                    os.makedirs(folder, exist_ok=True)
                    print(f"✅ Folder berhasil dibuat: {folder}")
                except Exception as e:
                    print(f"❌ Gagal membuat folder: {e}")
                    print("📁 Menggunakan folder saat ini sebagai gantinya")
                    folder = os.getcwd()
            else:
                print("📁 Menggunakan folder saat ini")
                folder = os.getcwd()
        else:
            print(f"✅ File akan disimpan di: {folder}")
        
        return folder
    else:
        print("❌ Pilihan tidak valid, menggunakan folder saat ini")
        return os.getcwd()

# =============================
# VIDEO INFO
# =============================
def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'extractor_args': {'youtube': {'player_client': ['android']}},
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info['title'], info['duration']

# =============================
# DOWNLOAD
# =============================
def download_full(url, title, folder):
    """Download video dengan kualitas tertinggi"""
    output_path = os.path.join(folder, f'{title}.%(ext)s')
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'outtmpl': output_path,
        'extractor_args': {'youtube': {'player_client': ['android']}},
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return os.path.join(folder, f'{title}.mp4')

def download_clip(url, title, start, end, folder):
    """Download hanya bagian video yang diperlukan (lebih cepat)"""
    output_path = os.path.join(folder, f'TEMP_{title}.%(ext)s')
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': output_path,
        'extractor_args': {'youtube': {'player_client': ['android']}},
        'download_ranges': yt_dlp.utils.download_range_func(None, [(start, end)]),
        'force_keyframes_at_cuts': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return os.path.join(folder, f'TEMP_{title}.mp4')

# =============================
# CUT VIDEO
# =============================
def cut_video(input_file, start, end, output_file):
    """Potong video dengan ffmpeg"""
    cmd = [
        "ffmpeg", "-y",
        "-ss", start,
        "-i", input_file,
        "-to", end,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        output_file
    ]
    subprocess.run(cmd, check=True)

def time_to_seconds(time_str):
    """Konversi mm:ss ke detik"""
    parts = time_str.split(':')
    return int(parts[0]) * 60 + int(parts[1])

# =============================
# MAIN
# =============================
if __name__ == "__main__":
    cek_dep()
    
    url = input("🔗 Masukkan URL YouTube: ").strip()
    title, duration = get_video_info(url)
    title = safe_filename(title)
    
    print("\n📺 Judul  :", title)
    print("⏱ Durasi :", sec_to_mmss(duration), "(mm:ss)\n")
    
    # Pilih folder penyimpanan
    folder_tujuan = pilih_folder()
    
    print("\nPILIH MENU:")
    print("1️⃣  Download video FULL (kualitas tertinggi)")
    print("2️⃣  Download + POTONG video (hanya bagian yang dipilih)")
    
    pilihan = input("\nMasukkan pilihan (1/2): ").strip()
    
    if pilihan == "1":
        print("\n⬇  Mendownload video dengan kualitas tertinggi...")
        output_file = download_full(url, title, folder_tujuan)
        print("\n✅ Selesai!")
        print(f"📁 File: {output_file}")
        
    elif pilihan == "2":
        start = input("\n✂  Waktu MULAI (mm:ss): ").strip()
        end = input("✂  Waktu AKHIR (mm:ss): ").strip()
        
        if not (valid_time(start) and valid_time(end)):
            print("❌ Format waktu salah! Gunakan mm:ss")
            sys.exit(1)
        
        # Validasi waktu tidak melebihi durasi video
        start_sec = time_to_seconds(start)
        end_sec = time_to_seconds(end)
        
        if start_sec >= end_sec:
            print("❌ Waktu mulai harus lebih kecil dari waktu akhir!")
            sys.exit(1)
        
        if end_sec > duration:
            print(f"❌ Waktu akhir melebihi durasi video ({sec_to_mmss(duration)})")
            sys.exit(1)
        
        print("\n⬇  Mendownload bagian video yang diperlukan...")
        print("💡 Ini lebih cepat karena tidak download seluruh video")
        
        # Download hanya bagian yang diperlukan
        temp_file = download_clip(url, title, start_sec, end_sec, folder_tujuan)
        
        print("✂  Memproses video...")
        output_file = os.path.join(folder_tujuan, f"CLIP_{title}.mp4")
        cut_video(temp_file, "00:00", end, output_file)
        
        # Hapus file temporary
        try:
            os.remove(temp_file)
        except:
            pass
        
        print("\n✅ Selesai!")
        print(f"📁 File hasil: {output_file}")
        
    else:
        print("❌ Pilihan tidak valid")