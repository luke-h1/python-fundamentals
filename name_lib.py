def upper_case_name(name): 
    return name.upper()

if __name__ == "__main__": 
    name = 'Luke'
    upper_case_new_name = upper_case_name(name)
    print(f'upper case name is {upper_case_new_name}')
    print(__name__)