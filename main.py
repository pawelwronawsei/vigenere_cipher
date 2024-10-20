import tkinter as tk

alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę',
            'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł',
            'm', 'n', 'ń', 'o', 'ó', 'p', 'q', 'r',
            's', 'ś', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'ź', 'ż']

key_table = [alphabet[i:] + alphabet[:i] for i in range(len(alphabet))]

def encrypt_with_key(text, key):
    encrypted_text = ''
    key_idx = -1
    for char in text:
        if char == ' ':
            encrypted_text += char
        else:
            if key_idx == len(key) - 1:
                key_idx = 0
            else:
                key_idx += 1

            encrypted_text += key[key_idx]
    return encrypted_text

def encrypt():
    input_text = encrypt_entry1.get().lower()
    key_string = encrypt_entry2.get().lower()

    if not len(input_text) or any(char not in alphabet + [' '] for char in input_text):
        encrypt_response.config(text="Wpisz poprawny tekst!")
    elif not len(key_string) or any(char not in alphabet + [' '] for char in key_string):
        encrypt_response.config(text="Wpisz poprawny klucz!")
    else:
        text_encrypted_with_key = encrypt_with_key(input_text, key_string)
        new_text = ''

        for i in range(len(input_text)):
            if  input_text[i] == ' ':
                new_text += ' '
            else:
                row_idx = alphabet.index(input_text[i])
                col_idx = alphabet.index(text_encrypted_with_key[i])

                new_text += key_table[row_idx][col_idx]

        encrypt_response.config(text=new_text.upper())


def decrypt():
    input_text = decrypt_entry1.get().lower()
    key_string = decrypt_entry2.get().lower()

    if not len(input_text) or any(char not in alphabet + [' '] for char in input_text):
        decrypt_response.config(text="Wpisz poprawny tekst!")
    elif not len(key_string) or any(char not in alphabet + [' '] for char in key_string):
        decrypt_response.config(text="Wpisz poprawny klucz!")
    else:
        text_encrypted_with_key = encrypt_with_key(input_text, key_string)
        decrypted_text = ''

        for i in range(len(input_text)):
            if input_text[i] == ' ':
                decrypted_text += ' '
            else:
                col_idx = alphabet.index(text_encrypted_with_key[i])
                for row in key_table:
                    if row[col_idx] == input_text[i]:
                        decrypted_text += row[0]

        decrypt_response.config(text=decrypted_text.upper())


root = tk.Tk()
root.title("Szyfr Vigenere")
root.geometry("800x400")

root.configure(bg="#0D1B2A")

# SZYFROWANIE (ENCRYPTION)
encrypt_box = tk.Frame(root, padx=10, pady=10, bg="#0D1B2A")
encrypt_box.pack(pady=20)

encrypt_label0 = tk.Label(encrypt_box, text="SZYFROWANIE", bg="#0D1B2A", fg="#E0E1DD", font=("Helvetica", 16))
encrypt_label0.grid(row=0, column=0, columnspan=2, pady=10)

enccrypt_label1 = tk.Label(encrypt_box, text="Tekst do zaszyfrowania:", bg="#0D1B2A", fg="#E0E1DD")
enccrypt_label1.grid(row=1, column=0, pady=10)

encrypt_entry1 = tk.Entry(encrypt_box, width=50, bg="#1B263B", fg="#E0E1DD", insertbackground='#E0E1DD')
encrypt_entry1.grid(row=1, column=1, pady=10)

enccrypt_label2 = tk.Label(encrypt_box, text="Klucz:", bg="#0D1B2A", fg="#E0E1DD")
enccrypt_label2.grid(row=2, column=0, pady=10)

encrypt_entry2 = tk.Entry(encrypt_box, width=50, bg="#1B263B", fg="#E0E1DD", insertbackground='#E0E1DD')
encrypt_entry2.grid(row=2, column=1, pady=10)

encrypt_btn = tk.Button(encrypt_box, text="Szyfruj", command=encrypt, bg="#415A77", fg="#E0E1DD")
encrypt_btn.grid(row=3, column=0, columnspan=2, pady=10)

encrypt_response = tk.Label(encrypt_box, text="", bg="#0D1B2A", fg="#A9D6E5")  # Light blue text for encrypted response
encrypt_response.grid(row=4, column=0, columnspan=2)

# DESZYFROWANIE (DECRYPTION)
decrypt_box = tk.Frame(root, padx=10, pady=10, bg="#0D1B2A")
decrypt_box.pack(pady=20)

decrypt_label0 = tk.Label(decrypt_box, text="DESZYFROWANIE", bg="#0D1B2A", fg="#E0E1DD", font=("Helvetica", 16))
decrypt_label0.grid(row=0, column=0, columnspan=2, pady=10)

deccrypt_label1 = tk.Label(decrypt_box, text="Tekst do odszyfrowania:", bg="#0D1B2A", fg="#E0E1DD")
deccrypt_label1.grid(row=1, column=0, pady=10)

decrypt_entry1 = tk.Entry(decrypt_box, width=50, bg="#1B263B", fg="#E0E1DD", insertbackground='#E0E1DD')
decrypt_entry1.grid(row=1, column=1, pady=10)

deccrypt_label2 = tk.Label(decrypt_box, text="Klucz", bg="#0D1B2A", fg="#E0E1DD")
deccrypt_label2.grid(row=2, column=0, pady=10)

decrypt_entry2 = tk.Entry(decrypt_box, width=50, bg="#1B263B", fg="#E0E1DD", insertbackground='#E0E1DD')
decrypt_entry2.grid(row=2, column=1, pady=10)

decrypt_btn = tk.Button(decrypt_box, text="Odszyfruj", command=decrypt, bg="#415A77", fg="#E0E1DD")
decrypt_btn.grid(row=3, column=0, columnspan=2, pady=10)

decrypt_response = tk.Label(decrypt_box, text="", bg="#0D1B2A", fg="#A9D6E5")  # Light blue text for decrypted response
decrypt_response.grid(row=4, column=0, columnspan=2)

root.mainloop()
