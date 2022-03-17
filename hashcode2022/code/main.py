# filename = 'a_an_example'
filename = 'b_better_start_small'
# filename = 'c_collaboration'
# filename = 'd_dense_schedule'
# filename = 'e_exceptional_skills'
# filename = 'f_find_great_mentors'


import reader
from collections import defaultdict

skills_dict, projects = reader.read_file('input_data/' + filename + '.in.txt')
# projects.sort(key=lambda x: x['best_before'])

assigned_projects = []
wrong_loops = 0

inavailable_people = set()

# for each project -> find contributors with skills that match the project requirements and assign them to the project
while len(projects) > 0 and wrong_loops <= len(projects):
    print(len(projects))
    project = projects.pop(0)

    # find all contributors that match the project requirements / level_ups
    level_up_contributors = []
    matching_contributors = []
    max_levels = defaultdict(int)

    project_done = True

    for required_skill, required_level in project['skills']:
        best_contributor_dict = None
        for contributor_dict in skills_dict[required_skill]:
            if contributor_dict['contributor_name'] not in matching_contributors:
                if contributor_dict['level'] >= required_level:
                    if best_contributor_dict is None:
                        best_contributor_dict = contributor_dict
                    elif contributor_dict['level'] < best_contributor_dict['level']:
                        best_contributor_dict = contributor_dict
                if contributor_dict['level'] == required_level - 1 and max_levels[required_skill] >= required_level:
                    best_contributor_dict = contributor_dict

        if best_contributor_dict:
            best_contributor, skill_level = best_contributor_dict['contributor_name'], best_contributor_dict['level']
            if skill_level == required_level:
                level_up_contributors.append(best_contributor_dict)

            matching_contributors.append(best_contributor)
            max_levels[required_skill] = max(max_levels[required_skill], skill_level)
        else:
            project_done = False


    # if there are no contributors that match the project requirements -> skip the project
    if project_done:
        assigned_projects.append((project['project_name'], matching_contributors))
        for contributor_dict in level_up_contributors:
            contributor_dict['level'] += 1
        wrong_loops = 0
    else:
        projects.append(project)
        wrong_loops += 1


# write to output file
with open('output_data/' + filename + '.out.txt', 'w') as file:
    file.write(str(len(assigned_projects)) + '\n')
    for project in assigned_projects:
        file.write(project[0] + '\n' + ' '.join(project[1]) + '\n')
