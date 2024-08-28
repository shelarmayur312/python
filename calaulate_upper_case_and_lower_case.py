''' Write a Python function that accepts a string and calculate the number of upper 
case letters and lower case letters.
Sample String: 'The quick Brown Fox' Expected
Output: No. of Upper case characters: 3
No. of Lower case characters: 13'''

def string_test(s):
    d={"upper_case":0,"LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["upper_case"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass

        print("Orignal String:",s)
        print("No.of Upper case characters:",d["upper_case"])
        print("No.of Lower case characters:",d["LOWER_CASE"])

string_test('The quick Brown Fox')