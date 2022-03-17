# 3 3
# Anna 1
# C++ 2
# Bob 2
# HTML 5
# CSS 5
# Maria 1
# Python 3
# Logging 5 10 5 1
# C++ 3
# WebServer 7 10 7 2
# HTML 3
# C++ 2
# WebChat 10 20 20 2
# Python 3
# HTML 3


# Contributors dict -> {'contributor_name': {'skills': level}}





# Projects list -> [{'project_name': project_name, 'days': days, 'score': score, 'best_before': bes_before, [{'skill': skil, level}]}]

# Skills dict -> {skill: [{'contributor_name': contributor_name, 'level': level, 'available': false}}
# false -> not available
# true -> available
from collections import defaultdict

# read txt file
def read_file(file_name):
    with open(file_name, 'r') as file:
        # read the first line
        contributors_num, projects_num = file.readline().split()

        skills_dict = defaultdict(list)

        # read contrubutors_nums lines
        for _ in range(int(contributors_num)):
            contributor, skills_num = file.readline().split()
            for _ in range(int(skills_num)):
                skill_name, skill_level = file.readline().split()
                skills_dict[skill_name].append({'contributor_name': contributor, 'level': int(skill_level)})

        # print(skills_dict)
        # print('------')


        projects = []
        for _ in range(int(projects_num)):
            project, days_to_complete, score, best_before, num_of_roles = file.readline().split()

            skills = []
            for _ in range(int(num_of_roles)):
                skill_name, skill_level = file.readline().split()
                skills.append((skill_name, int(skill_level)))
            projects.append({'project_name': project, 'days': int(days_to_complete), 'score': int(score), 'best_before': int(best_before), 'skills': skills})

        # print(projects)

        return skills_dict, projects

