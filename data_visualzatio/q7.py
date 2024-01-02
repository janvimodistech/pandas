import matplotlib.pyplot as plt
exam_scores = [85, 90, 88, 72, 93, 78, 85, 60, 91, 70, 80, 82, 75, 88, 91, 68, 98, 84, 78, 80]
plt.hist(exam_scores, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Exam Scores')
plt.ylabel('Frequency')
plt.title('Distribution of Exam Scores')
plt.show()
