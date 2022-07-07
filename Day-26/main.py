# # import random
# import pandas as pd
#
# # ------------------------List Comprehension---------------------------------
# # number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# # new_list = [item + 1 for item in number]
# # print(new_list)
#
# # double_each_item = [item * 2 for item in range(1, 6)]
# # print(double_each_item)
#
# # names = ["Sabbir", "Shamima", "Salman", "Momin Mia", "Shajeda Begum"]
# # all_cap_names = [name.upper() for name in names if len(name) < 10]
# # print(all_cap_names)
#
# # ----------------------Dictionary Comprehension--------------------
#
# # student_score = {student: random.randint(1, 100) for student in names}
# # # new_dictionary = {new_key:new_value for (key, value) in dictionary.items()}
# # passed_student = {student: score for (student, score) in student_score.items() if score > 70}
# # print(student_score)
# # print(passed_student)
#
# # sentence = "What is the Airspeed velocity of an unladen swallow?"
# # result = {word: len(word) for word in sentence.split()}
# # print(result)
#
# # weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday":15, "Thursday": 14, "Friday": 21, "Saturday": 22,
# "Sunday": 24} # weather_f = {day: (value * 9/5) + 32 for (day, value) in weather_c.items()} # print(weather_f)
#
# # -------------------loop Throw a Data Frame--------------------
#
# student_dict = {
#     "student": ["Sabbir", "Salman", "Shamima"],
#     "score": [50, 60, 70]
# }
# # Dictionary to DataFrame
# student_dict_data_frame = pd.DataFrame(student_dict)
# # ------------------ Manually loop through DataFrame------------------------
# # for (key, value) in student_dict_data_frame.items():
# #     print(key)
# #     print(value)
# # --------------------Manually loop through DataFrame row ------------------
# for (index, row) in student_dict_data_frame.iterrows():
#     # print(row)
#     # print(f"{row.student}: {row.score}")
#     if row.student == "Sabbir":
#         print(row.score)

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
new_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
user_input = input("Enter a word: ").upper()
nato_word_list = [new_dictionary[letter] for letter in user_input]
print(nato_word_list)
