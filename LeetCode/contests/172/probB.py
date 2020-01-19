text = raw_input()

text = text.split(" ")



max_str_len = -1

for item in text:
    if len(item) > max_str_len:
        max_str_len = len(item)
        
for item in range(len(text)):
    text[item] = text[item].ljust(max_str_len, " ")

output = []

for k in range(max_str_len):
    s  = ''
    for item in (text):
        s += item[k]
        
    output.append(s)
    
    
for out in range(len(output)):
    output[out] = output[out].rstrip()
print(output)