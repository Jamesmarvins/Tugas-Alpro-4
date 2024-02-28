def cek_digit_belakang(x, y, z):
    digit_x = x % 10
    digit_y = y % 10
    digit_z = z % 10

    if digit_x == digit_y or digit_x == digit_z or digit_y == digit_z:
        return True
    return False

input_x = int(input("Masukkan bilangan pertama: "))
input_y = int(input("Masukkan bilangan kedua: "))
input_z = int(input("Masukkan bilangan ketiga: "))

hasil = cek_digit_belakang(input_x, input_y, input_z)

print("Output yang diharapkan =", hasil)
