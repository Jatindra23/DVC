with open('artifact.txt','r') as f:
    text = f.read()

with open('artifact.txt','w') as f:

    text = f.write(text+'new line')
print(text)    