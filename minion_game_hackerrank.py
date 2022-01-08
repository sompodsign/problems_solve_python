def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score = len(string) - i
            kevin += kevin_score
        else:
            stuart_score = len(string) - i
            stuart += stuart_score
    if kevin > stuart:
        print('Kevin', kevin)
    elif kevin < stuart:
        print('Stuart', stuart)
    else:
        print('Draw')


if __name__ == '__main__':
    minion_game("BANANA")
    minion_game("BAANANAS")
    minion_game("BAANANAS")
    minion_game("BAANANAS")