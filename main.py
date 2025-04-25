class Zikirmatik:
    def __init__(self):
        self.sayac = 0
        self.hedef = 33
    
    def artir(self):
        self.sayac += 1
        if self.sayac >= self.hedef:
            self.sayac = 0
            print(f"\n{self.hedef} kere tamamlandı! Tekrar başlıyoruz.\n")
        self.goster()
    
    def sifirla(self):
        self.sayac = 0
        print("Sayaç sıfırlandı!")
        self.goster()
    
    def goster(self):
        print(f"Şu anki sayım: {self.sayac}/{self.hedef}", end='\r')

def main():
    print("Python Zikirmatik Uygulaması")
    print("---------------------------")
    print("Artırmak için 'a' ya basın")
    print("Sıfırlamak için 's' ya basın")
    print("Çıkmak için 'q' ya basın\n")
    
    zikir = Zikirmatik()
    zikir.goster()
    
    while True:
        komut = input("\nKomut (a/s/q): ").lower()
        
        if komut == 'a':
            zikir.artir()
        elif komut == 's':
            zikir.sifirla()
        elif komut == 'q':
            print("Program sonlandırılıyor...")
            break
        else:
            print("Geçersiz komut! 'a', 's' veya 'q' girin.")

if __name__ == "__main__":
    main()