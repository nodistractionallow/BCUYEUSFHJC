import re

with open('mainconnect.py', 'r') as f:
    content = f.read()

# Fix duplicated playerDismissed logic
content = re.sub(r'def playerDismissed\(player\):\n\s+nonlocal batter1, batter2, onStrike, batting_playing_order, fow_data\n\s+fow_data\.append\(.*?\)\n\s+nonlocal batter1, batter2, onStrike',
                 r'def playerDismissed(player):\n        nonlocal batter1, batter2, onStrike, batting_playing_order, fow_data\n        fow_data.append({"wicket": wickets + 1, "runs": runs, "player": player["player"]["playerInitials"], "over": f"{balls // 6}.{balls % 6}"})',
                 content, flags=re.DOTALL)

content = re.sub(r'def playerDismissed\(player\):\n\s+nonlocal batter1, batter2, onStrike, targetChased, batting_playing_order, fow_data\n\s+fow_data\.append\(.*?\)\n\s+nonlocal batter1, batter2, onStrike, targetChased',
                 r'def playerDismissed(player):\n        nonlocal batter1, batter2, onStrike, targetChased, batting_playing_order, fow_data\n        fow_data.append({"wicket": wickets + 1, "runs": runs, "player": player["player"]["playerInitials"], "over": f"{balls // 6}.{balls % 6}"})',
                 content, flags=re.DOTALL)

with open('mainconnect.py', 'w') as f:
    f.write(content)
