
# def AddNum(num1, num2):
#     total = num1 + num2
    
#     return total
    
# print(AddNum(3,5))

# def Mult2Nums(num1, num2):
#     total = 0
#     for i in range(num2):
#         total = AddNum(total, num1)
    
#     return total
    
# print(Mult2Nums(3,5))

# def Exp2Num(num1, num2):
    
#     result = 1
    
#     for i in range(num2):
#         result = Mult2Nums(result, num1)
        
#     return result

# print(Exp2Num(2,1000))


# address = input("Enter an address: ")
# print(address.isalnum())

# address= address.replace(" ", "")
# print(address.isalnum())

lst = ["blue", 'white', "red"]

colors = ", ".join(lst)

intro = "My favorite colors are: "

print(intro + colors)

