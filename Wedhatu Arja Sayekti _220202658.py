def encrypt(text, shift):
    result = ""

    # Loop setiap karakter di dalam teks
    for i in range(len(text)):
        char = text[i]

        # Enkripsi huruf kapital (A-Z)
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Enkripsi huruf kecil (a-z)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Jika bukan huruf, tetap tambahkan tanpa enkripsi
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Pengguna memasukkan teks dan pergeseran
text = input("Masukkan teks yang ingin dienkripsi/dekripsi: ")
shift = int(input("Masukkan nilai pergeseran (shift): "))

# Enkripsi
encrypted_text = encrypt(text, shift)
print(f"Teks terenkripsi: {encrypted_text}")

# Dekripsi
decrypted_text = decrypt(encrypted_text, shift)
print(f"Teks terdekripsi: {decrypted_text}")
