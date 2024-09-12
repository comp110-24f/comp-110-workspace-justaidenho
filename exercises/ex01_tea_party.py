"""This program will calculate how expensive a tea party will be"""

__author__: str = "730759640"


def main_planner(guests: int) -> None:
    """This will calculate the final cost using the number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Teabags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # This line needs to use nested function calls in order to find teabags and treats


def tea_bags(people: int) -> int:
    """This function calculates the number of teabags needed"""
    return people * 2


def treats(people: int) -> int:
    """This function calculates the number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This function will calculate the final cost"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
