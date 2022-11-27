def check_parenthesis(x):
    stack = []
    opening_brackets = ['(','{','[']
    closing_brackets = [')','}',']']
    bracket_map = {')':'(', '}':'{', ']':'['}
    for i in x:
        if i in opening_brackets:
            stack.append(i)
        elif i in closing_brackets:
            if not stack:
                return False
            last_opening_bracket = stack.pop()
            if bracket_map[i] != last_opening_bracket:
                return False
        else: 
            return False
    if stack:
        return False
    return True
            

def __main__():

    input_str= input("Enter a string containing characters '(', ')', '{', '}', '[' or  ']'")
    if  input_str == "" or input_str == None:
        print("True")
        return
    result = check_parenthesis(input_str)
    if result:
        print("True")
    else:
        print("False")
__main__()
