# sum / penjumlahan 

def main():
    bilangan = []
    jumlah_bilangan = int(input("Masukkan jumlah bilangan: "))

    for i in range(jumlah_bilangan):
        bilangan.append(float(input(f"Masukkan bilangan ke-{i+1}: ")))

    total = sum(bilangan)
    print(f"Hasil penjumlahan: {total}")


if __name__ == "__main__":
    main()


# palindrome

def is_padlimore(number):
    doubled_number = str(number) + str(number)
    
    number_set = set(str(number))
    doubled_number_set = set(doubled_number)
    
    return number_set == doubled_number_set

number1 = 1210
number2 = 1234

if is_padlimore(number1):
    print(number1, "adalah angka Padlimore")
else:
    print(number1, "bukan angka Padlimore")

if is_padlimore(number2):
    print(number2, "adalah angka Padlimore")
else:
    print(number2, "bukan angka Padlimore")


#bilangan prima 
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

num = int(input("Masukkan sebuah bilangan: "))
if is_prime(num):
    print(num, "adalah bilangan prima.")
else:
    print(num, "bukan bilangan prima.")


#tahun kabisat 
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

year = int(input("Masukkan tahun: "))
if is_leap_year(year):
    print(year, "adalah tahun kabisat.")
else:
    print(year, "bukan tahun kabisat.")


#merubah menjadi kecil semua 
input_str = input("Masukkan teks: ")

lower_str = input_str.lower()

print("Hasil: ", lower_str)


#menghitung jumlah huruf yang di inputkan user
def count_substring(s):
    if not s:
        return

    count = 1
    prev_char = s[0]

    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            print(f"{prev_char} = {count}")
            count = 1
            prev_char = char

    print(f"{prev_char} = {count}")

input_str = input("Masukkan string yang hanya terdiri dari huruf tidak kapital: ")
count_substring(input_str)

#jumlah luas daerah 
def calculate_area(coords):
    n = len(coords)
    area = 0

    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)

    return abs(area) / 2.0

def get_coordinates(num_coords):
    coords = []
    for i in range(num_coords):
        x = int(input(f"Masukkan koordinat X titik ke-{i + 1}: "))
        y = int(input(f"Masukkan koordinat Y titik ke-{i + 1}: "))
        coords.append((x, y))
    return coords

num_coordinates = int(input("Masukkan jumlah koordinat pojok denah rumah: "))

coordinates = get_coordinates(num_coordinates)

area = calculate_area(coordinates)
print("Luas denah rumah adalah:", area)
