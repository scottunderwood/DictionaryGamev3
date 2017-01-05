from game_logic_round import search_tool

def score_set(player_list, score_dict_list):
	for x in player_list:
		score_dict = {'player': x, 'score': 0}
		score_dict_list.append(score_dict)
	return score_dict_list


def score_update(score_d,r_scores):
	for x in score_d:
		p_holder = search_tool(x['player'], 'player', r_scores)[0]
		x['score'] = x['score'] + p_holder['p_r_score']
	return score_d
		
def score_report(score_d):
	for x in score_d:
		print "%s Current Score: %s" % (x['player'], x['score'])