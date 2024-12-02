import random
from utils import clear, normalize, show, wait, request
from words import words_list
import unicodedata

is_running = True

hangman = [
    "O",
    "|",
    "/|\\",
    "|",
    "/ \\",
]


def draw_hangman(errors, center_size):
    if errors == 0:
        return
    parts = len(hangman) if errors > len(hangman) else errors
    print("\n")
    for i in range(parts):
        show(hangman[i].center(center_size))
    print("\n")

def show_won(word):
    clear()
    show(f"\n:confetti_ball: Parabéns! Você acertou a palavra {word}!\n")


def main():
    while is_running:
        clear()
        show(":fox: Bem vindo ao famosíssimo jogo da forca!")
        wait(1000)

        show(f":fox: Bora começar!")
        wait(2500)
        break

    clear()
    selected_list = random.randint(0, len(words_list) - 1)
    selected_word = random.choice(words_list[selected_list]["list"])
    placeholder = ["_" for _ in range(len(selected_word))]
    selected_word_length = len(selected_word)

    word = normalize(selected_word)
    tip = words_list[selected_list]["tip"]

    show(
        f':light_bulb: A sua palavra {word} tem {selected_word_length} letra{"s" if selected_word_length > 1 else ""}!'
    )

    wait(1500)
    errors = 0
    wrong_letters = []
    has_extra_chance = False
    has_used_extra_chance = False

    while is_running:
        clear()
        show(f":right_arrow: {' '.join(placeholder)}\n")

        draw_hangman(errors, (selected_word_length * 2) + 2)

        if errors >= len(hangman) and not has_extra_chance:
            show(f"\n:skull: Você perdeu! A palavra era {word}!\n")
            break

        if errors == len(hangman) and has_extra_chance and not has_used_extra_chance:
            has_used_extra_chance = True
            has_extra_chance = False
            show("   Você perdeu!")
            wait(1000)
            show("   Mas eu resolvi te dar a uma saideirinha, rsrs!")
            wait(1500)

        if "_" not in placeholder:
            show_won(word)
            break

        if errors == len(hangman) - 1:
            show(
                f"\n:backhand_index_pointing_right: Parece que você só tem mais uma chance, aqui vai uma dica!"
            )
            show(f":light_bulb: Essa palavra {tip}!")

        if len(wrong_letters) > 0:
            show(f":light_bulb: Você já tentou: {' - '.join(wrong_letters)}\n")

        input_letter = request(
            "\n:backhand_index_pointing_right: Digite a letra ou o palpite sobre a palavra: "
        ).upper()


        if normalize(input_letter) == word:
            show_won(word)
            break

        if len(input_letter) > 1:
            clear()
            show(":prohibited: uhmm, eu até aceito chutes assim, mas como você errou só perdeu um ponto!\n")
            errors += 1
            wait(5000)
            continue

        if input_letter in word:
            for i in range(len(word)):
                if word[i] == input_letter:
                    placeholder[i] = input_letter

            if placeholder.count("_") <= len(word) * 0.2 and not has_extra_chance:
                has_extra_chance = True
            continue

        if input_letter in wrong_letters:
            continue

        wrong_letters.append(input_letter)
        errors += 1


if __name__ == "__main__":
    main()
