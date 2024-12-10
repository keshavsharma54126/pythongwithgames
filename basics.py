
for i in range(0,4,1):
        print(i)

fruits = ["banana","apple","orange"]
for fruit in fruits:
        print(fruit)

my_list =[]
numbers = [1,3,35,235]
mixed = [1,"hello",2.34,True]

print(my_list,numbers,mixed)

#list operations

#adding elemetns
my_list.append(5)
print(my_list)
my_list.insert(0,2)
print(my_list)
my_list.extend([3,5])
print(my_list)

#removing elemetns
my_list.pop()
print(my_list)
my_list.pop(0)
print(my_list)
my_list.remove(5)
print(my_list)
#

#accessing elements
first = my_list[0]
last = [-1]
slice = my_list[1:3]

#list methods
numbers = [3,23,3,23,234,55,234,4]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(len(numbers))
print(numbers.count(1))
print(numbers.index(4))

#list comphrehensions
#tradditional way
squares=[]
for i in range(5):
    squares.append(i**i)
print(squares)
#list comphrehension way
squaress =[x**x for x in range(5)]
print(squaress)