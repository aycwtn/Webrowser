import webbrowser as w
ig = "https://instagram.com"
wp = "https://web.whatsapp.com"
gl = "https://google.com"
dst = "C:/Users/can/Desktop"
favlar = ["", ig,wp,gl,dst]

while 1:
    print("""
1 - İnstagram
2 - Whatsapp
3 - Google
4 - Masaüstü""")
    secim = int(input("CHATBOT> "))

    if secim < 1 or secim > 4:
        continue
    w.open(favlar[secim])
    
