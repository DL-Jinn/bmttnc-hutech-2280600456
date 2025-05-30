from .alphabet import ALPHABET

class CaesarCipher:
    def encrypt_text(self, plain_text, key):
        result = ''
        for char in plain_text.upper():
            if char in ALPHABET:
                idx = (ALPHABET.index(char) + key) % len(ALPHABET)
                result += ALPHABET[idx]
            else:
                result += char
        return result

    def decrypt_text(self, cipher_text, key):
        result = ''
        for char in cipher_text.upper():
            if char in ALPHABET:
                idx = (ALPHABET.index(char) - key) % len(ALPHABET)
                result += ALPHABET[idx]
            else:
                result += char
        return result
