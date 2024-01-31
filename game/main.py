import random


def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera?').lower()

  if not user_option in options:
    print('Opción inválida')
    ##continue
    return None, None

  computer_option = random.choice(options)
  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')

  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Ganaste!')
      user_wins += 1
    else:
      print('Perdiste!')
      computer_wins += 1

  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Ganaste!')
      user_wins += 1
    else:
      print('Perdiste!')
      computer_wins += 1

  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Ganaste!')
      user_wins += 1
    else:
      print('Perdiste!')
      computer_wins += 1

  return user_wins, computer_wins


def message_winner(user_wins, computer_wins, rounds):
  if computer_wins == 3:
    message_each_round(user_wins, computer_wins, rounds='END')
    print('Perdiste todo!')
    exit()

  if user_wins == 3:
    message_each_round(user_wins, computer_wins, rounds='END')
    print('Ganaste todo!')
    exit()


def message_each_round(user_wins, computer_wins, rounds):
  print('*' * 10)
  print('ROUND ', rounds)
  print('*' * 10)

  print('computer_wins ', computer_wins)
  print('user_wins ', user_wins)


def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1

  while True:
    message_each_round(user_wins, computer_wins, rounds)
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option,
                                           user_wins, computer_wins)
    message_winner(user_wins, computer_wins, rounds)
    rounds += 1


run_game()
