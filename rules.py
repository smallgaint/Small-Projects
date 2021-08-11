def rule(*args):
    if args[0] == args[1]:
        print ('draw')
    else:
        if 'rock' in args:
            if 'scissor' in args:
                win = 'rock'
                return (win)
            elif 'paper' in args:
                win = 'paper'
                return (win)
        else:
                win = 'scissor'
                return (win)

def rules(*args):
    a = args[0]
    b = args[1]
    c = args[2]
    if a == b and b == c:
        print ('draw')
    elif a != b and b != c and a != c:
        print ('draw')
    else:
        if b == c:
            win = rule(a,b)
            if a == win:
                print('a')
            elif b == win:
                print ('b','c')
        elif a == c:
            win = rule(a,b)
            if a == win:
                print('a', 'c')
            elif b == win:
                print ('b')
        elif a == b:
            win = rule(a,c)
            if a == win:
                print('a','b')
            elif c == win:
                print ('c')

rules('rock','paper','scissor')
rules('rock','rock','paper')
rules('rock','rock','rock')
rules('paper','rock','paper')
rules('paper','scissor','scissor')
