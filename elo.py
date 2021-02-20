player_elos = [1825, 1652]
game_result = [0, 1]
k = 32

def adjustElo(player_elos, game_result, k):
	expected_p1_odds = 1 / (1 +(10**((player_elos[1] - player_elos[0])/400)))
	expected_p2_odds = 1 / (1 +(10**((player_elos[0] - player_elos[1])/400)))
	player_elos[0] = player_elos[0] + k*(game_result[0] - expected_p1_odds)
	player_elos[1] = player_elos[1] + k*(game_result[1] - expected_p1_odds)
	return player_elos

print(adjustElo(player_elos, game_result, k))

