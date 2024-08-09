from copy import deepcopy
import math

# Add up strings        .join
words = ["road", "Herbie", "Goes", "Bananas"];
text = ' '.join(words);
print(text);


# Indexation in string
text = "Big Red";
print(text[-1]); # Prints the last element in string
# index in range [-7, 7);


# Slicing
text = "Never Cry Wolf";
print(text[2 : 10]) # Prints in range [2, 10)
print(text[:13]) # Prints in range [0, 15)
print(text[4 : 11 : 2]) # Prints in range([4, 11), 2)


# Lenght of string        len
text = "GUS";
print(len(text));


# Substrings        find   index   count   
text = "The Apple Dumpling Gang";
print(text.find("Dumpling")); # Finds index of first appearance "Dumpling" in text otherwise returns -1
print(text.index("Dumpling")); # Finds index of first appearance "Dumpling" in text otherwise returns ValueError
print(text.count("a")); # Counts appearance of "a" in text


# Split Partition Splitlines       split   partition   splitlines
print(text.split(' ')); # Returns list of strings splited by ' ' ["The", "Apple", "Dumpling", "Gang"]
print(text.partition("Apple")); # Returns 3-tuple ("The " "Apple" " Dumpling Gang") otherwise returns (text, "", "");
print(text.splitlines()) # Returns list of strings divided by '\n' '\r' etc.


# Flex with letter's cases        capitalize(useless shit)   lower   upper   casefold
print(text.capitalize()); # Every words' first letter is capital
print(text.lower()); # tolower(string)
print(text.upper()); # toupper(string)
print("ŤÄäÔЯюЄЇ".casefold()); # agressive lowering Ä to ä etc. mostly used for string comparison


# Remove symbols   Ajustify text    Fill        strip lstrip rstring   ljust rjust center   
print(text.strip(' ')); # Removes leading and trailing spaces(lstring only leading, rstring only trailing)
print(text.rjust(40, ' ')); # Ajust string to left side of 40 symbols if 40 < len(text) returns text
print(text.ljust(40, ' ')); # Ajust string to right side of 40 symbols if 40 < len(text) returns text
print(text.center(40, '_')); #Ajust string to center of 40 symbols, other symbols are _ if 40 < len(text) returns text
print(text.zfill(40)); # rjust


# Replace Maketrans        replace   maketrans translate   
print(text.replace('z', 'b')); # Replace every z with b
print(text.translate(text.maketrans('pa', 'dg'))); # Replace but list, p into d and a into g


# Checks        startswitch endswith   islower isupper  istitle  isalpha    isdecimal  isdigit  isnumric  isalnum
print(text.startswith("The"));
print(text.endswith("Gang"));
print(text.islower());
print(text.isupper());
print(text.istitle()); # first letters are capital    otherwise false
print(text.isalpha());

text = "351587";

print(text.isdigit()); # number   otherwise return false
print(text.isdecimal()); # isanumber with base of 10    otherwise false
print(text.isnumeric()); # number   otherwise return false
print(text.isalnum()); # any of (3)above functions returns true otherwise false


# String formating
print("{1}" .format("blo", "bin"));
print("{0[1]}" .format(["str", "bebra"]));

print("{:>30}" .format(text)); # right aligned 
print("{:^30}" .format(text)) # center aligned
print("{:-^30}" .format(text)); # center aligned with symbols


# Number formating
num = 4321.5678;
print("{:0.2f}" .format(num));


# Lists
lst = ['a','b', 'm', 'e', 'b', 'a'];
lst[2] = 'o';
lst[3 : 6] = ['b', 'a', 'z'];
lst.remove('z') # Removes first appearance of 'a'

new_lst = deepcopy(lst); 
new_lst.append("d"); 

new_lst = [int(math.sqrt(i)) for i in range(1, 10)];
print(lst, new_lst);


# Tuples
tpl = (1, "2", True);
print("{}" .format(tpl[2]));
