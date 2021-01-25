# Cleaning CADASTRO_MATRICULAS_REGIAO_* files by selecting only the data I'd like to work on

file_result = open("data-prepared/school_infrastructure_2012.csv", "a", encoding="ISO-8859-1") 

count = 0
headers_to_read = [
    "UF",                           # school's state
    "Municipio",                    # school's city 
    "Situacao_Funcionamento",       # is school active?
    "SALA_DIRETORIA",               # has directors room
    "SALA_PROFESSOR",               # has teachers room
    "SECRETARIA",                   # has secretary
    "REFEITORIO",                   # has a place for meal
    "AUDITORIO",                    # has auditorium
    "LABORATORIO_INFORMATICA",      # has computer room
    "LABORATORIO_CIENCIAS",         # has science lab
    "QUADRA_ESPORTES_COBERTA",      # has sports pitch
    "QUADRA_ESPORTES_DESCOBERTA",   # has sports pitch open air
    "PARQUE_INFANTIL",              # has kindengarden
    "BIBLIOTECA",                   # has library
    "SANITARIO_DENTRO_PREDIO",      # has bathroom in the building
    "SANITARIO_FORA_PREDIO",        # has bathroom outside the building
    "ALIMENTACAO",                  # offers meal
    "AGUA_INEXISTENTE",             # has water
    "ENERGIA_INEXISTENTE",          # has electricity
    "ESGOTO_INEXISTENTE",           # has sewage collection
    "INTERNET",                     # has internet connection
    "COMPUTADORES",                 # has computers
    "EQUIP_DVD",                    # has DVR
    "EQUIP_IMPRESSORA",             # has printers
    "EQUIP_COPIADORA",              # has copy machines
]

files_regions = [
    "data-source/CADASTRO_MATRICULAS_REGIAO_CENTRO-OESTE_2012.csv",
    "data-source/CADASTRO_MATRICULAS_REGIAO_NORDESTE_MA_PI_CE_RN_PB_2012.csv",
    "data-source/CADASTRO_MATRICULAS_REGIAO_NORDESTE_PE_AL_SE_BA_2012.csv",
    "data-source/CADASTRO_MATRICULAS_REGIAO_NORTE_2012.csv",
    "data-source/CADASTRO_MATRICULAS_REGIAO_SUDESTE_ES_RJ_2012.csv",
    "data-source/CADASTRO_MATRICULAS_REGIAO_SUDESTE_MG_2012.csv",
    "data-source/CADASTRO_MATRICULAS_REGIAO_SUDESTE_SP_2012 (1).csv",
    "data-source/CADASTRO_MATRICULAS_REGIAO_SUL_2012 (1).csv"
]

for file_region in files_regions:
    file_region = open(file_region, "r", encoding="ISO-8859-1") 

    print("Processing header") 

    # discard the first rows, it's a weird header
    for i in range(11):
        file_region.readline()

    file_headers = file_region.readline() 
    file_headers = file_headers.split(";")

    # mapping columns index for selection
    headers_index = []
    for fh in file_headers:
        for htr in headers_to_read:
            if fh == htr:
                headers_index.append(file_headers.index(fh))

    print(headers_index)

    print("Processing rows")
    if count == 0:
        file_result.write(";".join(headers_to_read) + "\n")

    while True: 
        count += 1
        
        line = file_region.readline() 
        if not line: 
            break
        
        cells = line.split(";")
        
        file_row = ""
        for hi in headers_index:
            file_row += cells[hi] + ";"
        
        file_result.write(file_row + "\n")

        if count % 10000 == 0:
            print(f"Rows processed: {count}")
     
    file_region.close() 

file_result.close() 