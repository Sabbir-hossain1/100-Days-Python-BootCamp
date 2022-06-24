def format_name(firstName,LastName):
    formate_f_name = firstName.title()
    formated_l_name = LastName.title()
    return formate_f_name+" "+formated_l_name
resultantname = format_name('sabbir','hossain')
print(f"your name is {resultantname}")