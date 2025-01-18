def generalized_caesar_encrypt(plain_text, shift):
    # Инициализация переменной, в которую будем складывать зашифрованный текст
    encrypted_text = ''

    # Перебираем каждый символ в исходном тексте
    for char in plain_text:
        # Проверяем, является ли символ буквой
        if char.isalpha():
            # Определяем базовый код символа. Если буква заглавная, используем код 'A', иначе - 'a'
            base = ord('A') if char.isupper() else ord('a')
            # Вычисляем зашифрованный символ, применяя сдвиг
            # Вычитаем код базового символа, добавляем сдвиг, берем по модулю 26 для оборачивания
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            # Добавляем зашифрованный символ к результату
            encrypted_text += encrypted_char
        else:
            # Если этот символ не буква (например, пробел или знак препинания), добавляем его без изменений
            encrypted_text += char

    # Возвращаем окончательный зашифрованный текст
    return encrypted_text


def generalized_caesar_decrypt(encrypted_text, shift):
    # Инициализация переменной для хранения расшифрованного текста
    decrypted_text = ''

    # Перебираем каждый символ в зашифрованном тексте
    for char in encrypted_text:
        # Проверяем, является ли символ буквой
        if char.isalpha():
            # Определяем базовый код символа так же, как и при шифровании
            base = ord('A') if char.isupper() else ord('a')
            # Вычисляем расшифрованный символ, вычитая сдвиг
            # Процедура аналогична шифрованию, но с вычитанием сдвига
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            # Добавляем расшифрованный символ к результату
            decrypted_text += decrypted_char
        else:
            # Если символ не буква, добавляем его без изменений
            decrypted_text += char

    # Возвращаем окончательный расшифрованный текст
    return decrypted_text


def frequency_analysis_decrypt(ciphertext):
    frequency = {}

    # Подсчет частоты каждой буквы в зашифрованном тексте
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char, 0) + 1

    # Сортируем буквы по их частоте в порядке убывания
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

    # Находим наиболее частую букву
    most_frequent_cipher_letter = sorted_frequency[0][0]

    # Предполагаем, что наиболее частая буква в английском языке — это 'e'
    assumed_shift = (ord(most_frequent_cipher_letter) - ord('e')) % 26

    decrypted_text = generalized_caesar_decrypt(ciphertext, assumed_shift)
    return decrypted_text


if __name__ == "__main__":
    # Проверим обобщенный шифр Цезаря
    text = "Hello, World! eeee"
    shift_value = 5  # Определяем сдвиг для шифрования
    encrypted = generalized_caesar_encrypt(text, shift_value)  # Шифруем текст
    print("Зашифрованный текст:", encrypted)  # Выводим зашифрованный текст

    decrypted = generalized_caesar_decrypt(encrypted, shift_value)  # Дешифруем текст
    print("Расшифрованный текст:", decrypted)  # Выводим расшифрованный текст

    # Проверим взлом зашифрованного текста
    decrypted = frequency_analysis_decrypt(encrypted)
    print("Расшифрованный текст:", decrypted)  # Выводим расшифрованный текст
