#https://repl.it/languages/python3
from random import *
from collections import deque


players = []
player_count = input("How many players?")
player_count_int_original = int(player_count)

#populates players list
player_count_int = player_count_int_original
player_num = 0

while player_count_int > 0:
  player_num = player_num + 1
  players.append("Player " + str(player_num))
  player_count_int = player_count_int - 1

for p in players:
  print (p)

#creates list of roles for each player in the players ist    
player_roles = []
player_role_count_int = player_count_int_original
initial_host = randint(0,(player_role_count_int - 1))
player_role_assignment_num = -1

while player_role_count_int > 0:
  player_role_assignment_num = player_role_assignment_num + 1
  if player_role_assignment_num == initial_host:
    player_roles.append("round_host")
  else:
    player_roles.append("round_participant")
  player_role_count_int = player_role_count_int - 1

for p in player_roles:
  print (p)

#attempt at round advancement function    

current_round_test = input("what is current round")
current_round_test_int = int(current_round_test)

round_count = player_count_int_original * 2

def round_advancement(role_list, current_round):
    role_list_rotator = deque(role_list)
    role_list_rotator.rotate(current_round)
    for ro in role_list_rotator:
        print (ro)
    return role_list_rotator  

# temorarily closing out the next two lines
round_advancement(player_roles, current_round_test_int)    
#role_list = role_list_rotator

#end attempt at round advancement function

def game_round(player_list, role_list):
  host_input = input("What is the word?")

player_dict = {}
player_dict['players'] = players
player_dict['roles'] = player_roles

#test at user input round
#update this so that each entry has a numeric key and then contains a list with the 
n = 1
round_resp = {}
for pl in players:
  round_sub = "round_sub_p%s" % (str(n))
  round_sub_answer = raw_input("%s Response: " % (round_sub))
  # make random list of submission indexes as long as the player count to randomize order of responses 
  round_sub_answer_list = [round_sub, round_sub_answer]
  round_resp[n] = round_sub_answer_list
  n = n+1

for a, b in round_resp.iteritems():
  print a, b

rand_round_resp_list = []
for x in round_resp.values():
  rand_round_resp_item = x[1]
  rand_round_resp_list.append(rand_round_resp_item)

print rand_round_resp_list

# This creates a function called "randomList" that takes a list as a parameter. It creates a temporary list to hold the randomized items. While the list passed to the function still has items in it, the for statement randomly selects one, removes it from that list, then appends it to the end of the temporary list. When all of the items in the original list have been moved, the function returns the randomized list.
def randomList(a): 
  b = [] 
  for i in range(len(a)): 
    len_var = len(a)
    element_num = round(randint(0,len_var)
    element = a[element_num]                 
    a.remove(element) 
    b.append(element)
    element_num = element_num - 1                    
    return b 

randomList(rand_round_resp_list) 

for item in rand_round_resp_list:
  print item
    
# need to create a starting score dictionary with value of zero for each player

# next is adding vote function that adds points to the user associated with each 
# option and then adds it to a running total for each user

# need to loop through the round / scoring x number of times and then announce a winner
  
#rand_round_resp = round_resp.values()
#ran_round_resp = list(rand_round_resp)
#random.shuffle(rand_round_resp)
#for val in rand_round_resp:
  #print val

# extended game logic framework
#def game_round(role_list, word_prompt, etc...): 
#def game(role_list, rotator, game_round, scoring, etc...):
  #game_round

#https://stackoverflow.com/questions/1349332/python-passing-a-function-into-another-function