# throw new error 
try:
    int('a')

except ValueError as e: 
    print('you can\'t do that :(' ) 
    print(e)