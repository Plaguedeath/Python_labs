def check_polindrom(polindrom):
    clean_text = (polindrom.lower()).split()

    reverse_text = clean_text[::-1]
    return clean_text == reverse_text


name = input("Введите ваше слово:")
if check_polindrom(name):
    print("Text is Polindrom")


