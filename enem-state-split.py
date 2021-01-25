# Spliting enem_2013 cleaned file into files by state because github allows only files up to 100MB

file_enem2013 = open("data-prepared/enem_2013.csv", "r", encoding="ISO-8859-1") 
file_by_state = {}

count = 0
file_headers = file_enem2013.readline()

print(file_headers)
while True: 
    count += 1
    
    line = file_enem2013.readline() 
    if not line: 
        break
    
    state = line.split(";")[1]
    
    if state not in file_by_state:
        file_by_state[state] = open(f"data-prepared/enem_2013_{state}.csv", "a", encoding="ISO-8859-1") 
        file_by_state[state].write(file_headers)
    
    file_by_state[state].write(line)

    if count % 10000 == 0:
        print(f"Rows processed: {count}")
  
# Closing files 
file_enem2013.close() 
for f in file_by_state:
    f.close()