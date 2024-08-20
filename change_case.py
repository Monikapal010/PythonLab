def change_case(string, style):
    result = ""
    
    if style == "c":
        # Convert entire string to uppercase
        for char in string:
            if 'a' <= char <= 'z':  
                result += chr(ord(char) - ord('a') + ord('A'))
            else:
                result += char
    
    elif style == "s":
        for char in string:
            if 'A' <= char <= 'Z':  
                result += chr(ord(char) - ord('A') + ord('a'))
            else:
                result += char
    
    elif style == "r":
        for char in string:
            if 'A' <= char <= 'Z':  # Uppercase to lowercase
                result += chr(ord(char) - ord('A') + ord('a'))
            elif 'a' <= char <= 'z':  # Lowercase to uppercase
                result += chr(ord(char) - ord('a') + ord('A'))
            else:
                result += char
    
    elif style == "u":
        # Alternate between lowercase and uppercase based on the first character
        first_char = string[0]
        if 'A' <= first_char <= 'Z':
            # Start with uppercase, then alternate
            for i, char in enumerate(string):
                if i % 2 == 0 and 'a' <= char <= 'z':
                    result += chr(ord(char) - ord('a') + ord('A'))
                elif i % 2 != 0 and 'A' <= char <= 'Z':
                    result += chr(ord(char) - ord('A') + ord('a'))
                else:
                    result += char
        elif 'a' <= first_char <= 'z':
            # Start with lowercase, then alternate
            for i, char in enumerate(string):
                if i % 2 == 0 and 'A' <= char <= 'Z':
                    result += chr(ord(char) - ord('A') + ord('a'))
                elif i % 2 != 0 and 'a' <= char <= 'z':
                    result += chr(ord(char) - ord('a') + ord('A'))
                else:
                    result += char
    
    else:
        return "Invalid style code"
    
    return result

# Example usage:
print(change_case("Hello World", "c"))  
print(change_case("Hello World", "s"))  
print(change_case("Hello World", "r")) 
print(change_case("Hello World", "u"))  



