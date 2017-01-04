from random import *
from collections import deque


def round_pos_determination(player_list, player_role_list):
  r_host_num_start = 0
  for x in player_role_list:
    if x == "round_host":
      r_host_num = r_host_num_start
    else:
      r_host_num_start = r_host_num_start + 1
  return player_list[r_host_num]


def round_word_share(r_host):
  r_word = raw_input("%s please provide a word: " % (r_host))
  return r_word


def round_answer_sub(player_list):
  r_answer_list = []
  for x in player_list:
    p_answer = raw_input("%s please provide your answer: " % (x))
    p_answer_dict = {'user': x, 'answer': p_answer}
    r_answer_list.append(p_answer_dict)
  return r_answer_list


def round_answer_return(r_answer_list):
  n = 1
  for x in r_answer_list:
    print "%s) %s" % (n, x['answer'])
    n = n + 1

    
def round_vote(player_list, r_answer_list, r_votes, ??):
  r_votes = []
  for x in player_list:
    #need to validate for 1 - x based on length of answers
    p_r_vote = raw_input('%s vote: ' % (x))
    r_votes.append({'user': x, p_r_vote})
  for x in r_votes:
    if #vote == host response:
      #voter + 1
    elif #vote == non-host:
      #non-host + 2
    elif #host votes == 0:
      #host score +3
      
    