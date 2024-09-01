from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError

class BirthdateValidator(Validator):
    def validate(self, document):
        date = document.text.strip()
        if len(date) != 10 or date[4] != '-' or date[7] != '-':
            raise ValidationError(message='El formato debe ser aaaa-mm-dd.')
        try:
            year, month, day = map(int, date.split('-'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
                raise ValueError()
        except ValueError:
            raise ValidationError(message='Fecha inválida.')

def input_birthdate():
    date = prompt('Ingrese su fecha de nacimiento (aaaa-mm-dd): ', validator=BirthdateValidator())
    return date