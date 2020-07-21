from random import randrange
from random import choice
from faker import Faker
import datetime

fake = Faker()

minimum_age = 19
now = datetime.datetime.now()
current_year = now.year - minimum_age

# 22 AMERICAN NAMES
first_names = [
    'Saint',
    'Bowie',
    'Kylo',
    'Bode',
    'Creed',
    'Benicio',
    'Adonis',
    'Fox',
    'Nyall',
    'Kye',
    'Hakeem',
    'Shepherd',
    'Zayn',
    'Stoker',
    'Mikael',
    'Eason',
    'Karim',
    'Franco',
    'Apollo',
    'Zyaire',
    'Kingsley',
    'Bridger',
    'Grey'
]

# 100 AMERICAN SURNAMES
surnames = [
    'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
    'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',
    'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King',
    'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter',
    'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker' 'Evans', 'Edwards', 'Collins', 'Stewart',
    'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey', 'Rivera', 'Cooper',
    'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez', 'James', 'Watson',
    'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman',
    'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons',
    'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes', 'Sanchez', 'Mitchell'
]

workers = [
    'Builder',
    'Programmer',
    'Electrician',
    'Priest',
    'Shop assistant',
    'Plumber',
    'Lawyer',
    'Banker',
    'Baker',
    'Head Teacher',
    'Economic',
    'Photographer',
    'Historian',
    'IT Specialist',
    'Politician',
    'Cop',
    'Firefighter',
    'Pilot',
    'Teacher',
    'Waiter',
    'Truck driver',
    'Driver',
    'Journalist',
    'Reporter',
    'Judge',
    'Writer',
    'Dentist',
    'Surgeon',
    'Translator',
    'Webmaster',
    'Dancer',
    'Singer',
    'Soldier',
    'Sailer',
]

# -- BIRTHDAY DATA
months = [
    # I quarter
    'January',
    'February',
    'March',

    # II quarter
    'April',
    'May',
    'June',

    # III quarter
    'July',
    'August',
    'September',

    # IV quarter
    'October',
    'November',
    'December'
]

days = [ # IF MONTH IS != FEBRUARY --> ADD 3 MORE DAYS
    '1', '2', '3', '4', '5',
    '6', '7', '8', '9', '10',
    '11', '12', '13', '14', '15',
    '16', '17', '18', '19', '20',
    '21', '22', '23', '24', '25',
    '26', '27', '28', '29'
]

years = []
year = 1940
for i in range(0, (current_year - 1940)):
    years.append(year)
    year += 1

# born_year = choice(years)


# -- OTHER DATA
nationality = 'American'
numbers = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '0'
]

country_code = 1
# age = now.year - born_year

# print(age)
# print(years)


def full_name():
    global fullname
    fullname = choice(first_names) + ' ' + choice(surnames)
    return fullname


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        if year % 400 == 0:
            return True
    elif year % 4 != 0:
        return False


def birthday():
    global born_year, born_month, born_day
    birthday_date = ''
    rand_month = choice(months)
    rand_year = choice(years)
    born_year = rand_year
    born_month = rand_month

    if rand_month != 'February':
        x = 29
        while len(days) < 30:
            days.append(str(x))
            x += 1
    else:
        if not leap_year(rand_year):
            days.remove('29')

    rand_day = choice(days)
    born_day = rand_day

    return rand_day + ' ' + rand_month + ' ' + str(rand_year)


def age():
    year_age = now.year - born_year

    if now.month > months.index(born_month):
        return year_age
    elif now.month <= months.index(born_month):
        if now.day > days.index(born_day):
            return year_age
        else:
            return year_age - 1


def phone_number():
    phone_num = ''
    for num in range(0, 10):
        number = choice(numbers)
        if num == 3 or num == 6:
            phone_num += '-'

        phone_num += number

    return phone_num


def email_address():
    email = ''

    chars = [
        '-',
        '_',
        '.',
        ''
    ]

    email_page = [
        '@gmail.com',
        '@yahoo.com',
        '@hotmail.com',
        '@aol.com'
    ]

    fullname_list = fullname.split()
    [name.lower() for name in fullname_list]

    email += fullname_list[0].lower() + choice(chars) + fullname_list[1].lower() + choice(chars) + choice(email_page)
    return email


def identity():
    print("Full name: {}".format(full_name()))
    print("Birthday: {}".format(birthday()))
    print("Age: {}".format(age()))
    print("Phone number: {}".format('+' + str(country_code) + ' ' + phone_number()))
    print("Nationality: {}".format(nationality))
    print("Address: ")
    print(fake.address())
    print("Workplace: {}".format(choice(workers)))
    print("E-mail: {}".format(email_address()))


identity()

