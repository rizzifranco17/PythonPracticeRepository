
import re
#re.I means that ignores lower and upper cases
my_string = "This is the lesson number 21 :Lesson Regular Expression"
my_other_string = "This isn't the lesson number 6: File Handling"

match = re.match ("This is the lesson", my_string, re.I)
print (match)
start,end = match.span ()
print (my_string [start:end])

match = print(re.match("This is the lesson", my_other_string))
if not (match == None):
    print (match)
    start, end = match.span()
    print (my_string[start:end])

match = re.match ("This isn't the lesson", my_other_string)
if not (match == None):
    print (match)
    start, end = match.span ()
    print (my_other_string[start:end])

#Search 
search = re.search("lesson", my_string, re.I)
print (search)
start ,  end = search.span ()
print (my_string[start:end])

#FindAll

findall = re.findall ("lesson", my_string,re.I)
print (findall)

#split 

split = re.split

print(split (":", my_string))


#sub 
re.sub ("Expression", "expression", my_string)

print (re.sub ("Expression", "expression", my_string))
 #Only afffects the first match 

print (re.sub ("lesson|lesson", "Lesson", my_string))
#this way we can change more than one 


#Patterns
pattern = r"[l|L]" #search for l and L 
print (re.findall(pattern, my_string))

pattern = r"[l|L]esson" #search for l and L 
print (re.findall(pattern, my_string))

pattern = r"[0-9]"
print (re.findall(pattern, my_string))

pattern = r"[l|L]esson" 
print (re.match(pattern, my_string))
pattern = r"[0-9]" 
print (re.search(pattern, my_string))
pattern = r"\d"  #just numbers
print (re.findall(pattern, my_string))
pattern = r"\D" #just letters
print (re.findall(pattern, my_string))
pattern = r"[i]." 
print (re.findall(pattern, my_string))



email = "franco@rizzi.com.it"
pattern = r"^[a-zA-z0-9_+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9.]+$"
print (re.match(pattern,email))
print (re.search(pattern,email))
print (re.findall(pattern,email))