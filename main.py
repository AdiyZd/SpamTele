import asyncio
from telegram.ext import Application

async def kirim_pesan(app, chat_id, text, jumlah):
    """Fungsi untuk mengirim pesan ke Telegram"""
    for i in range(jumlah):
        await app.bot.send_message(chat_id=chat_id, text=text)
        print(f"Pesan ke-{i+1} dikirim.")
        await asyncio.sleep(0.02)  # Tunggu 20 ms sebelum mengirim pesan berikutnya
    print("Selesai mengirim semua pesan!")

async def start():
    # Token bot Telegram
    A_TOKEN = "7688094611:AAElQKUmzUVdoqeTUAUsqWL1O0lLzCToLt4"
    app = Application.builder().token(A_TOKEN).build()

    # Input ID target dan pesan
    T_ID = input("Masukkan ID target yang mau di-spam: ")
    text = input("Masukkan pesan yang ingin dikirim: ")

    # Input jumlah pesan
    print("Mau berapa kali kirimnya?")
    print("1. 100x")
    print("2. 200x")
    print("3. 300x")
    print("4. 400x")

    pilihan = input("Masukkan angka pilihan Anda: ")
    jumlah = {"1": 100, "2": 200, "3": 300, "4": 400}.get(pilihan, 0)

    if jumlah == 0:
        print("Pilihan tidak valid!")
        return await start()

    # Kirim pesan
    await kirim_pesan(app, chat_id=T_ID, text=text, jumlah=jumlah)

    # Mulai polling untuk menangani event
    await app.initialize()
    await app.start()
    await app.stop()
    await app.shutdown()

def main():
    asyncio.run(start())

if __name__ == "__main__":
    main()
