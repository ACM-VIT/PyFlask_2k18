# Python Strings Examples

# capitalize
str = "this is string example....wow!!!";
print "str.capitalize() : ", str.capitalize()

str.capitalize() :  This is string example....wow!!!

#count
str = "this is string example....wow!!!";
sub = "i";
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow";
print "str.count(sub) : ", str.count(sub)

str.count(sub, 4, 40) :  2
str.count(sub) :  1

#endswith
str = "this is string example....wow!!!";
suffix = "wow!!!";
print str.endswith(suffix)
print str.endswith(suffix,20)
suffix = "is";
print str.endswith(suffix, 2, 4)
print str.endswith(suffix, 2, 6)

True
True
True
False

#find
str1 = "this is string example....wow!!!";
str2 = "exam";
print str1.find(str2)
print str1.find(str2, 10)
print str1.find(str2, 40)

15
15
-1

#isalnum
str = "this2009";  # No space in this string
print str.isalnum()
str = "this is string example....wow!!!";
print str.isalnum()

True
False

#isalpha
str = "this";  # No space & digit in this string
print str.isalpha()
str = "this is string example....wow!!!";
print str.isalpha()

True
False

#isdigit
str = "123456";  # Only digit in this string
print str.isdigit()
str = "this is string example....wow!!!";
print str.isdigit()

True
False

#islower
str = "THIS is string example....wow!!!"; 
print str.islower()
str = "this is string example....wow!!!";
print str.islower()

False
True

#isalnum
str = u"this2009";  
print str.isnumeric()
str = u"23443434";
print str.isnumeric()

False
True

#isupper
str = "THIS IS STRING EXAMPLE....WOW!!!"; 
print str.isupper()
str = "THIS is string example....wow!!!";
print str.isupper()

True
False

#len
str = "this is string example....wow!!!";
print "Length of the string: ", len(str)

Length of the string:  32

#islower
str = "THIS IS STRING EXAMPLE....WOW!!!";
print str.lower()

this is string example....wow!!!

#strip
str = "0000000this is string example....wow!!!0000000";
print str.strip( '0' )

this is string example....wow!!!

#replace
str = "this is string example....wow!!! this is really string"
print str.replace("is", "was")
print str.replace("is", "was", 3)

thwas was string example....wow!!! thwas was really string
thwas was string example....wow!!! thwas is really string

#join
s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print s.join( seq )

a-b-c

#split
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( )
print str.split(' ', 1 )

['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']