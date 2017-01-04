def score_set(player_list, score_dict_list):
	for x in player_list:
		score_dict = {'user': x, 'score': 0}
		score_dict_list.append(score_dict)
	return score_dict_list

#change score holder from dict of lists to list of dicts?
# http://stackoverflow.com/questions/4391697/find-the-index-of-a-dict-within-a-list-by-matching-the-dicts-value

#def Score_Update(score_d,round_scores):
#	for x in score_d:
#		player_tag_num = 0
#		player_tag = score_d[1][0]
#		player_tag_index
#		score_d[]


#def Score_Report