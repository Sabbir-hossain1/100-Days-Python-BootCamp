# -----open a file and read data as a list--------


# with open("./weather_data.csv") as data:
#     data_list = data.readlines()
#     print(data_list)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# series_list = data["temp"]
# average = sum(series_list) / len(series_list)
# print(average)
# print(series_list)
# print(series_list.max())
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(f"{monday_temp * (9 / 5) + 32} Fahrenheit")

# data_dict = {
#     "student": ["Amy", "James", "Sabbir"],
#     "score": [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)


# ----Read a CSV file, Extract data from CSV and make a DataFrame and Convert to CSV--------------------


# import pandas as pd
# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrel_count, red_squirrel_count, black_squirrel_count)
#
# data_dict = {
#     "Fur color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
# }
# df = pd.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
# # print(data_dict)


# -- U.S State Games
import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Manually find all co-ordinates of the States
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []
missing_sates = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct",
                                    prompt="What is the state's name?").title()
    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missing_sates.append(state)
        new_data = pd.DataFrame(missing_sates)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
