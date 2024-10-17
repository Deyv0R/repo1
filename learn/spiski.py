#numbers = [5, 2, 7]
#numbers.append(100)
#numbers.append(True)
#numbers.insert(1, 2.3)

#spiski = [4, 6, 8]
#numbers.extend(spiski)
#numbers.sort()

#numbers.reverse()
#numbers.pop(-1)
#numbers.remove(True)
#numbers.clear()

#print(numbers.count(2))
#print(len(numbers))


#nums = [5, 2, 7, "50", True]

#for el in nums:
#    el *= 2
#    print(el)


n = int(input("Enter length: "))
user_list = []

i = 0
while i < n:
    string = "Enter element # " + str(i + 1) + ": "
    user_list.append(input(string))
    i += 1

print(user_list)