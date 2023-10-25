#Открываем файлы для чтения и записи
f_read = open("file1_NN.txt", "r")
f_write = open("file2_NN.txt", "w")

even_product = 1
odd_product = 1
numbers = f_read.read().split()

#Проходим по каждому числу в файле
for number in numbers:
    number = int(number)

    #Проверяем, четное ли число
    if number % 2 == 0:
        even_product *= number
    else:
        odd_product *= number

#Записываем произведение четных чисел в файл
f_write.write(f"Произведение четных чисел: {even_product}\n")
#Записываем произведение нечетных чисел в файл
f_write.write(f"Произведение нечетных чисел: {odd_product}\n")

#Закрываем файлы
f_read.close()
f_write.close()