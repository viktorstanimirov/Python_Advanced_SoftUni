def team_lineup(*args):
    result = {}

    for player, country in args:
        if country not in result:
            result[country] = []
        result[country].append(player)

    final_result = sorted(result.items(), key=lambda x: -len(x[1]))
    return "\n".join(final_result)



print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))


