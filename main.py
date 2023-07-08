class Kalkulacka:

    def secti(self, a, b):
        """
        Metoda sečti se využívá ke sčítání dvou celých čísel.
        :param a: celé číslo, první člen ke sčítání
        :param b: celé číslo, druhý člen ke sčítání
        :return: návratová hodnota reprezentuje součet parametrů a a b
        """
        return a + b

    def odecti(self, a, b):
        return a - b

    def vynasob(self, a, b):
        return a * b

    def vydel(self, a, b):
        """
        Metoda pro dělení celých čísel.
        :param a: celé číslo, dělenec
        :param b: celé číslo, dělitel, nesmí být nulový
        :return: podíl čísel a a b
        :raises: Pokud je parametr B 0, tak vyhazuje výjmu proti dělení nulou.
        """
        if b == 0:
            raise Exception("Nelze dělit nulou")
        return a / b
