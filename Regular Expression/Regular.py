import re
a = "From stephenho@gmail.com sat fam 5"
def pts(a):
    k = re.findall("\S+@\S+", a)
    print(k)  # bien k luu tru truoc sau @
def check(a):
    k = re.search("\S+@\S+", a)
    if k:  # k True if search true, false if search false
        print(1)
    else:
        print(2)
def checkandpts(a):
    # Find all occurrences of the pattern
    matches = re.findall("^From ", a)
    # Print the results
    print(matches)
def doublesplit(a):
    words = a.split()
    email = words[1]
    pieces = email.split("@")
    print(pieces[1  ])
pts(a)
checkandpts(a)
check(a)
doublesplit(a)