# Cleaning ENEM2013 file (6GB) by selecting only the data I'd like to work on (18 out of 219 columns)
# reduced the file from 6GB to around 300MB, better to load into pandas

file_enem2013 = open("data-source/MICRODADOS_ENEM_2013.csv", "r", encoding="ISO-8859-1") 
file_enem2013_result = open("data-prepared/enem_2013.csv", "a", encoding="ISO-8859-1") 

count = 0
headers_to_read = [
    "NO_MUNICIPIO_RESIDENCIA",  # candidate's city name
    "UF_RESIDENCIA",            # candidate's state code
    "NO_MUNICIPIO_ESC",         # candidate's city name
    "UF_ESC",                   # candidate's state code
    "IDADE",                    # candidate's age
    "ST_CONCLUSAO",             # candidate has finished high school
    "TP_ESCOLA",                # candidate's school type (1 = public or 2 = private)
    "Q003",                     # candidate's family monthly income  
    "Q004",                     # number of people who lives with the candidate in the same house
    "Q031",                     # "Q040 you left elementary school?"
    "Q034",                     # "have you left high school?"
    "Q040",                     # "how old were you when started working?"
    "Q042",                     # "I started working to help my parents"
    "Q043",                     # "I started working to support my family"
    "Q044",                     # "I started working to be independent"
    "Q045",                     # "I started working to gain experience"
    "Q046",                     # "I started working to afford my education"
    "Q076",                     # "how old were you when left the school?"
]

print("Processing header") 
file_headers = file_enem2013.readline() 
file_headers = file_headers.split(";")

# mapping columns index for selection
headers_index = []
for fh in file_headers:
    for htr in headers_to_read:
        if fh == htr:
            headers_index.append(file_headers.index(fh))

print(headers_index)

print("Processing rows")
file_enem2013_result.write(";".join(headers_to_read) + "\n")

while True: 
    count += 1
    
    line = file_enem2013.readline() 
    if not line: 
        break
    
    cells = line.split(";")
    
    file_row = ""
    for hi in headers_index:
        file_row += cells[hi] + ";"
    
    file_enem2013_result.write(file_row + "\n")

    if count % 10000 == 0:
        print(f"Rows processed: {count}")
  
# Closing files 
file_enem2013.close() 
file_enem2013_result.close() 