output_path = f"C:\\Users\\Suhail.DESKTOP-0CIIIA7\\OneDrive\\Desktop\\python_prgms\\Course\\100 days python\\day_24\\Output\\ReadytoSend\\letter_for_{stripped_name}.txt"
        with open(output_path, mode="w", encoding="utf-8") as completed_letter:
            completed_letter.write(new_letter)