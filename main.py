from PyPDF2 import PdfReader, PdfWriter

# Orijinal PDF dosyasını oku
reader = PdfReader("EvritimNotlar.pdf")

# Yeni PDF dosyasını oluştur
writer = PdfWriter()

# Kaçıncı sayfadan sonra istiyorsan, oradan itibaren ekle (örneğin 5. sayfa ve sonrası)
start_page = 18  # Sayfa numaraları 0'dan başlar, yani 5. sayfa için 4 yazılır
for page_num in range(start_page, len(reader.pages)):
    writer.add_page(reader.pages[page_num])

# Yeni PDF'yi kaydet
with open("yeni_belge.pdf", "wb") as f:
    writer.write(f)

print("Yeni PDF başarıyla oluşturuldu.")
