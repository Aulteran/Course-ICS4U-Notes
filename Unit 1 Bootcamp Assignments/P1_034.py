# msg = '''1) Square
# 2) Triangle

# Enter a number: '''

# def sq():
#     side_len = input("enter a side length: ")
#     print(f"area is {side_len**2}")

# def tr():
#     tri_base = input("enter the base length of the triangle: ")
#     tri_height = input("enter the height of the triangle: ")
#     print(f"area is {((tri_base*tri_height)/2)}")

# while True:
#     msg_response = input(msg)
#     if msg_response == 1:
#         sq()
#     elif msg_response == 2:
#         tr()
#     else:
#         print('Invalid response, error, restart')
#         continue
#     break

# print("bye bye :)")

lent = int(input("enter length: "))
widt = int(input("enter width: "))

def area(len:int, wid:int):
    a = len*wid
    return a

def volume(A):
    return A*int(input("enter depth: "))

print(volume(area(lent,widt)))
