calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    string = input("Enter your string and press Enter button: ")
    global calls
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    string = input("Enter your string to find: ")
    list_to_search = input("Enter your list of several words spelled with space: ").split()
    string_to_search = ''.join(str(el) for el in list_to_search)
    string.lower()
    string_to_search.lower()
    print(string in string_to_search)
    global calls
    count_calls()

print(string_info(""))
is_contains("", [])
print(calls)