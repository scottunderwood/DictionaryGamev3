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
    p_answer_dict = {'player': x, 'answer': p_answer}
    r_answer_list.append(p_answer_dict)
  return r_answer_list


def round_answer_return(r_answer_list):
  n = 1
  for x in r_answer_list:
    print "%s) %s" % (n, x['answer'])
    n = n + 1

    
def round_vote(player_list, r_answer_list, r_votes, r_host):
  for x in player_list:
    if x != r_host:
      p_r_vote = raw_input("%s please provide your vote: " % (x))
      #need to validate for 1 - x based on length of answers
      #need to make validation to ensure vote is a number
      p_r_vote_dict = {'player': x, 'vote': p_r_vote}
      r_votes.append(p_r_vote_dict)
  for z in r_votes:
    z_num = int(z['vote']) - 1
    z['vote_text'] = r_answer_list[z_num]['answer']
    z['vote_origin'] = r_answer_list[z_num]['player']
  return r_votes

#attempt at defining separate search function to use in the score vote tranlation function
def search_tool(dict_value, dict_key, dict_list):
    return [element for element in dict_list if element[dict_key] == dict_value]

#https://docs.google.com/spreadsheets/d/1H5v99y8FTe2-qGrfrQJH0kFtQ-IxeXbEjGYtN64Zt5U/edit#gid=0
#need to fix lingering count issues
def p_r_score_determination(r_vote_item, p_r_scores, p_r_host):
  non_responder_score_holder = search_tool(r_vote_item['vote_origin'], 'player', p_r_scores)[0]
  responder_score_holder = search_tool(r_vote_item['player'], 'player', p_r_scores)[0]
  #added filter for if people vote for their own answer
  if r_vote_item['vote_origin'] == r_vote_item['player']:
    responder_score_holder['p_r_score'] = responder_score_holder['p_r_score']
  elif r_vote_item['vote_origin'] == p_r_host:
    responder_score_holder['p_r_score'] = responder_score_holder['p_r_score'] + 1 
  elif r_vote_item['vote_origin'] != p_r_host:
    non_responder_score_holder['p_r_score'] = non_responder_score_holder['p_r_score'] + 2
  for k in p_r_scores:
    if k['player'] == non_responder_score_holder['player']:
      k['p_r_score'] = k['p_r_score'] + non_responder_score_holder['p_r_score']
    elif k['player'] == responder_score_holder['player']:
      k['p_r_score'] = k['p_r_score'] + responder_score_holder['p_r_score']
    else:
      k['p_r_score'] = k['p_r_score']
    return p_r_scores

def r_host_score_determination(r_vote, rnd_scores, rnd_host):
  r_host_vote_count = 0
  for z in r_vote:
    if z['vote_origin'] == rnd_host:
      r_host_vote_count = r_host_vote_count + 1
    else:
      r_host_vote_count = r_host_vote_count
  r_host_score_holder = search_tool(rnd_host, 'player', rnd_scores)[0]
  if r_host_vote_count == 0:
    r_host_score_holder['p_r_score'] = 3
  for m in rnd_scores:
    if m['player'] == rnd_host:
      #changed from m['p_r_score'] = m['p_r_score'] + r_host_score_holder['p_r_score'] and appears to have solved the problem?
      m['p_r_score'] = r_host_score_holder['p_r_score']
    else:
      m['p_r_score'] = m['p_r_score']
  return rnd_scores
  
def round_vote_score_translation(player_list, r_host, r_votes, r_scores):
  for y in player_list:
    r_scores.append({'player': y, 'p_r_score': 0})
  for x in r_votes:
    p_r_score_determination(x, r_scores, r_host)  
  r_host_score_determination(r_votes, r_scores, r_host)
  return (r_scores)