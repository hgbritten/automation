import re
import shutil
import glob


with open(
    "/home/the_procter/codefellows/code401/automation/automation/potential_contacts.txt"
) as file:
    potentials = file.read()


phone = []

phone.extend(
    re.findall(
        "\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}",
        potentials,
    )
)

new_nums = list(set(phone))
sort_nums = new_nums.sort()

phone_num_str = ""
for num in new_nums:
    phone_num_str += num + ", "

print(phone_num_str)

with open(
    "/home/the_procter/codefellows/code401/automation/automation/phone_numbers.txt", "w"
) as file:
    phone_nums = file.write(phone_num_str)

email_address = []
email_address.extend(
    re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", potentials)
)

new_list = list(set(email_address))
sort_email = new_list.sort()

email_str = ""
for string in new_list:
    email_str += string + ", "

print(email_str)

with open(
    "/home/the_procter/codefellows/code401/automation/automation/emails.txt", "w"
) as file:
    emails = file.write(email_str)
