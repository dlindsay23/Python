# Devin Lindsay


box1 = 6
box2 = 9
box3 = 20

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


MaxNumber = compute_lcm(box1,box2) + compute_lcm(box1,box3) - box1 - box2 - box3

print(MaxNumber)

# while Guess != box1:

#     num += 1
#     print("Num:",num)


#     # for i in range(1,box3):
#     #     for j in range(1,box2):
#     #         for k in range(1,box1):
#     #                 MaxNumber = (i*box1 + j*box2 + k*box3)
                    

#     if box1 % num == 0 or box2 % num == 0 or box3 % num == 0 :
#         Guess += 1
#         MaxNumber = num
#         input()
#     else:
#         Guess = 0

# print(MaxNumber)



