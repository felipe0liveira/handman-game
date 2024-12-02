import random
from utils.delay import wait
from utils.terminal import clear, show, request
from utils.strings import normalize

from data.words import words_list

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


def get_random_word():
    selected_list = random.randint(0, len(words_list) - 1)
    selected_word = random.choice(words_list[selected_list]["list"])
    placeholder = ["_" for _ in range(len(selected_word))]
    selected_word_length = len(selected_word)

    word = normalize(selected_word)
    tip = words_list[selected_list]["tip"]

    return placeholder, selected_word_length, selected_word, word, tip


def main():
    clear()
    show(":fox: Bem vindo ao famosíssimo jogo da forca!")
    wait(1000)

    show(f":fox: Bora começar!")
    wait(2500)

    clear()

    placeholder, selected_word_length, selected_word, word, tip = get_random_word()

    show(
        f':light_bulb: A sua palavra tem {selected_word_length} letra{"s" if selected_word_length > 1 else ""}!'
    )

    wait(1500)

    errors = 0
    wrong_letters = []
    has_extra_chance = False
    has_used_extra_chance = False
    user_input = ""

    while is_running:
        clear()
        show(f":right_arrow: {' '.join(placeholder)}\n")

        draw_hangman(errors, (selected_word_length * 2) + 2)

        user_lost = errors >= len(hangman) and not has_extra_chance
        if user_lost:
            show(f"\n:skull: Você perdeu! A palavra era {selected_word}!\n")
            break

        user_was_blessed = (
            errors == len(hangman) and has_extra_chance and not has_used_extra_chance
        )
        if user_was_blessed:
            has_used_extra_chance = True
            has_extra_chance = False
            show("   Você perdeu!")
            wait(1000)
            show("   Mas eu resolvi te dar a uma saideirinha, rsrs!")
            wait(1500)

        user_won = "_" not in placeholder
        if user_won:
            show_won(selected_word)
            break

        user_last_chance = errors == len(hangman) - 1
        if user_last_chance:
            show(
                f"\n:backhand_index_pointing_right: Parece que você só tem mais uma chance, aqui vai uma dica!"
            )
            show(f":light_bulb: Essa palavra {tip}!")

        should_show_tries = len(wrong_letters) > 0
        if should_show_tries:
            show(f":light_bulb: Você já tentou: {' - '.join(wrong_letters)}\n")

        user_input = request(
            "\n:backhand_index_pointing_right: Digite a letra ou o palpite sobre a palavra: "
        ).upper()

        user_guessed_word = normalize(user_input) == word
        if user_guessed_word:
            show_won(selected_word)
            break

        user_guessed_wrong = len(user_input) > 1
        if user_guessed_wrong:
            clear()
            show(
                ":prohibited: uhmm, eu até aceito chutes assim, mas como você errou só perdeu um ponto!\n"
            )
            errors += 1
            wait(5000)
            continue

        if user_input in word:
            for i in range(len(word)):
                if word[i] == user_input:
                    placeholder[i] = user_input

            if placeholder.count("_") <= len(word) * 0.2 and not has_extra_chance:
                has_extra_chance = True
            continue

        if user_input in wrong_letters:
            continue

        wrong_letters.append(user_input)
        errors += 1


if __name__ == "__main__":
    main()
