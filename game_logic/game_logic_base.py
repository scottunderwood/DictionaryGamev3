from game_logic_player_setup import player_list_creator, player_roles_list_creator
from game_logic_score_tool import score_set, score_update, score_report
from game_logic_round import round_pos_determination, round_word_share, round_answer_sub, round_answer_return, round_vote, round_vote_score_translation, round_advancement

def dict_game():
  players_list = []
  player_roles_list = []

  player_list_creator(players_list)
  player_roles_list_creator(players_list, player_roles_list)

  score_dictionary_list =[]

  score_set(players_list, score_dictionary_list)

  current_round_count = 1
  #testing full game loop with assumption that round limit is 2x the player count, ultimately want this managed as a user setting
  #round_limit = (len(players_list) * 2) + 1
  round_limit = 4

  #start of round loop
  while current_round_count < round_limit:
    round_host = ""
    round_host = round_pos_determination(players_list, player_roles_list)

    round_word = ""
    round_word = round_word_share(round_host)

    round_answers = []
    round_answers = round_answer_sub(players_list)

    # shelving round answer shuffle function for now
    #round_answer_shuffle(round_answers)
  
    round_answer_return(round_answers)

    round_votes = []
    round_vote(players_list,round_answers,round_votes, round_host)

    round_scores = []
    round_vote_score_translation(players_list,round_host,round_votes,round_scores)

    score_update(score_dictionary_list, round_scores)
  
    round_advancement(player_roles_list)
  
    current_round_count = current_round_count + 1

  #end of round loop
  
  score_report(score_dictionary_list)
  
dict_game()