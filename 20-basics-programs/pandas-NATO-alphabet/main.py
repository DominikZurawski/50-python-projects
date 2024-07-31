# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}


#print(nato_dictionary)
def generate_phonetic():
    123
    word = input("Input word to spell in NATO code: ").upper()
    try:
        list_phonetic_code = [nato_dictionary[k] for k in word]
    except KeyError:
        print("Sorty, only  letters in the alphabet please.")
        generate_phonetic()
    else:
        print(list_phonetic_code)


while True:
    generate_phonetic()
