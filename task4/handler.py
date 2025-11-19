import re
from decorators import input_error

"""
def normalize_phone(phone):
    pattern = r'^[0-9+\-()]+'
    if not re.fullmatch(pattern, phone):
        raise ValueError("Invalid phone number format")

    phone = re.sub(r"[^\d+]", "", phone)

    if phone.startswith("+380"):
        return phone
    if phone.startswith("380"):
        return "+" + phone
    if phone.startswith("0"):
        return "+38" + phone

    raise ValueError("Invalid phone format")

def normalize_name(name):
    name = name.strip()
    pattern = r'^[A-Za-z]+$'
    if not re.fullmatch(pattern, name):
        raise ValueError("Invalid name format")
    return name.capitalize()
"""

@input_error
def add_contact(args, contacts):
    name, phone = args  # тут може бути ValueError / IndexError
    name = name
    phone = phone
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args  # може бути ValueError / IndexError
    name = name
    if name not in contacts:
        raise KeyError
    new_phone = new_phone
    contacts[name] = new_phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]  # може бути IndexError
    return contacts[name]  # може бути KeyError

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved yet."

    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()
