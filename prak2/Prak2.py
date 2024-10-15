#TUGAS 1
def evaluate_performance(percentage):
    # Jika nilai persentase >= 90, kembalikan "Excellent performance"
    if percentage >= 90:
        return "Excellent performance"
    # Jika nilai persentase >= 80 dan < 90, kembalikan "Very Good performance"
    elif percentage >= 80:
        return "Very Good performance"
    # Jika nilai persentase >= 70 dan < 80, kembalikan "Good performance"
    elif percentage >= 70:
        return "Good performance"
    # Jika nilai persentase >= 60 dan < 70, kembalikan "Average performance"
    elif percentage >= 60:
        return "Average performance"
    # Jika nilai persentase < 60, kembalikan "Needs Improvement"
    else:
        return "Needs Improvement"

# Pengguna diminta memasukkan persentase sebagai input
percentage = float(input("Enter the percentage: "))
# Fungsi evaluate_performance dipanggil untuk mengevaluasi kinerja siswa
result = evaluate_performance(percentage)
# Hasil evaluasi dicetak
print(result)


#TUGAS 2
def largest_of_three(a, b, c):
    # Fungsi max() digunakan untuk menemukan angka terbesar di antara a, b, dan c
    return max(a, b, c)

# Pengguna diminta memasukkan tiga angka untuk dibandingkan
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))
# Fungsi largest_of_three dipanggil untuk menemukan angka terbesar
print("The largest number is:", largest_of_three(a, b, c))


#TUGAS 3
n = int(input("Masukkan batas bilangan Fibonacci: "))

# Inisialisasi dua bilangan pertama dari deret Fibonacci
a, b = 0, 1
# Loop untuk mencetak deret Fibonacci sampai nilai a kurang dari atau sama dengan n
while a <= n:
    print(a, end=" ")  # Cetak nilai a
    a, b = b, a + b  # Update nilai a dan b dengan aturan Fibonacci (a menjadi b, dan b menjadi a+b)
print()


#TUGAS  4
def cetak_angka_ganjil(n):
    # Loop dari 1 hingga n
    for i in range(1, n + 1):
        if i % 2 != 0:  # Memeriksa apakah angka ganjil (sisa bagi dengan 2 harus 1)
            print(i, end=' ')  # Cetak angka ganjil
    print()

# Pengguna diminta memasukkan nilai n sebagai batas
n = int(input("Masukkan nilai n: "))
# Fungsi cetak_angka_ganjil dipanggil untuk mencetak angka ganjil hingga n
cetak_angka_ganjil(n)


#TUGAS 5
def print_pattern(n):
    # Loop untuk mencetak pola
    for i in range(1, n + 1):  # Loop melalui setiap baris
        for j in range(i):  # Loop untuk mencetak angka sesuai jumlah baris
            print(i, end=' ')  # Cetak angka i sebanyak i kali di baris tersebut
        print()  # Pindah ke baris berikutnya setelah satu baris selesai

# Pengguna diminta memasukkan nilai n sebagai batas untuk pola
n = int(input("Enter the value of n: "))
# Fungsi print_pattern dipanggil untuk mencetak pola
print_pattern(n)
