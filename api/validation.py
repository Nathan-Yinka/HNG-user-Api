def validate_name_space(name):   #function to run validation of the posted data
    names = name.split()
    for name in names:
        name = name.strip()
        if not name.isalpha():
            return False
        name = " ".join(names)
    return name.lower()