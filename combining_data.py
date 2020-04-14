import glob
import csv
import pandas as pd
import os
import random

file_dir = "/Users/gianluca/Desktop/fabia_data_final/"
core_dir = file_dir + 'core' + '.csv'
demographic_dir = file_dir + 'demographic' + '.csv'
session_dir = file_dir + 'session' + '.csv'

files = [core_dir, demographic_dir, session_dir]


def extract_data(file_directory):
    file_object = open(file_directory, 'r')

    # reader = csv.reader(codecs.open(elem, 'rU', 'utf-8'))
    reader_2 = csv.reader(x.replace('\0', '') for x in file_object)

    rows = [row for row in reader_2 if row]
    rows = rows[1:]

    for i in rows:
        if len(i) == 1:
            rows.remove(i)

    stripped_rows = rows[1:]

    # get list of user ID's to iterate through
    id_list = []
    for i in stripped_rows:
        if i[0] not in id_list:
            id_list.append(i[0])

    return stripped_rows, id_list


def extract_headings(file_directory):
    file_object = open(file_directory, 'r')

    # reader = csv.reader(codecs.open(elem, 'rU', 'utf-8'))
    reader_2 = csv.reader(x.replace('\0', '') for x in file_object)

    rows = [row for row in reader_2 if row]
    headings = rows[0]

    return headings


core_heading = extract_headings(core_dir)
demographic_heading = extract_headings(demographic_dir)
session_heading = extract_headings(session_dir)

all_headings = [
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
 'total_3',
 'Gender',
 'Ethnic Origin',
 'Problem',
 'Problem Duration',
 'Previous Treatment',
 'Age Range',
 'Unemployed',
 'activation_date',
 'status',
 'last_activity',
 'depression_1',
 'depression_2',
 'depression_3',
 'depression_4',
 'depression_5',
 'depression_6',
 'depression_7',
 'depression_8',
 'anxious_1',
 'anxious_2',
 'anxious_3',
 'anxious_4',
 'anxious_5',
 'anxious_6',
 'anxious_7',
 'anxious_8',
 'suicide_1',
 'suicide_2',
 'suicide_3',
 'suicide_4',
 'suicide_5',
 'suicide_6',
 'suicide_7',
 'suicide_8',
 'serious_1',
 'serious_2',
 'serious_3',
 'serious_4',
 'serious_5',
 'serious_6',
 'serious_7',
 'serious_8']

raw_core_data = extract_data(core_dir)
raw_demographic_data = extract_data(demographic_dir)
raw_session_data = extract_data(session_dir)

core_id = raw_core_data[1]
demo_id = raw_demographic_data[1]
session_id = raw_session_data[1]

core_data = raw_core_data[0][int((len(raw_core_data[0])/2)):]
demo_data = raw_demographic_data[0][int(len(raw_demographic_data[0])/2):]
session_data = raw_session_data[0][int(len(raw_session_data[0])/2):]

# we need to first do the id's with full datasets
all_ids = core_id + demo_id + session_id
unique_ids = list(set(all_ids))

# full_data_id = core_id + demo_id + session_id
# for i in full_data_id:
#     if i not in (core_id and demo_id and session_id):
#         full_data_id.remove(i)

unique_ids = [[i] for i in unique_ids]

# here we will add demo data to core data if demo_id is in core_i
for i in unique_ids:
    for j in core_data:
        if i[0] == j[0]:
            i += j[2:]
        else:
            i += ['' for i in range(24)]

    for j in demo_data:
        if i[0] == j[0]:
            i += j[2:]
        else:
            i += ['' for i in range(7)]

    for k in session_data:
        if i[0] == k[0]:
            i += k[1:]
        else:
            i += ['' for i in range(35)]



df = pd.DataFrame(columns=all_headings)

