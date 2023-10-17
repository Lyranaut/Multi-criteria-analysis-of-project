import csv
import numpy as np

n_projects = 10

project_indices = np.arange(n_projects)
project_costs = np.array(project_indices, dtype='float32')
project_costs[:] = 0.0
project_titles = []
i = 0
while i < n_projects:
    project_titles.append('')
    i = i + 1

with open('project_criteria.csv', newline='') as csvfile:
    criteria_data = list(csv.reader(csvfile, delimiter=','))
criteria_count = 0
for row in criteria_data:
    if criteria_count == 0:
        criteria_count = len(row) - 2
    project_index = int(row[0])
    project_titles[project_index] = row[1]
    project_costs[project_index] = float(row[2])
    criteria_values = [float(value) for value in row[3:]]
    # Add code to fill the criteria array based on criteria_values

for project_index in range(n_projects):
    print(f"Project: {project_titles[project_index]}, Cost: {project_costs[project_index]}")
    # Add code to print criteria for each project

with open('project_sets.csv', newline='') as csvfile:
    sets_data = list(csv.reader(csvfile, delimiter=','))
project_sets = np.zeros((len(sets_data), n_projects), dtype='int')
for i, row in enumerate(sets_data):
    for project_index, value in enumerate(row):
        if value.lower() == 'x':
            project_sets[i][project_index] = 1

for i in range(len(sets_data)):
    included_projects = [project_titles[j] for j in range(n_projects) if project_sets[i][j] == 1]
    print(f"Set {i + 1}: {', '.join(included_projects)}")

criteria_weights = [0.2, 0.3, 0.1, 0.4, 0.2, 0.15, 0.25, 0.35, 0.15, 0.1]
set_scores = np.dot(project_sets, criteria_weights)
best_set_index = np.argmax(set_scores)
best_set = project_sets[best_set_index]
included_projects = [project_titles[j] for j in range(n_projects) if best_set[j] == 1]
print(f"The best set of projects is: {', '.join(included_projects)}")
print(f"Score: {set_scores[best_set_index]}")