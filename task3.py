import re

def normalize_phone(phone_number):
    try:
        
        # Видаляємо всі символи, крім цифр
        digits = re.sub(r'\D', '', phone_number)

    # Якщо номер починається з '380' — додаємо тільки '+'
        if digits.startswith('380'):
            return '+' + digits
    
    # Якщо номер починається з '0' або без коду країни — додаємо '+38'
        elif digits.startswith('0'):
            return '+38' + digits
    
    # Якщо просто набір цифр без префіксу — також додаємо '+38'
        else:
            return '+38' + digits
    except:
        return 'Invalid number'
    

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

for num in raw_numbers:
    print(normalize_phone(num))
