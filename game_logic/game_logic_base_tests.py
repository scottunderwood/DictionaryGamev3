from game_logic_player_setup import player_list_creator, player_roles_list_creator
from game_logic_score_tool import score_set
from game_logic_round import round_pos_determination, round_word_share, round_answer_sub, round_answer_return, round_vote, round_vote_score_translation

players_list = []
player_roles_list = []

player_list_creator(players_list)
player_roles_list_creator(players_list, player_roles_list)

score_dictionary_list =[]

score_set(players_list, score_dictionary_list)

round_host = ""
round_host = round_pos_determination(players_list, player_roles_list)

round_word = ""
round_word = round_word_share(round_host)

round_answers = []
round_answers = round_answer_sub(players_list)

round_answer_return(round_answers)

round_votes = []
round_vote(players_list,round_answers,round_votes, round_host)

round_scores = []
round_vote_score_translation(players_list,round_host,round_votes,round_scores)


# Tests

for p in players_list:
  print (p)
  
for p in player_roles_list:
  print (p)
  
for p in score_dictionary_list:
  print (p)

print ("the round host is: %s" % (round_host))
print ("the round word is: %s" % (round_word))

for p in round_votes:
  print (p)
  
for g in round_scores:
  print (g)