def minion_game(string):
    #----> practice 1 
    #vowels ="AEIOU"
    #player_1=[]
    #player_2=[]
    #for i in range(len(string)):
    #    if string[i] not in vowels :
    #        for j in range(i+1,len(string)+1):
    #            player_1.append(string[i:j])
    #    if string[i] in vowels :
    #         for j in range(i+1,len(string)+1):
    #            player_2.append(string[i:j]) 
    #score_1 = len(player_1)
    #score_2 = len(player_2)
    #if score_1>score_2:
    #    print(f"Stuart {score_1}")
    #elif score_1 == score_2:
    #    print("Draw")
    #else:
    #    print(f"Kevin {score_2}")
    
    #-----> practice 2
    vowels = "AEIOU"

    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
