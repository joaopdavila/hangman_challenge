import os


def main():

    os.system("cls")

    raw_word = input("\n\nGAME MASTER - Insira a palavra a ser adivinhada:\nR: ")
    os.system("cls")
    word = raw_word.upper()
    guess = []
    correct_guess = []
    wrong_guess = []
    lives = len(word) + 1

    """
    game_status = 0 # Jogo não iniciado
    game_status = 1 # Jogo em andamento
    game_status = 2 # Vitória
    game_status = 3 # Derrota
    """
    game_status = 1  # Jogo em andamento
    for character in word:
        guess.append("_")
        if character not in correct_guess:
            correct_guess.append(character)

    print(
        "Hora de começar o jogo!\nVocê tem 10 vidas! Use-as com sabedoria"
        + "\n\nA palavra tem %s letras" % len(word)
    )

    print("\n%s" % (" ".join(guess)))

    while game_status == 1:
        raw_letter = input("\nJOGADOR - Insira a sua letra\n- ")
        os.system("cls")
        letter = raw_letter.upper()
        if letter in wrong_guess or letter in guess:
            print("Cuidado, você está repetindo letras! Sua vida será poupada")
        else:
            print("Letra escolhida foi: %s" % letter)
            if letter in correct_guess:
                for i in range(0, len(word)):
                    if word[i] == letter:
                        guess[i] = letter
            else:
                lives -= 1
                wrong_guess.append(letter)

        if lives > 0:
            print("Vidas restantes: %s\n" % lives)
            print("Letras erradas: %s\n" % (", ".join(sorted(wrong_guess))))
            print("\n%s" % (" ".join(guess)))

            if "_" not in guess:
                game_status = 2

        else:
            game_status = 3

    os.system("cls")

    if game_status == 2:
        print("PARABÉNS!!!\n\nVocê venceu!\nA palavra era %s" % word)
    elif game_status == 3:
        print("GAME OVER!!!\n\nSuas vidas acabaram!\nA palavra era %s" % word)

    print("\n\nPara jogar novamente, pressione F5")


main()
