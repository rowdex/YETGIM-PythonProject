from typing import Dict, List, Optional
import random

def login():
    username = input("Kullanıcı adınızı girin: ")
    password = input("Şifrenizi girin: ") 
    if username == "admin" and password == "1234": 
        print("Giriş başarılı!")
        return True 
    else:
        print("Hatalı kullanıcı adı veya şifre!")
        return False


def display_menu(menu: Dict[str, Dict[str, List[Dict[str, object]]]]) -> None: 


    print("\n--- Ürün Kategorileri ---")
    for kategori, urunler_bilgisi in menu.items():
        print(f"\n{kategori}:")
        urunler = urunler_bilgisi["Ürünler"]
        for i, urun in enumerate(urunler):
            print(f"{i+1}. {urun['isim']} (Fiyat: {urun['fiyat']} TL)")

def find_product_by_name(menu: Dict[str, Dict[str, List[Dict[str, object]]]], product_name: str) -> Optional[Dict[str, object]]:
 
    for category, category_data in menu.items():
        for product in category_data["Ürünler"]:
            if product["isim"].lower() == product_name.lower():
                return product
    return None

def add_to_cart(cart: List[Dict[str, object]], menu: Dict[str, Dict[str, List[Dict[str, object]]]]) -> None:



    while True:
        product_name = input("Eklemek istediğiniz ürünün adını girin (Çıkmak için 'q'): ")
        if product_name.lower() == 'q':
            break
        
        selected_product = find_product_by_name(menu, product_name)

        if selected_product:
            cart.append(selected_product)
            print(f"{selected_product['isim']} sepete eklendi.")
        else:
            print("Ürün bulunamadı.")



def view_cart(cart: List[Dict[str, object]]) -> None:

    if not cart:
        print("Sepetiniz boş.")
    else:
        print("\n--- Sepetiniz ---")
        total = 0 
        

    for item in cart:
        print(f"- {item['isim']} (Fiyat: {item['fiyat']} TL)")
        total += item['fiyat']
    print(f"\nToplam: {total} TL")

def checkout(cart: List[Dict[str, object]]) -> None:
    if not cart:
        print("Sepetiniz boş, ödeme yapılamaz.")
        return
    
    while True:
        print("\n--- Ödeme Ekranı ---")
        payment_choice = input("Ödemeye devam etmek istiyor musunuz? (e/h): ")

        if payment_choice.lower() == 'e':
            credit_card_number = input("Kredi kartı numaranızı girin: ")
            cvv = input("CVV numaranızı girin: ")
            order_number = random.randint(100000, 999999)
            print(f"\nSiparişiniz oluşturuldu!")
            print(f"Sipariş numaranız: {order_number}")
            break 
        elif payment_choice.lower() == 'h':
            print("Ödeme ekranından çıkılıyor. Ana menüye dönülüyor.")
            return
        else:
            print("Geçersiz seçenek. Lütfen 'e' veya 'h' girin.")
    
    

def main():
    menu = {
        "Elektronik": {"Ürünler": [{"isim": "Telefon", "fiyat": 15000}, {"isim": "Tablet", "fiyat": 6000}, {"isim": "Bilgisayar", "fiyat": 25000}]},
        "Giyim": {"Ürünler": [{"isim": "Tişört", "fiyat": 250}, {"isim": "Pantolon", "fiyat": 500}, {"isim": "Ceket", "fiyat": 1200}]},
        "Ev Eşyası": {"Ürünler": [{"isim": "Masa", "fiyat": 1000}, {"isim": "Sandalye", "fiyat": 400}, {"isim": "Dolap", "fiyat": 2000}]},
        "Kitap": {"Ürünler": [{"isim": "Roman", "fiyat": 80}, {"isim": "Hikaye", "fiyat": 50}, {"isim": "Ders Kitabı", "fiyat": 200}]}
    }
    cart = []
    
    logged_in = login()
    if logged_in:
      display_menu(menu)
      add_to_cart(cart, menu)
      show_menu = True
      while show_menu:
        if len(cart) == 0:
          print("Sepetiniz boş.")
          add_to_cart(cart,menu)
        else:
          view_cart(cart)
          checkout_choice = input("Ödeme yapmak istiyor musunuz? (e/h): ")
          if checkout_choice.lower() == 'e':
              checkout(cart)
              show_menu = False
          else:
            add_to_cart(cart,menu)
        
        

if __name__ == "__main__":
    main()


