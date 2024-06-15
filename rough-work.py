import random

def printboard (xstate ,ystate):
    data0 = 'X' if xstate[0] else ('O'if ystate[0] else 0)
    data1 = 'X' if xstate[1] else ('O'if ystate[1] else 1)
    data2 = 'X' if xstate[2] else ('O'if ystate[2] else 2)
    data3 = 'X' if xstate[3] else ('O'if ystate[3] else 3)
    data4 = 'X' if xstate[4] else ('O'if ystate[4] else 4)
    data5 = 'X' if xstate[5] else ('O'if ystate[5] else 5)
    data6 = 'X' if xstate[6] else ('O'if ystate[6] else 6)
    data7 = 'X' if xstate[7] else ('O'if ystate[7] else 7)
    data8 = 'X' if xstate[8] else ('O'if ystate[8] else 8)
    print(f' {data0}| {data1} | {data2}')
    print( '--|---|--') 
    print(f' {data3}| {data4} | {data5}')
    print( '--|---|--')
    print(f' {data6}| {data7} | {data8}')

# def get_user_input():
#     while True:
#         try:
#             value = int(input('Please enter a value: '))
#             if 0 <= value <= 8:
#                 return value
#             else:
#                 print('Invalid input. Please enter a number between 0 and 8.')
#         except ValueError:
#             print('Invalid input. Please enter a number.')
    
if __name__=='__main__':
    xstate = [0,0,0,0,0,0,0,0,0]
    ystate = [0,0,0,0,0,0,0,0,0]
    turn = 1 
    while True:
        print('welcome to tic tac toe')
        # print(get_user_input())
        print(printboard(xstate ,ystate))
        # if (0,1,2 == "X" ) and (0,3,4=="X") and (6,7,8=="X") and (0,4,5=="X") and (2,4,6=="X") and (0,3,6=="X")and (1,4,7=="X") and (2,5,8 == "X"):
        #     print('x winnes')
        if turn ==1:
            
                print('x chance ')
                value = int(input ('please enter a value '))
                xstate[value] = 1
                turn = 0
                xwines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
                for win in xwines:
                    if sum([xstate[win[0]], xstate[win[1]], xstate[win[2]]]) == 3:
                        print("X wins the match")
                        print("match is over")
                        break
                        
                    
        else:
            print('o chance ')
            value = int(input ('please enter a value '))
            ystate[value] = 1
            turn = 1
            ywines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            for win in ywines:
                if sum([ystate[win[0]], ystate[win[1]], ystate[win[2]]]) == 3:
                    print("o wins the match")
                    print("match is over")
                    break
                    
                
            
            print(printboard(xstate ,ystate))

        # elif (0,1,2 == "Z" ) and (0,3,4=="Z") and (6,7,8=="Z") and (0,4,5=="Z") and (2,4,6=="Z") and (0,3,6=="Z")and (1,4,7=="Z") and (2,5,8 == "Z"):
        #     print('o winnes')