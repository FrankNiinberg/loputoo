# main.py

import random
import csv

FILE = "rps_results.csv"


def get_name():
    name = input("Sisesta oma nimi: ").strip()

    while name == "":
        print("Nimi ei tohi olla tühi!")
        name = input("Sisesta oma nimi: ").strip()

    return name


def get_choice():
    while True:
        choice = input("Vali kivi, paber või käärid: ").lower().strip()

        if choice == "kivi" or choice == "paber" or choice == "käärid":
            return choice
        else:
            print("Vale valik! Proovi uuesti.")


def check_winner(player, computer):
    if player == computer:
        return "viik"

    elif player == "kivi" and computer == "käärid":
        return "mängija"

    elif player == "käärid" and computer == "paber":
        return "mängija"

    elif player == "paber" and computer == "kivi":
        return "mängija"

    else:
        return "arvuti"


def save_result(name, player_score, computer_score, winner):
    try:
        try:
            with open(FILE, "r", encoding="utf-8") as file:
                empty = file.read(1) == ""
        except FileNotFoundError:
            empty = True

        with open(FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if empty:
                writer.writerow(["nimi", "mängija", "arvuti", "võitja"])

            writer.writerow([name, player_score, computer_score, winner])

        print("Tulemus salvestati faili!")

    except OSError:
        print("Faili salvestamisel tekkis viga!")


def read_results():
    try:
        with open(FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            results = list(reader)

            if len(results) > 0:
                return results[1:]

            return []

    except FileNotFoundError:
        return []

    except (OSError, csv.Error):
        print("Faili lugemisel tekkis viga!")
        return []


def show_statistics():
    results = read_results()

    player_wins = 0
    computer_wins = 0

    for result in results:
        if len(result) == 4:
            if result[3] == "mängija":
                player_wins += 1

            elif result[3] == "arvuti":
                computer_wins += 1

    print("\n========== STATISTIKA ==========")
    print("Mänge kokku:", len(results))
    print("Mängija võite:", player_wins)
    print("Arvuti võite:", computer_wins)

    if len(results) > 0:
        last_game = results[-1]

        print("\nViimane lõpetatud mäng:")
        print("Mängija:", last_game[0])
        print("Mängija vooruvõidud:", last_game[1])
        print("Arvuti vooruvõidud:", last_game[2])
        print("Võitja:", last_game[3])

    else:
        print("Mänge pole veel mängitud.")


def play_game(name):
    player_score = 0
    computer_score = 0
    round_number = 0

    choices = ["kivi", "paber", "käärid"]

    print("\n========== UUS MÄNG ==========")
    print("Mängitakse 5 otsustavat vooru.")
    print("Viik ei lähe arvesse.")

    while player_score < 5 and computer_score < 5:

        print("\nVoor", round_number + 1)

        player = get_choice()
        computer = random.choice(choices)

        print("Sina:", player)
        print("Arvuti:", computer)

        round_winner = check_winner(player, computer)

        if round_winner == "viik":
            print("Viik! Mängime uuesti.")

        elif round_winner == "mängija":
            print("Vooru võitsid sina!")
            player_score += 1
            round_number += 1

        else:
            print("Vooru võitis arvuti!")
            computer_score += 1
            round_number += 1

        print("Seis: sina", player_score, "arvuti", computer_score)

    print("\n========== MÄNG LÄBI ==========")
    print("Sinu vooruvõidud:", player_score)
    print("Arvuti vooruvõidud:", computer_score)

    if player_score > computer_score:
        game_winner = "mängija"
        print("Palju õnne! Sina võitsid mängu!")

    else:
        game_winner = "arvuti"
        print("Arvuti võitis mängu!")

    save_result(name, player_score, computer_score, game_winner)


def main():
    print("==============================")
    print("      KIVI, PABER, KÄÄRID")
    print("==============================")

    name = get_name()

    while True:
        print("\n1 - Alusta uut mängu")
        print("2 - Vaata statistikat")
        print("3 - Välju mängust")

        choice = input("Vali tegevus: ").strip()

        if choice == "1":
            play_game(name)

        elif choice == "2":
            show_statistics()

        elif choice == "3":
            print("Aitäh mängimast!")
            break

        else:
            print("Vale valik! Vali 1, 2 või 3.")


if __name__ == "__main__":
    main()