"""
4* Реализовать кодирование и декодирование ключевых слов для латинского алфавита согласно указанному соответствию (маппингу).
Шифр (используйте данное соответствие букв при решении задания)
* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
Пример:
cipher = Cipher()
cipher.encode("Hello world")
"Btggj vjmgp"

cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"

"""
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
z = "CRYPTOABDEFGHIJKLMNQSUVWXZ"
layout = dict(zip(s, z))
symb = [",", " ", ":", "."]


class Cipher():
    """
    Класс кодируют и декодирует последовательность взависимости от указанного шифра
    """
    def encode(self, string):
        new_string = ""
        for i in string:
            for key, value in layout.items():
                if i == key:
                    new_string += value
                elif i == key.lower():
                    new_string += value.lower()
            if i in symb:
                new_string += i
        return print(new_string)

    def decode(self, string):
        new_string = ""
        for i in string:
            for key, value in layout.items():
                if i == value:
                    new_string += key
                elif i == value.lower():
                    new_string += key.lower()
            if i in symb:
                new_string += i
        return print(new_string)


cipher = Cipher()
cipher.encode("Hello world")
cipher.decode("Fjedhc dn atidsn")
