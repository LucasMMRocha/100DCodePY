file_1 = open("file1.txt", "r")
file_2 = open("file2.txt", "r")

list_1 = [int(n) for n in file_1]
list_2 = [int(n) for n in file_2]

result = [n for n in list_1 if n in list_2]

print(result)
