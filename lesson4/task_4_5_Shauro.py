from datetime import date

current_date = date.today()
date_was_born = input("Введите вашу дату рождения в формате день/месяц/год : ")
date_info = input("Введите любую дату что бы узнать сколько вам было лет в формате день/месяц/год: ")
date_was_born = date_was_born.split("/")
date_info = date_info.split("/")
if int(date_was_born[2]) > int(date_info[2]):
    print(f"Вы тогда еще не родились")
else:
    year = (int(date_info[2])) - (int(date_was_born[2]))
    month = abs(int(date_was_born[1]) - (int(date_info[1]))) * 30
    days = month + abs(int(date_was_born[0]) - int(date_info[0]))
    print(f"Вам было {year} полных лет и столько {days} дней")
