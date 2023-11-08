file_path = "wk07b_ques2.txt"

# Read names from the file and create login IDs
login_ids = []
with open(file_path, "r") as file:
    for line in file:
        # Remove the trailing newline character and concatenate the first letter of the first name and the last name
        name_parts = line.strip('\n').split()
        first_letter = name_parts[0][0].lower()
        last_name = name_parts[-1].lower()
        login_id = first_letter + last_name[:8]  # Combine the first letter and up to 8 characters of the last name
        login_ids.append(login_id)

# Display the list of login IDs
print(login_ids)