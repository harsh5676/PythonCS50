# Convert funtion which converts emoticons into emojis and returns all other text unchanged
def convert(sen):
    sen = sen.replace(":)", "🙂")
    sen = sen.replace(":(", "🙁")
    # print(sen)
    return sen

# Defining main function which takes input from the user
def main():
    sentence = input()
    # Function call for convert function to check the user's input & convert emoticons into emojis present.
    # c = convert(sentence)
    print(convert(sentence))

# Calling main function
main() 