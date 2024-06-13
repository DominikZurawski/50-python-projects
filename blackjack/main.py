############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def sum(list):
  """" Take a list and return sum"""
  sum = 0
  is_ace = False

  for x in list:
    if x == 11:
      is_ace = True

    sum += x
  if sum > 21 and is_ace:
    sum -= 10
    for x in range(len(list)):
      if list[x] == 11:
        list[x] = 1

  return sum


player = {"name": "Player", "cards": [], "sum": sum}
dealer = {"name": "Dealer", "cards": [], "sum": sum}


def score(gamer):
  gamer_sum_function = gamer["sum"]
  gamer["result"] = gamer_sum_function(gamer["cards"])
  return gamer["result"]


def print_cards_ans_score():
  print(f"Dealer first card is: {dealer['cards'][0]}")
  print(f"Score: {score(player)}, you're cards are: {player['cards']}")


def result():
  print(f"Score: {score(dealer)}, Dealer cards were: {dealer['cards']}, ")
  print(f"Score: {score(player)}, you're cards were: {player['cards']}, ")
  return


def check_result():
  """Check a result od game and return winer"""
  if score(player) == 21 or score(dealer) == 21:
    if score(player) == 21:
      print(f"{player['name']} win! \U0001F600")
    else:
      print(f"{dealer['name']} win! \U0001F612")
    result()
    return 'n'

  elif score(player) > 21 and score(dealer) > 21:
    print("A draw! \U0001F642")
    result()
  elif score(player) > 21 or score(dealer) > 21:
    if score(player) > 21:
      print(f"{dealer['name']} win! \U0001F612")
    elif score(dealer) > 21:
      print(f"{player['name']} win! \U0001F600")
    result()
    return 'n'
  return


def result_less_21_points():
  """Check a result od game and return winer when computer and player pass less than 21 points"""
  if score(player) > score(dealer):
    print(f"{player['name']} win! \U0001F600 ")

  elif score(player) < score(dealer):
    print(f"{dealer['name']} win! \U0001F612")

  elif score(player) == score(dealer):
    print("A draw! \U0001F642")
  result()
  return


def dealer_choice():
  """Its a computer logic game"""
  possibility = [0, 1]
  while random.choice(possibility) == 1 and score(dealer) <= 21:
    dealer["cards"].extend(random.sample(cards, 1))
  if random.choice(possibility) == 0:
    check_result()
  return


def game_logic():
  is_not_end = 'y'
  if score(player) == 21 or score(dealer) == 21:
    check_result()

  while is_not_end == 'y':
    is_not_end = check_result()
    if is_not_end != 'n':
      is_not_end = input(
          "Type 'y' to get another card, type 'n' to pass: ").lower()
    else:
      return

    if is_not_end == 'y':
      player["cards"].extend(random.sample(cards, 1))
      if score(dealer) < 17:
        dealer["cards"].extend(random.sample(cards, 1))
      elif score(player) >= 21 or score(dealer) >= 21:
        check_result()
        is_not_end = 'n'
        return
      print_cards_ans_score()

    elif is_not_end != 'y':
      while score(dealer) < 17:
        dealer["cards"].extend(random.sample(cards, 1))

      if score(dealer) < 21 and score(player) < 21:
        result_less_21_points()
        return
      elif score(dealer) < 21:
        dealer_choice()
        check_result()

      else:
        check_result()
        return


again = 'y'
while again == 'y':
  print(logo)
  dealer["cards"] = random.sample(cards, 2)
  player["cards"] = random.sample(cards, 2)
  print_cards_ans_score()

  game_logic()
  again = input("Do you want play again? Type: Y/N ").lower()
