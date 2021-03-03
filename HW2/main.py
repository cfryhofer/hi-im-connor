if __name__ == '__main__':
    input = input()
    normal = ""
    backwards = ""
    for ch in input.lower():
        if ch != ' ':
            normal += ch
            backwards = ch + backwards

    if normal == backwards:
        print(input + " is a palindrome")
    else:
        print(input + " is not a palindrome")