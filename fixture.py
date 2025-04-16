def generate_round_robin(players):
    if len(players) % 2 != 0:
        players.append("BYE")  # Odd number of players, add a dummy

    n = len(players)
    rounds = n - 1
    half = n // 2

    schedule = []

    for round_num in range(rounds):
        round_matches = []
        for i in range(half):
            p1 = players[i]
            p2 = players[n - 1 - i]
            if p1 != "BYE" and p2 != "BYE":
                round_matches.append((p1, p2))
        schedule.append(round_matches)
        players = [players[0]] + [players[-1]] + players[1:-1]

    return schedule

# Example usage:
players = ["Ayehsa", "Sampurna", "Sristi", "Rohan", "Harsh Junior","Samar Ansari"]
fixture = generate_round_robin(players)

for i, round_matches in enumerate(fixture, 1):
    print(f"Round {i}:")
    for match in round_matches:
        print(f"  {match[0]} vs {match[1]}")
        
print(f"\nTotal matches to be played: {len(players) * (len(players) - 1) // 2}")
