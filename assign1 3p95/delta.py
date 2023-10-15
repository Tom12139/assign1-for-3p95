def is_failing(input_str):
    output_str = processString(input_str)
    # Add a condition to check whether the output is as expected or not
    # Return True if the output is incorrect (test fails), otherwise False

def delta_debugging(input_str):
    n = 2  # Initial granularity
    while n <= len(input_str):
        start_idx = 0
        subset_found = False
        while start_idx < len(input_str):
            subset = input_str[start_idx:start_idx+n]
            if is_failing(subset):
                input_str = subset
                n = max(n-1, 2)
                subset_found = True
                break
            start_idx += n
        if not subset_found:
            n += 1
    return input_str

def processString(input_str):
    output_str = ""
    for char in input_str:
        if char.isupper():  
            output_str += char.lower()  
        elif char.islower():  
            output_str += char.upper()  
        elif char.isnumeric():  
            output_str += char  
        else:
            output_str += char  
    return output_str


# Test the delta_debugging function with the given input values
inputs = ["abcdefG1", "CCDDEExy", "1234567b", "8665"]
for input_str in inputs:
    minimized_input = delta_debugging(input_str)
    print(f"Minimized input for '{input_str}': '{minimized_input}'")
