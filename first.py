import math

my_name = "Gia Bảo"
my_age = 19
is_dreaming = True
my_goal = "Become a Software Engineer"
skill_level = "Beginner"

print("MY PORTFOLIO: ")
print(f'Name: {my_name}')
print(f'Age: {my_age}')
print(f"Goal: {my_goal}")
print(f"Determined: {is_dreaming}")
print(skill_level)

complete_year = 1.5
finish_year = 2026 + complete_year
print(f'Complete in: {math.ceil(finish_year)}')

# Mình thấy ra kết quả là 2027.5 (năm không tồn tại) nên mình đã tự tìm hiểu về math trong Python