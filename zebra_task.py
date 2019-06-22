import json
import random
import os.path

# This script gets a .txt file with multiple JSON objects in it,
# divides them into individual JSON objects, adds a randomized field
# indicating successful or failed login, and prints out the paths of
# 2 output files: 1 is a .txt file containing all input JSONs
# with the randomized login field, and the second is a list if all
# usernames who's login success field indicates a failed login attempt at
# least once.

file_path = input('Please provide input file path: ')


def is_json(attempt_string):
    # This function gets a string, and returns True if the string is a valid JSON object,
    # or False if it's not
    try:
        json_file = json.loads(attempt_string)
    except:
        return False
    return True


def find_jsons(txt):
    # This function gets a string, and iterates over it to find all valid JSON objects within it.
    # Using 2 nodes, 'attempt_start" and 'attempt_end', it starts with the first char of the string, and in each
    # iteration it adds another char to the substring, until it finds a valid JSON object. IT will then add
    # it to a list, and move the 'attempt_start' node to the letter after the last letter of the previous JSON.
    # It returns a list of all the valid JSON objects as dictionaries
    json_list = []
    attempt_start = 0
    attempt_end = 1
    while attempt_end < len(txt)+1:
        cur_attempt = txt[attempt_start:attempt_end]
        if is_json((cur_attempt)):
            json_list.append(json.loads(cur_attempt))
            attempt_start = attempt_end
        attempt_end += 1
    return json_list


def random_result():
    # Returns a random choice of either True or False
    return random.choice([True,False])


def login_attempt(user_list):
    # The function gets a list of dictionaries. For each dict, it gets a random value of either True or False,
    # and based on it adds a new field to the dict, 'actual result', indicating a successful or failed login attempt.
    # If it's a failed attempt, the username will be added to a list of failed login attempts.
    # It returns a list of modified dictionaries, and a list of usernames who failed the login attempt.
    failed_users = []
    for user in user_list:
        if random_result():
            user["actual_result"] = 'successfull login'
        else:
            user["actual_result"] = 'login failed'
            failed_users.append(user['scenario_data']['username'])
    return user_list, failed_users

def remove_duplicates(user_list):
    # The function removes duplicates from a list
    return list(set(user_list))

def write_to_file(file_path, data_list):
    # The function gets a full file path and data in the form of a list,
    # and writes the data into a new file, locates in the specified path.
    with open('{}'.format(file_path), 'w') as file_writer:
        file_writer.write("\n".join([json.dumps(item) for item in data_list]))


def run_test(path):
    # This function operate as the Main of the file. It gets a complete file path, with input JSON objects.
    # It creates and saves 2 .txt files, once with all the input JSON objects with an added 'actual result' field,
    # and the other contains all the usernames whose login attempt failed.
    # It then print their paths to the console.
    file_dir = os.path.split(path)[0]
    with open(path) as file_reader:
        file_txt = file_reader.read()
    json_list = find_jsons(file_txt)
    json_list, failed_users = login_attempt(json_list)
    failed_users = remove_duplicates(failed_users)
    json_output_path = os.path.join(file_dir, 'json_output.txt')
    failed_users_path = os.path.join(file_dir, 'failed_users.txt')
    write_to_file(json_output_path, json_list)
    write_to_file(failed_users_path, failed_users)
    print('The JSON output file can be found here: {} \nThe Failed Users output file can be found here: {}'.format(json_output_path, failed_users_path))


run_test(file_path)