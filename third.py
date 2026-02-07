import random
    
def start_game():

    random_num = random.randint(1, 10)
    is_correct = False

    while is_correct == False:

        guess_num = int(input("Hãy nhập một số từ 1 -> 10: "))

        if(guess_num < 1 or guess_num > 10):
            print('Chỉ có thể chọn số từ 1 -> 10')
        elif(guess_num < random_num):
            print('Nhỏ quá, hãy thử số lớn hơn')
        elif(guess_num > random_num):
            print('Lớn quá, hãy thử số nhỏ hơn')
        else:
            print('Chúc mừng! Bạn đoán rất chính xác')
            is_play_again = input('Bạn có muốn chơi lại không (C/K): ')

            if is_play_again == "C" or is_play_again == "c":
                is_correct = False
            elif is_play_again == "K" or is_play_again == "k":
                print('Vậy thì tạm biệt bạn nhé!')
                is_correct = True
            else:
                is_play_again = input('Bạn có muốn chơi lại không (C/K): ')

is_start_game = input('Bạn có muốn chơi trò choi đoán số không (C/K): ')

if(is_start_game == 'C' or is_start_game == 'c'):
    start_game()
elif(is_start_game == 'K' or is_start_game == 'k'):
    print("Vậy thì tạm biệt bạn nhé!")
else:
    is_start_game = input('Bạn có muốn chơi trò choi đoán số không (C/K): ')