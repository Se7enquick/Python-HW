class Temperatures:
    def fah2cel(self, fah): # Перевод из Фарингейта в Цельсии
        self.cel = 5.0*(fah - 32) / 9
        return cel
    
    def cel2fah(self, cel): # Перевод из Цельсия в Фарингейты
        self.fah = (9 / 5.0 * cel) + 32
        return fah
