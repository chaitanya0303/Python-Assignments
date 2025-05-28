

# creating the file
 
f = open('sample.txt', 'w')


# writing to a file

lines = ['this is a sample text i am writing...']

with open('sample.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
        
        
 # appending the text
        
more_lines = ['', 'i am appending this text here ']

with open('sample.txt', 'a') as f:
    f.write('\n'.join(more_lines))
    
    
    
# reading 

with open('sample.txt') as f:
    contents = f.read()
    print(contents)