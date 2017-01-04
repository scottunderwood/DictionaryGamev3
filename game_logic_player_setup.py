from random import *

def player_list_creator(players):
  player_count = input("How many players?")
  player_count_int_original = int(player_count)
  
  #populates players list
  player_count_int = player_count_int_original
  player_num = 0
  while player_count_int > 0:
    player_num = player_num + 1
    players.append("Player " + str(player_num))
    player_count_int = player_count_int - 1
  
  return players

def player_roles_list_creator(players, player_roles):
  player_role_count_int = len(players)
  initial_host = randint(0,(player_role_count_int - 1))
  player_role_assignment_num = -1
  
  while player_role_count_int > 0:
    player_role_assignment_num = player_role_assignment_num + 1
    if player_role_assignment_num == initial_host:
      player_roles.append("round_host")
    else:
      player_roles.append("round_participant")
    player_role_count_int = player_role_count_int - 1
    
  return player_roles