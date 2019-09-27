# Data Types In Python Are
#     1. Integers
#     2. Floating Point Numbers
#     3. Strings
#     4.Boolean
#     5.Tuple
#     6.Dictionary

######################################## 1. Integers ##########################################
# In Python 3, there is effectively no limit to how long an integer value can be

#___________________________________ i. Decimal Integers _____________________________________
int_num = 3
print(int_num)

#____________________________ ii. Binary Integers (Base 2 [only 1 and 0 s are allowed]) __________________
    # Binary Inetegers Can Be Represented Using 0b (zero + lowercase letter 'b') or 0B (zero + uppercase letter 'B')
bi_num = 0b101
print(bi_num)    

bi_num = 0B1010
print(bi_num)

# bi_num = 0b102 
# above statement is invalid since binary numbers have base 2

#____________________________ iii. Octal Integers (Base 8 [0-7] numbers are allowed)______________
    # Octal Inetegers Can Be Represented Using 0o (zero + lowercase letter 'o') or 0O (zero + uppercase letter 'O')
oct_num = 0o1024
print(oct_num)    

oct_num = 0O104
print(oct_num)

# oct_num = 0O129 
# above statement is invalid since octal numbers have base 8


#____________________________ iv. Hexadecimal Integers (Base 16 [0-9] numbers and [A-F] are allowed)______________
    # Hexadecimal Inetegers Can Be Represented Using 0x (zero + lowercase letter 'x') or 0X (zero + uppercase letter 'X')
hex_num = 0x1024A
print(hex_num)    

hex_num = 0X104
print(hex_num)

# oct_num = 0O129 
# above statement is invalid since hexadecimal numbers have base 16


##################################### 2. Floating Point Numbers ##############################
    # float values are specified with a decimal point. 
    # Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation

float_num = 4.2
print(float_num)    

float_num = 4. #assigns 4.0 value as we ommited fractional part
print(float_num)

float_num = .23 #assigns 0.23 value as we ommited decimal part
print(float_num)

float_num = 4e2 # evaluated as 4 * 10^2 [value of e is 10]
print(float_num)

#____________________________________ Complex Numbers ________________________________________
# Complex numbers are specified as <real part>+<imaginary part>j.
complex_num = 4 + 3j
print(complex_num)

########################################### 3. Strings ########################################
string = "This is a double quoted \"string\""
print(string)

string = 'This is a single quoted \'string\''
print(string)

string = 'this is a \
    multiline string \
    continued with \\ at the end of line. It Does not Prints All The Text Content As It IS(does not show new line and tabs)'

print(string)

string = """ This is 
a multiline String .    It Prints All The Text Content As It IS (shows new line and tabs)."""
print(string)


########################################### 4. Boolean ########################################
    #Boolean type may have one of two values, True or False:
boolean_var = True
print(boolean_var)

boolean_var = False
print(boolean_var)

########################################## 5. Tuples #########################################
    # Tuple is another form of collection where different type of data can be stored. Similat to array.
    # Tuples are enclosed in parenthesis and cannot be changed.
tuple = ('abc', 12, 43, 'pqr')
print(tuple)

########################################## 6. Dictionary #########################################
    # Dictionary is a collection which works on a key-value pairs.
    # it works like an associated array where no two keys can be same.
    # Dictionaries are enclosed by curly braces ({}) and values can be retrieved by square bracket([]).

dictionary={'name':'Test User','id':100,'marks': 500}  
print(dictionary) #prints entire dictionary
print(dictionary.keys()) #prints keys in dictionaries
print(dictionary.values()) #prints values in dictionaries

