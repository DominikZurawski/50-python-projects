import os

output_folder = "./ReadyToSend"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    message = letter_file.readlines()
with open("./Input/Names/invited_names.txt", "r") as name_file:
    names = name_file.readlines()

for name in names:
    name = name.strip("\n")
    new_message = ''.join(message)
    new_message = new_message.replace("[name]", name)
    with open(f"./ReadyToSend/invited_{name}.txt", "w") as file:
        file.write(new_message)







