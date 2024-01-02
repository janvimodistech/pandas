import matplotlib.pyplot as plt
time = [1, 2, 3, 4, 5]
team1_scores = [10, 15, 12, 18, 20]
team2_scores = [8, 12, 10, 14, 16]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.plot(time, team1_scores, marker='o', linestyle='-', color='b')
ax1.set_title('Team 1 Performance')
ax1.set_xlabel('Time')
ax1.set_ylabel('Scores')
ax2.plot(time, team2_scores, marker='s', linestyle='--', color='r')
ax2.set_title('Team 2 Performance')
ax2.set_xlabel('Time')
ax2.set_ylabel('Scores')
plt.tight_layout()
plt.show()
