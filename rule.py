def rule(*args):
    if args[0] == args[1]:
        print ('draw')
    else:
        if 'rock' in args:
            if 'scissor' in args:
                win = 'rock'
                print (win)
            elif 'paper' in args:
                win = 'paper'
                print (win)
        else:
                win = 'scissor'
                print (win)

rule('rock', 'scissor')
rule('rock', 'paper')
rule('rock', 'rock')
