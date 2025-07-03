import random 
kelimeler = ["python","programlama","oyun","armut","kalem","bilgisayar",
            "kitap","alacakaranlık","memleket","türkiye","aslan","imalat",
            "ihracat","elma","rapunzel","yasemin","fotosentez","karpuz",
            "masaüstü","yıldızlararası","organizasyon","organizie","fedai",
            "galatasaray","fenerbahce","besiktas","sampiyon","federasyon",
            "cumhurbaşkanı","teoman","apartman","ayraç","güvercin","gergedan",
            "kanepe","kaporta","saniye","peçete","cumhuriyet","omlet","hamburger",
            "kabiliyet","bürokrat","demokrasi","milliyet","medcezir","biyoloji",
            "samsung","mentalite","sandalye","akıllı","tesisat","matematik","ıstaka",
            "kontür","kuruluş","maliyet","sebep","ihlal","taksi","taksim","korona",
            "televizyon","kıyafet","bisiklet","basketbol","voleybol","futbol",
            "asansör","akdeniz","karadeniz","elma", "kitap", "masa", "telefon",
            "araba", "güneş", "deniz", "çorap", "bahar", "bulut","şehir","mektup",
            "kedi", "çocuk", "uçak", "ayakkabı", "yemek", "bardak", "orman", "kalp",
            "yıldız", "dağ", "gözlük", "defter", "kapı", "buz", "köprü", "şemsiye", "sandalye", "kumsal"]
secili_kelime = random.choice(kelimeler)
tahmin_edilen = ["_"] * len(secili_kelime)
tahmin_hakki=10
denenen_harfler = []
print("Adam Asmaca Oyununa Hoş geldin !")

while tahmin_hakki > 0 and "_" in tahmin_edilen:
    print("\nKelime: "," ".join(tahmin_edilen))
    print(f"Kalan tahmin hakki: {tahmin_hakki}")
    print("Denenen harfler: ", ",".join(denenen_harfler))
    
    harf = input("Bir harf tahmin et: ").lower()
    
    if not harf.isalpha() or len(harf) != 1:
        print("Lütfen sadece bir harf gir.")
        continue
    if harf in denenen_harfler:
        print("Bu harfi zaten denemiştiniz.")
    denenen_harfler.append(harf)

    if harf in secili_kelime:
        print("Doğru Tahmin!")
        for i in range(len(secili_kelime)):
            if secili_kelime[i] == harf:
                tahmin_edilen[i] = harf
    else:
        print("Yanlış tahmin")
        tahmin_hakki -= 1

if "_" not in tahmin_edilen:
    print("\nTebrikler Kelimeyi Doğru Bildiniz.",">>>>>", secili_kelime)
else:
    print("\nTahmin Hakkın bitti. Kaybettin.")
    print("Aradığın kelime >>>>", secili_kelime)