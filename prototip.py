import osmnx as ox
import random

# 1. Veri Toplama (küçük ve hızlı alan)
print("📡 Denizli merkez yol ağı alınıyor...")
G = ox.graph_from_point((37.7765, 29.0864), dist=1000, network_type="drive")

# Kavşak yoğunluklarını bağlantı sayısıyla temsil edelim
kavsak_yogunluk = {}
for node in G.nodes:
    baglanti = len(list(G.neighbors(node)))
    if baglanti > 2:
        kavsak_yogunluk[node] = baglanti

# En yoğun 5 kavşağı al
en_yogun = sorted(kavsak_yogunluk.items(), key=lambda x: x[1], reverse=True)[:5]

# 2. Mevcut ışık süreleri (simülasyon) — rastgele atıyoruz
onceki_sureler = {}
for kavsak, _ in en_yogun:
    onceki_sureler[kavsak] = random.choice([20, 25, 30, 35, 40])

# 3. Karar: Yoğunluk oranına göre yeni süre hesapla
toplam_yogunluk = sum([y for _, y in en_yogun])
print("\n🔄 GreenSync Güncelleme Raporu:\n")

for i, (kavsak, yogunluk) in enumerate(en_yogun, 1):
    onceki = onceki_sureler[kavsak]
    oran = yogunluk / toplam_yogunluk
    yeni = round(oran * 60)  # 60 sn toplam döngü süresi

    fark = yeni - onceki

    print(f"{i}. Kavşak ID: {kavsak}")
    print(f"   🔸 Yoğunluk: {yogunluk}")
    print(f"   ⏱️ Önceki süre: {onceki} sn")
    print(f"   ⏱️ Yeni süre: {yeni} sn")

    if fark > 0:
        print(f"   🟢 Yeşil ışık süresi {fark} sn **artırıldı**.\n")
    elif fark < 0:
        print(f"   🔴 Yeşil ışık süresi {abs(fark)} sn **azaltıldı**.\n")
    else:
        print(f"   🟡 Yeşil ışık süresi **değişmedi**.\n")
