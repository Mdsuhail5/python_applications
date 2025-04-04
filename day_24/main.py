# # with open("my_file.txt", encoding="utf-8")as file:
# #     contents = file.read()
# #     print(contents)


# with open("my_file.txt", mode="a")as file:
#     file.write("New text.")
# # modes
# # write:  w
# # append: a
# # read :  r
# with open("new_file.txt", mode="w")as file:
#     file.write("New text.")


# with open(r"\Users\Suhail.DESKTOP-0CIIIA7\OneDrive\Desktop\f1.txt")as text:
#     content = text.read()
# print(content)

# # Absolute path: it is always relative to your root
# # Relative path: it is always relative to your current working directory

PLACEHOLDER = "[name]"
with open(r"C:\Users\Suhail.DESKTOP-0CIIIA7\OneDrive\Desktop\python_prgms\Course\100 days python\day_24\Input\Names\invited_names.txt", encoding="utf-8") as names:
    names_list = names.readlines()

with open(r"C:\Users\Suhail.DESKTOP-0CIIIA7\OneDrive\Desktop\python_prgms\Course\100 days python\day_24\Input\Letters\starting_letters.txt", encoding="utf-8") as letters:
    letter_file = letters.read()
    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_file.replace(PLACEHOLDER, stripped_name)

        output_path = f"C:\\Users\\Suhail.DESKTOP-0CIIIA7\\OneDrive\\Desktop\\python_prgms\\Course\\100 days python\\day_24\\Output\\ReadytoSend\\letter_for_{stripped_name}.txt"
        with open(output_path, mode="w", encoding="utf-8") as completed_letter:
            completed_letter.write(new_letter)
