# try:
#     код , який виконується
# except:
#     обробка вийнятку

# error = "!"
# try:
#     print("start code")
#     print(error)
#     print("No error")
# except:
#     print("We have error")

# print("code after capsule")

# try:
#     print("start code")
#     print(a)
#     print(10/0)
#     print("No error")
# except NameError:
#     print("We have error")
# except ZeroDivisionError:
#     print("0 / !")
#
# print("code after capsule")

# try:
#     print("start code")
#     print(a)
#     print(10/0)
#     print("No error")
# except (NameError, ZeroDivisionError):
#     print("We have error")
#
# print("code after capsule")

# try:
#     print("start code")
#     print(a)
#     print(10 / 0)
#     print("No error")
# except (NameError, ZeroDivisionError) as error:
#     print(f"Error: {error}")
#
# print("code after capsule")



# def checker(text):
#     if type(text) != str:
#         raise TypeError(f"Sorry, we can`t work with {type(text)}, we need calss STR!")
#
# try:
#     checker(5)
# except TypeError as error:
#     print(error)

# def calculator():
#     print("Вітаю в калькуляторі!")
#     while True:
#         operation = input("Виберіть дію(+,-,*,/): ")
#         if operation not in ['+', '-', '*', '/']:
#             print("не правильна дія.Попробуйте ще раз.")
#             continue
#         n1 = float(input("Перше число: "))
#         n2 = float(input("Друге числоу: "))
#         try:
#             if operation == '+':
#                 result = n1 + n2
#             elif operation == '-':
#                 result = n1 - n2
#             elif operation == '*':
#                 result = n1 * n2
#             elif operation == '/':
#                 result = n1 / n2
#             print("Result: ", result)
#         except ZeroDivisionError:
#             print("Error: division by zero")
#             continue
#             print(f"{n1} {operation} {n2} = {result}")
#
# calculator()
#
# 2 пара
#
# import logging
#
# logging.basicConfig(level=logging.DEBUG,
# filename="logs.log", filemode="w",
# format="[%(asctime)s] %(levelname)s %(message)s")
# logging.debug("text")
# logging.info("User123 succesfull logget to account 'login123'")
# logging.info("text")
# logging.warning("text")
# logging.error("text")
# logging.critical("text")