import phonenumbers

class Number_validation:
    def __init__(self) -> None:
        pass


    def number_validation(self,number):
        number=phonenumbers.parse(str(number))
        return phonenumbers.is_valid_number(number)
    


