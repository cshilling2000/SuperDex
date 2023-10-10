import csv

dex_filename = "natdex.csv"
alolan_forms_filename = "forms\\alola.csv"

# Pull the national dex from dex_filename.
def grab_names_and_numbers():
    names = []
    with open(dex_filename) as csvfile:
        for row in csvfile:
            names.append(row.split(',')[1].strip('\n')) 
    
    return names

# Gets a dex number from a Pokemon name.
def get_dex_no_from_name(names, name):
    return names.index(name) + 1

# Gets the name of a Pokemon from it's number.
def get_name_from_no(names, no):
    return names[no-1]

# Gets forms from a single file (excluding Tauros forms)
def get_forms(forms_filename):
    numbers = []
    with open(forms_filename) as csvfile:
        for row in csvfile:
            numbers.append(int(row.strip('\n'))) 
 
    return numbers

# Converts the national dex to a list of numbers.
def name_list_to_no_list(names):
    return range(1, len(names) + 1)

# Masks a list of numbers out of another list.
def number_mask(parent,mask):
    for element in mask:
        parent.remove(element)

# Adds an identifier to names: ex, "Alolan Raticate."
def form_name_maker(names,form_nos,form_name):
    form_names = []
    for no in form_nos:
        form_names.append(form_name + ' ' + get_name_from_no(names,no))
    return form_names
