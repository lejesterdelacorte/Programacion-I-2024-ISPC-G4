# Import desde Books
from .books.createBook import createBook
from .books.deleteBook import deleteBook
from .books.getBooks import getBooks
from .books.updateBook import updateBook

# Import desde Contact
from .contact.createContact import createContact
from .contact.deleteContact import deleteContact
from .contact.getContacts import getContacts
from .contact.updateContact import updateContact

#Register User
from .register.registerForm import registerForm

# Import desde Address
from .address.createAddress import createAddress
from .address.updateAddress import updateAddress

# Import desde MeetingPoint
from .meeting.createMeetingPoint import createMeetingPoint
from .meeting.deleteMeetingPoint import deleteMeetingPoint
from .meeting.getMeetingPoint import getMeetingPoints
from .meeting.updateMeetingPoint import updateMeetingPoint

#Import desde captcha
from .captcha.generate_captcha import generate_captcha

#Import desde login
from .login.login import login

#Import desde resetPassword
from .resetPassword.resetPassword import resetPassword

