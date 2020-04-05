import glob
import csv
import pandas as pd
import os
import random

file_dir = "/Users/gianluca/Desktop/fabias_data_two/"
files = glob.glob(file_dir + '*.csv')

for elem in files:

    file_object = open(elem, 'r')

    # reader = csv.reader(codecs.open(elem, 'rU', 'utf-8'))
    reader_2 = csv.reader(x.replace('\0', '') for x in file_object)

    rows = [row for row in reader_2 if row]
    rows = rows[1:]

    for i in rows:
        if len(i) == 1:
            rows.remove(i)

    stripped_rows = rows[1:]
    # get list of user ID's to iterate through
    temp_list = []
    for i in stripped_rows:
        temp_array = []
        if i[0] not in temp_list:
            temp_array.append(i[0])
        if i[1] not in temp_list:
            temp_array.append(i[1])
        temp_list.append(temp_array)

    # make the id list unique
    id_list = []
    for i in temp_list:
        if i not in id_list:
            id_list.append(i)

    # fill in empty external_ID
    missing_id = 'MISSING_'
    seed = random.seed(1)

    for i in id_list:
        rand = str(random.randint(1000, 999999))
        new_external_id = missing_id + rand
        if not i[1] or i[1] == '0':
            i[1] = new_external_id


    df = pd.DataFrame(data={'user_id': [],
                            'external_id': [],
                            'session_id_1': [],
                            'questionnaire_date_1': [],
                            'well_being_1': [],
                            'problem_severity_1': [],
                            'functioning_1': [],
                            'risk_1': [],
                            'total_minus_1': [],
                            'total_1': [],
                            'session_id_2': [],
                            'questionnaire_date_2': [],
                            'well_being_2': [],
                            'problem_severity_2': [],
                            'functioning_2': [],
                            'risk_2': [],
                            'total_minus_2': [],
                            'total_2': [],
                            'session_id_3': [],
                            'questionnaire_date_3': [],
                            'well_being_3': [],
                            'problem_severity_3': [],
                            'functioning_3': [],
                            'risk_3': [],
                            'total_minus_3': [],
                            'total_3': []
                            })

    # get data into individual lists
    for i in id_list:
        session_id, questionnaire_date, well_being, problem_severity, functioning, risk, total_minus, total = [],\
                                                                                                  [], [], [], [], [],\
                                                                                                              [], []
        other = []

        group_1, group_2, group_3, all_groups = [], [], [], []



        print('1')

        for j in stripped_rows:
            if j[0] == i[0]:
                session_id.append(j[2])
                questionnaire_date.append(j[3])
                well_being.append(j[4])
                problem_severity.append(j[5])
                functioning.append(j[6])
                risk.append(j[7])
                total_minus.append(j[8])
                total.append(j[9])

            print('2')

        for j in session_id:
            if j == '-1':
                session_id[session_id.index('-1')] = '8'

        # pad list
        for k in range(3):
            if len(session_id) != 3:
                session_id.append('')
            if len(questionnaire_date) != 3:
                questionnaire_date.append('')
            if len(well_being) != 3:
                well_being.append('')
            if len(problem_severity) != 3:
                problem_severity.append('')
            if len(functioning) != 3:
                functioning.append('')
            if len(risk) != 3:
                risk.append('')
            if len(total_minus) != 3:
                total_minus.append('')
            if len(total) != 3:
                total.append('')

        try:
            group_1.append(session_id[0])
            group_1.append(questionnaire_date[0])
            group_1.append(well_being[0])
            group_1.append(problem_severity[0])
            group_1.append(functioning[0])
            group_1.append(risk[0])
            group_1.append(total_minus[0])
            group_1.append(total[0])
            group_2.append(session_id[1])
            group_2.append(questionnaire_date[1])
            group_2.append(well_being[1])
            group_2.append(problem_severity[1])
            group_2.append(functioning[1])
            group_2.append(risk[1])
            group_2.append(total_minus[1])
            group_2.append(total[1])
            group_3.append(session_id[2])
            group_3.append(questionnaire_date[2])
            group_3.append(well_being[2])
            group_3.append(problem_severity[2])
            group_3.append(functioning[2])
            group_3.append(risk[2])
            group_3.append(total_minus[2])
            group_3.append(total[2])

        except IndexError:
            print('oops')

        all_groups.append(group_1)
        all_groups.append(group_2)
        all_groups.append(group_3)

        for x in range(3):
            for z in all_groups:
                if set(z) == {''}:
                    all_groups.remove(z)

        all_groups.sort()

        empty_list = ['', '', '', '', '', '', '', '']

        for z in range(3):
            if len(all_groups) < 3:
                all_groups.append(empty_list)

        group_1 = all_groups[0]
        group_2 = all_groups[1]
        group_3 = all_groups[2]


        print('1.5')

        user_id = i[0]
        external_id = i[1]
        df = df.append({'user_id': user_id,
                        'external_id': external_id,
                        'session_id_1': group_1[0],
                        'questionnaire_date_1': group_1[1],
                        'well_being_1': group_1[2],
                        'problem_severity_1': group_1[3],
                        'functioning_1': group_1[4],
                        'risk_1': group_1[5],
                        'total_minus_1': group_1[6],
                        'total_1': group_1[7],
                        'session_id_2': group_2[0],
                        'questionnaire_date_2': group_2[1],
                        'well_being_2': group_2[2],
                        'problem_severity_2': group_2[3],
                        'functioning_2': group_2[4],
                        'risk_2': group_2[5],
                        'total_minus_2': group_2[6],
                        'total_2': group_2[7],
                        'session_id_3': group_3[0],
                        'questionnaire_date_3': group_3[1],
                        'well_being_3': group_3[2],
                        'problem_severity_3': group_3[3],
                        'functioning_3': group_3[4],
                        'risk_3': group_3[5],
                        'total_minus_3': group_3[6],
                        'total_3': group_3[7]
                        },
                       ignore_index=True)
        columns = [
                'user_id',
                'external_id',
                'session_id_1',
                'questionnaire_date_1',
                'well_being_1',
                'problem_severity_1',
                'functioning_1',
                'risk_1',
                'total_minus_1',
                'total_1',
                'session_id_2',
                'questionnaire_date_2',
                'well_being_2',
                'problem_severity_2',
                'functioning_2',
                'risk_2',
                'total_minus_2',
                'total_2',
                'session_id_3',
                'questionnaire_date_3',
                'well_being_3',
                'problem_severity_3',
                'functioning_3',
                'risk_3',
                'total_minus_3',
                'total_3']
        df = df[columns]
    save_path = '/Users/gianluca/Desktop/fabias_data_updated/' + 'core_updated' + '.csv'
    df.to_csv(save_path, index=False)
