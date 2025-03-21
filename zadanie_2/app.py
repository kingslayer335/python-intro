#Piotr Artym, 122212
from datetime import datetime
def is_email_on_the_list(list, email):
    if email in list:
        return True
    return False

def square_of_number(number):
    return number * number

def sort_numbers(list):
    list.sort()
    return list

def convert_date(date):
    return date.strftime('%Y-%m-%d')
    
def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length-i-1]:
            return False
    return True