def menghitung_frekuensi(kalimat, kata):
    
    kalimat = kalimat.lower()
    kate = kalimat.split()
    f = kate.count(kata)

    return f

kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata = "makan"
f = menghitung_frekuensi(kalimat, kata)

print(f"kata {kata} ada {f} buah")