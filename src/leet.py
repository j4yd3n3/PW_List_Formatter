from itertools import product

leet_possibilities = {
    "a": ["4", "@"],
    "b": ["8", "6"],
    "c": ["<", "{", "("],
    "e": ["3"],
    "g": ["6", "9"],
    "h": ["#"],
    "i": ["1", "!"],
    "l": ["1", "!"],
    "o": ["0"],
    "q": ["9"],
    "s": ["5", "$", "z"],
    "t": ["7", "+"],
    "x": ["%"],
    "z": ["2"]
}
def leet(orig: set) -> set:
    leet_combinations = set() 
    for word in orig:
        char_options = []
        for char in word:
            if char.lower() in leet_possibilities:
                char_options.append([char] + leet_possibilities[char.lower()])
            else:
                char_options.append([char])

        for combination in product(*char_options):
            leet_word = ''.join(combination)
            leet_combinations.add(leet_word)  
    return leet_combinations
