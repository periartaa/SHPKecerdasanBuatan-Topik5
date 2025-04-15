# Penalaran berbasis aturan (rule-based reasoning)
rules = {
    ("A", "A") : ["A", "O"],
    ("B", "A") : ["A", "B", "AB", "O"],
    ("AB", "A") : ["A", "B", "AB"],
    ("O", "A") : ["A", "O"],
    
    ("A", "B") : ["A", "B", "AB", "O"],
    ("B", "B") : ["B", "O"],
    ("AB", "B") : ["A", "B", "AB"],
    ("O", "B") : ["B", "O"],
    
    ("A", "AB") : ["A", "B", "AB"],
    ("B", "AB") : ["A", "B", "AB"],
    ("AB", "AB") : ["A", "B", "AB"],
    ("O", "AB") : ["A", "B"],
    
    ("A", "O") : ["A", "O"],
    ("B", "O") : ["B", "O"],
    ("AB", "O") : ["A", "B"],
    ("O", "O") : ["O"]  
}

print("SISTEM PAKAR PREDIKSI GOLONGAN DARAH ANAK")
print("----------------------------------------")

# Input golongan darah orang tua
ayah = input("Jika suami bergolonagn darah (A/B/AB/O): ").upper()
ibu = input("Istri bergolongan darah (A/B/AB/O): ").upper()

# Cek kemungkinan golongan darah anak
hasil = rules.get((ayah, ibu), ["Tidak Valid"])

# Cek hasil
print(f"\nKemungkinan golongan darah anak: {', '.join(hasil)}")

# catatan
print("\nCatatan:")
print("- Sistem ini memprediksi berdasarkan aturan pewarisan golongan darah A, B, AB, O")
print("- Untuk hasil pasti, disarankan melakukan tes laboratorium")