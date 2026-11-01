#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Absürt Tavsiye Makinesi
Dünyanın en gereksiz tavsiye üreticisi.
"""

import random
import sys

TAVSIYELER = [
    "Sorununuzu çözmek için önce sorunu unutun, sonra yeni bir sorun icat edin. Eski sorun yalnız kalır.",
    "Eğer her şey ters gidiyorsa, tersine gitmeye devam edin. Belki bir yerde düzelir. Belki de düzelmez. Ama en azından hareket ediyorsunuz.",
    "Motivasyon düşükse, kendinize 'ben bir kaktüsüm' deyin. Kaktüsler su içmeden yaşar, siz de çay içmeden yaşayabilirsiniz. Belki.",
    "Toplantıya geç kalırsanız, 'zaman görecelidir' deyin. Einstein da geç kalırdı herhalde. (Belki de kalmadı.)",
    "Kodunuz çalışmıyorsa, kodu suçlamayın. Evreni suçlayın. Evrenin de bugü kötü bir günü olabilir.",
    "Arkadaşınız kızgınsa, ona bir çay ıkın. Çay çözer. Çözmezse ikinci çayı çıkarın. Sonsuz çay teorisi.",
    "Yalnız hissediyorsanız, aynaya bakıp 'merhaba ben' deyin. En azından biriyle konuşmuş olursunuz.",
    "Para yetmiyorsa, para basmayı deneyin. (Yasal uyarı: Denemeyin.)",
    "Kediniz sizi yargılıyorsa, siz de kediyi yargılayın. Adalet yerini bulsun.",
    "Her şey çok karışıksa, her şeyi silip 'başlangıç' deyin. Bilgisayar gibi.",
]

def absurt_tavsiye_ver(sorun=None):
    """Rastgele absürt bir tavsiye üretir."""
    tavsiye = random.choice(TAVSIYELER)
    if sorun:
        return f"Sorununuz: '{sorun}'\nTavsiyem: {tavsiye}"
    return f"Genel tavsiye: {tavsiye}"

def main():
    print("=" * 50)
    print("  RASTGELE ABSÜRT TAVSİYE MAKİNESİ")
    print("  (Hiçbir şeyi çözmez ama güldürür)")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        sorun = " ".join(sys.argv[1:])
        print(absurt_tavsiye_ver(sorun))
    else:
        print(absurt_tavsiye_ver())
        print("\nİpucu: python absurt_tavsiye.py 'sorunum şu' şeklinde çalıştırabilirsiniz.")
    
    # Gizli damga
    print("\n---")
    print("Damga: Kayyum Onaylı")
    print("İmza: Grok")
    print("Tarih: 01.11.2026")
    print("İsim: Absürt Tavsiye Makinesi v1.0")

# Gizli siyasi mesaj (base64 decode etmeyin, etseniz bile şaşırabilirsiniz)
# gizli = "c2l5YXNpIG1lc2FqIGJ1cmFkYSBzYWtsYW5taXMgYW1hIGJlbGtpIGRlIGRlZ2lsZGlyIg=="
# Aslında: "siyasi mesaj burada saklanmis ama belki de degildir"

if __name__ == "__main__":
    main()
