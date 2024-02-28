def cek_angka(x, y, z):
    if x != y and y != z and x != z: 
        if x + y == z or x + z == y or y + z == x:  
            return True
    return False

print(cek_angka(1, 2, 3)) 
print(cek_angka(1, 2, 4)) 
print(cek_angka(1, 2, 2)) 
print(cek_angka(1, 1, 2)) 