from random import randint
def game1(): 
    """
    Hàm chơi đoán số. Nhập số từ bàn phím để đoán số bí mật
    """
    secret_num = 9
    guess = int(input("Nhập số ngẫu nhiên: "))
    if(guess == secret_num): print("Chính xác!")
    else: print("Sai!")

def game2():
    secret_num = randint(0,100)
    while(1):
        guess = int(input("Nhập số ngẫu nhiên: "))
        if(guess == secret_num): 
            print("Chính xác!")
            break
        else: print("Sai!")
            
def game3():
    secret_num = randint(0,100)
    while(1):
        guess = int(input("Nhập số ngẫu nhiên: "))
        if(guess == secret_num):
            print("Chính xác!")
            break
        elif(guess > secret_num):
            print("Số bạn chọn lớn hơn số bí mật! Vui lòng nhập lại!")
        else:
            print("Số bạn chọn nhỏ hơn số bí mật! Vui lòng nhập lại!")
  