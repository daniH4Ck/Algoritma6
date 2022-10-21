print("                ,---.      .-._          .=-.-.       ")
print("  _,..---._   .--.'  \    /==/ \  .-._  /==/_ /       ")
print("/==/,   -  \  \==\-/\ \   |==|, \/ /, /|==|, |        ")
print("|==|   _   _\ /==/-|_\ |  |==|-  \|  | |==|  |        ")
print("|==|  .=.   | \==\,   - \ |==| ,  | -| |==|- |        ")
print("|==|,|   | -| /==/ -   ,| |==| -   _ | |==| ,|        ")
print("|==|  '='   //==/-  /\ - \|==|  /\ , | |==|- |        ")
print("|==|-,   _`/ \==\ _.\=\.-'/==/, | |- | /==/. /        ")
print("`-.`.____.'   `--`        `--`./  `--` `--`-`         \n")

print("---PROGRAM KONVERSI BILANGAN---")
print("1 -> Desimal ke biner")
print("2 -> Biner ke Desimal")
print("3 -> Exit")
a = 0
while a != 3:
    a = int(input("Silahkan masukan menu: "))
    if a == 1:
        b = int(input("Masukan bilangan desimal: "))
        bineri = bin(b).replace("0b","")
        print("Nilai binernya adalah {0}".format(bineri))
    elif a == 2:
        b = int(input("Masukan bilangan biner: "),2)
        print("Nilai desimalnya adalah {0}".format(b))
print("Terimakasih telah menggunakan program ini!")
