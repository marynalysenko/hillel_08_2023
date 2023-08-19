team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def show_players(players: list[dict]) -> None:
    """This function should print all players to the client."""
    # Top row of the table
    print("+--------+--------+-----+")
    print("| Number |  Name  | Age |")
    print("+--------+--------+-----+")

    # Display information for each player
    for player in sorted(players, key=lambda item: item["number"]):
        print(
            f"| {str(player['number']).center(6)} | "
            f"{player['name'].center(6)} | "
            f"{str(player['age']).center(3)} |"
        )
        print("+--------+--------+-----+")


def add_player(num: int, name: str, age: int) -> None:
    global team

    existing_player = next(
        (player for player in team if player["number"] == num), None
    )

    def assign_new_number():
        new_num = int(input("Enter a new number for the new player: "))
        add_player(new_num, name, age)

    def change_existing_number():
        existing_name = existing_player["name"]
        new_num = int(
            input(
                f"Enter a new number for the existing player {existing_name}: "
            )
        )

        while any(player["number"] == new_num for player in team):
            print(f"Number {new_num} is already taken by another player.")
            new_num = int(
                input(
                    f"Enter a different number for the existing player {existing_name}: "
                )
            )

        existing_player["number"] = new_num
        team.append({"name": name, "age": age, "number": num})
        print(
            f"Player {name} has been added with number {num}"
            f", {existing_player['name']} has been updated to number {new_num}."
        )

    def remove_existing():
        team.remove(existing_player)
        team.append({"name": name, "age": age, "number": num})
        print(
            f"Player {name} has been added with number {num}"
            f", {existing_player['name']} has been removed."
        )

    def ignore_adding():
        print(f"Adding player {name} has been ignored.")

    actions = {
        "1": assign_new_number,
        "2": change_existing_number,
        "3": remove_existing,
        "4": ignore_adding,
    }

    if existing_player:
        existing_name = existing_player["name"]
        print(f"Number {num} is already taken by the player {existing_name}.")

        choice = input(
            "Choose an action:\n"
            "1. Assign a new number to the new player\n"
            "2. Change the number of the existing player\n"
            "3. Remove the existing player\n"
            "4. Ignore adding the new player\n"
            "Enter your choice (1/2/3/4): "
        )

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. No action taken.")
    else:
        team.append({"name": name, "age": age, "number": num})
        print(f"Player {name} has been added to the team.")


def remove_player(players: list[dict], num: int) -> None:
    """This function removes the player by his/her number."""
    player_to_remove = next(
        (player for player in players if player["number"] == num), None
    )

    if player_to_remove:
        players.remove(player_to_remove)
        print(f"Player with number {num} has been removed from the team.")
    else:
        print(f"There is no player with number {num} in the team.")


def main():
    show_players(team)

    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Bob", age=39)
    remove_player(players=team, num=17)

    show_players(team)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
