#Open the prefixes/suffixes/roots file
filename = input("What is the name of the prefixes/suffixes/roots file? ")
file = open(filename, 'r')

#Open to word list file
word_list_filename = input("What is the name of the word list file? ")
word_list_file = open(word_list_filename, 'r')

#Ignore commented lines and blank lines
line = file.readline()
#Extract the word part in each section & store them
while line != '':
    line = file.readline()
    #Reading Roots...
    if line.startswith('#Roots'):
        root_list = []
        while line !='\n' and line.startswith != '#':
            line = file.readline()
            root_line = line.split('\t', 1)
            root_list.append(root_line[0])
        root_list.remove('\n')
        #print(root_list)
        print('Reading Roots...')
    #Reading Prefixes...
    elif line.startswith('#Prefixes'):
        prefix_list = []
        while line !='\n' and line.startswith != '#':
            line = file.readline()
            prefix_line = line.split('\t', 1)
            prefix_list.append(prefix_line[0])
        prefix_list.remove('\n')
        #print(prefix_list)
        print('Reading Prefixes...')
    #Reading Suffixes...
    elif line.startswith('#Suffixes'):
        suffix_list = []
        while line !='\n' and line.startswith != '#':
            line = file.readline()
            suffix_line = line.split('\t', 1)
            suffix_list.append(suffix_line[0])
        suffix_list.remove('\n')
        #print(suffix_list)
        print('Reading Suffixes...')

#Close the prefixes/suffixes/roots file
file.close()

#Search through all words in the word list file and keep 
#tally of the number of times each of the roots, prefixes 
#and suffixes were encountered.

#Create list of all words in the word list file
word_list = []

for line in word_list_file:
    word_list.append(line.strip('\n').lower())


roots = {}
prefixes = {}
suffixes = {}

#Counting..
print('Counting...')

#For each word in the word list see if it contains a root, suffix or prefix
for word in word_list:
    count = 0
    #Root can be anywhere in the word
    for root in root_list:
        if root in word: # and not word.startswith(root): and not word.endswith(root): 
            if root in roots:
                roots[root] = roots[root] + 1
            else:
                roots[root] = 1
            #print('Root: ' + root + '\tWord: ' + word)
        else:
            if root not in roots:
                roots[root] = 0
    #Prefix must begin the word
    for prefix in prefix_list:
        if word.startswith(prefix):
            if prefix in prefixes:
                prefixes[prefix] = prefixes[prefix] + 1
            else:
                prefixes[prefix] = 1
            #print('Prefix: ' + prefix + '\tWord: ' + word)
        else:
            if prefix not in prefixes:
                prefixes[prefix] = 0
    #Suffix must end the word
    for suffix in suffix_list:
        if word.endswith(suffix):
            if suffix in suffixes:
                suffixes[suffix] = suffixes[suffix] + 1
            else:
                suffixes[suffix] = 1
            #print('Suffix: ' + suffix + '\tWord: ' + word)
        else:
            if suffix not in suffixes:
                suffixes[suffix] = 0

#Printing results...
print('Printing results...')

#Output a file according to the following format:
#Roots: list of roots with number of times found
print('\nRoots:\n')
for root in sorted(roots):
    print(root + '\t' + str(roots[root]))
#print(roots)

#Prefixes: list of prefixes with number of times found
print('\nPrefixes:\n')
for prefix in sorted(prefixes):
    print(prefix + '\t' + str(prefixes[prefix]))
#print(prefixes)

#Suffixes: list of suffixes with number of times found
print('\nSuffixes:\n')
for suffix in sorted(suffixes):
    print(suffix + '\t' + str(suffixes[suffix]))
#print(suffixes)

word_list_file.close()
