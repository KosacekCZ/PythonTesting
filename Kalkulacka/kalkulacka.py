class Kalkulacka:

    def secti(self, a, b):
        """
        Funkce pro sčítání dvou čísel.
        :param a: celé číslo, první člen sčítání
        :param b: celé číslo, druhý člen sčítání
        :return: vrací součet čísel a a b
        """

        return a + b

    def odecti(self, a, b):
        """
        Funkce pro odčítání dvou čísel.
        :param a: celé číslo, první člen odčítání
        :param b: celé číslo, druhý člen odčítání
        :return: vrací rozdíl čísel a a b
        """
        return a - b

    def vynasob(self, a, b):
        """
        Funkce pro násobení dvou čísel.
        :param a: celé číslo, první člen násobení
        :param b: celé číslo, druhý člen násobení
        :return: vrací součin čísel a a b
        """
        return a * b

    def vydel(self, a, b):
        """
        Metoda určená k dělení dvou čísel.
        :param a: číslo, dělenec
        :param b: číslo, dělitel
        :return: podíl čísel a,b.
        :raises vyhazuje výjímku v případě, že dělitel je nula.
        """
        if b == 0:
            raise Exception("Nelze dělit nulou")
        return a / b

    def modulo(self, a, b):
        return a % b