
def check_sum(a,b,c):
    print(a+b+c)
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

def check(xstate, ystate):
    xwines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in xwines:
        if sum([xstate[win[0]], xstate[win[1]], xstate[win[2]]]) == 3:
            print("X wins the match")
            return 1
        if sum([ystate[win[0]], ystate[win[1]], ystate[win[2]]]) == 3:
            print('O wins the match')
            return 0
    return -1

    
    
if __name__=='__main__':
    xstate = [0,0,0,0,0,0,0,0,0]
    ystate = [0,0,0,0,0,0,0,0,0]
    turn = 1 
    while True:
        print('welcome to tic tac toe')
        print(printboard(xstate ,ystate))
        if turn ==1:
            print('x chance ')
            value = int(input ('please enter a value '))
            xstate[value] = 1
            turn = 0
        else:
             print('o chance ')
             value = int(input ('please enter a value '))
             ystate[value] = 1
             result =check(xstate ,ystate)
             if result != -1:
                print('match over')
                break
             turn = 1
             
        print(printboard(xstate ,ystate))
        
