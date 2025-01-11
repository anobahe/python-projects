import pandas
#
# list1 = ['Ohio', 'New', 'York']
#
# data = pandas.read_csv("50_states.csv")
#
# new_state = "Ohio"
# state = data[data.state == new_state]
# print(state.x)

student_dict = {"studnet": ["Angela", "James", "Lily"],
                "score": [56, 76, 98]}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

for key,value in student_data_frame.items():
    print(key,value)