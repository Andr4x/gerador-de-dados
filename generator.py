# requeriments: 
# python 3.x.x
# biblioteca random
# biblioteca datetime

import random
from datetime import date


nome_masculino = [ "Lucas","Gustavo","Matheus","Vinicius","Madson","Wesley","Carson","Anderson","John","Dexer","Gilbar","Widson","Junior","Antonio","Francisco","Jair","Messias","Lula","Jordesto","Mario","Joao","Cid","Everton","Paulo","Bruce","Jefersson","Fernando",
"Johnson","Richard","Ricardo","Giles","Henry","Rick","Issac","Manoel","Jasper","Ivasper","Robert","Hobbert"] 

nome_feminino = [ "Ana","Maria","Alexandra","Larissa","Kauany","Aurora","Joana","Jelma","Clara","Melissa","Many","Raissa","Sabrina",
"Vitoria","Laura","Janna","Valdelte","Darci","Varsi","Alice","Sofia","Camila","Kamile","Laura","Lara","Valentina","Yasmin","Sophia",
"Anny","Fernanda","Lorensa","Manuela","Vitoria"] 

sobre_nome = [ "Ownigs","Bolsonaro","Mandson","Monalisa","Da Silva","Alves","Machado","Inacio","Borges","Madson","Viera","Alves de Oliveira",
"Lobo","Cobos","Coboltos","Issais","Oliveira","Hall","Halmilton","Redilson","Pereira","Da Costa","Elizabert","Hale","Thomas","King","Hight",
"Light","Torrens","Torres","Santos","Da Souza","Ferreira","Rodrigues","Almeida","Nascimento","Cavalho","Araujo","Ribeiro"] 

nome_rua = ["Princesa","Liberadora","Rainha","Elizabert","Martinho","Casa","Grande","Palmeira","Mundial","Rhino","Blood","Right","Agostinho"
"Anal","Nutter","Torres","Gemes","Arte","Museu","Principal"]

estados = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", 
"PE", "PI", "PR", "RJ", "RN", "RS", "RO", "RR", "SC", "SE", "SP", "TO"]

dominios_email = ["google.com","yahoo.com","hotmail.com","gmail.com","temp.com","real.io","contato.com","conect.me","locaweb.com",
"pt.com","host.me","org.com","pericia.com"]

print("Carregados:") 
print("[?] ["+str(len(nome_masculino))+"] Nomes Masculinos ")
print("[?] ["+str(len(nome_feminino))+"] Nomes femininos")
print("[?] ["+str(len(sobre_nome))+"] Sobrenomes")
print("[?] ["+str(len(estados))+"] Estados")
print("[?] ["+str(len(dominios_email))+"] Dominios de email")
print("[?] ["+str(len(nome_rua))+"] Nome de ruas")
print(" AVISO ESSES DADOS SAO FAKES PARA APROVACOES OU ALGO DO TIPO")
tipo_sexo = "NULL"

a = random.randrange(0,2)
if a == 1:
	gerar_nome = nome_masculino[random.randrange(1,39)]
	tipo_sexo = "Masculino"
if a == 2:
	gerar_nome = nome_feminino[random.randrange(1,33)]
	tipo_sexo = "Feminino"
if a == 0:
	gerar_nome = nome_feminino[random.randrange(1,33)]
	tipo_sexo = "Feminino"



def generate_cpf():                                                        
    cpf = [random.randrange(0, 9) for x in range(9)]                              
                                                                                
    for _ in range(2):                                                          
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
                                                                                
        cpf.append(11 - val if val > 1 else 0)                                                                                                            
    return "%s%s%s.%s%s%s.%s%s%s-%s%s" % tuple(cpf)

def generate_rg():                                                        
    rg = [random.randrange(0, 9) for x in range(9)]                              
                                                                                
    for _ in range(2):                                                          
        val = sum([(len(rg) + 1 - i) * v for i, v in enumerate(rg)]) % 11      
                                                                                
        rg.append(11 - val if val > 1 else 0)                                                                                                            
    return "%s%s%s.%s%s%s.%s%s%s-%s%s" % tuple(rg)

def generate_cell():                                                        
    rg = [random.randrange(1, 9) for x in range(8)]                              
                                                                                
    for _ in range(2):                                                          
        val = sum([(len(rg) + 1 - i) * v for i, v in enumerate(rg)]) % 11      
                                                                                
        rg.append(11 - val if val > 1 else 0)                                                                                                            
    return "(%s%s) 9 %s%s%s%s-%s%s%s%s" % tuple(rg)

def gerarate_estado(estado):
    if estado == "AC":
        return "Acre" 
    if estado == "AL":
        return "Alagoas"
    if estado == "AP":
        return "Amapá"
    if estado == "AM":
        return "Amazonas"
    if estado == "BA":
        return "Bahia"
    if estado == "CE":
        return "Ceará"
    if estado == "DF":
        return "Distrito Federal"
    if estado == "ES":
        return "Espirito Santo"
    if estado == "GO":
        return "Goias"
    if estado == "MA":
        return "Maranhao"
    if estado == "MT":
        return "Mato Grosso"
    if estado == "MS":
        return "Mato Grosso do Sul"
    if estado == "MG":
        return "Mina Gerais"
    if estado == "PA":
        return "Pará"
    if estado == "PB":
        return "Paraiba"
    if estado == "PR":
        return "Paraná"
    if estado == "PE":
        return "Pernambuco"
    if estado == "PI":
        return "Piaúi"
    if estado == "RJ":
        return "Rio De Janeiro"
    if estado == "RN":
        return "Rio Grande Do Norte"
    if estado == "RS":
        return "Rio Grande Do Sul"
    if estado == "RO":
        return "Rondônia"
    if estado == "RR":
        return "Roraina"
    if estado == "SC":
        return "Santa Catarina"
    if estado == "SP":
        return "São Paulo"
    if estado == "SE":
        return "Sergipe"
    if estado == "TO":
        return "Tocantins"
    else: 
        return "NULL"
def generate_cidade(estado):
    if estado == "AC":
        return "Rio Branco" 
    if estado == "AL":
        return "Maceió"
    if estado == "AP":
        return "Macapá"
    if estado == "AM":
        return "Manaus"
    if estado == "BA":
        return "Salvador"
    if estado == "CE":
        return "Fortaleza"
    if estado == "DF":
        return "Brasilia"
    if estado == "ES":
        return "Vitória"
    if estado == "GO":
        return "Goiânia"
    if estado == "MA":
        return "São Luiz"
    if estado == "MT":
        return "Cuiabá"
    if estado == "MS":
        return "Campo Grande"
    if estado == "MG":
        return "Belo Horizonte"
    if estado == "PA":
        return "Belém"
    if estado == "PB":
        return "João Pessoa"
    if estado == "PR":
        return "Curitiba"
    if estado == "PE":
        return "Recife"
    if estado == "PI":
        return "Teresina"
    if estado == "RJ":
        return "Rio De Janeiro"
    if estado == "RN":
        return "Natal"
    if estado == "RS":
        return "Porto Alegre"
    if estado == "RO":
        return "Porto Velho"
    if estado == "RR":
        return "Boa Vista"
    if estado == "SC":
        return "Florianópolis"
    if estado == "SP":
        return "São Paulo"
    if estado == "SE":
        return "Aracaju"
    if estado == "TO":
        return "Palmas"

def generate_nome_rua():
    a = random.randrange(0,2)
    if a == 1:
        gerar_nome_rua = nome_masculino[random.randrange(1,39)]
    if a == 2:
        gerar_nome_rua = nome_feminino[random.randrange(1,33)]
    if a == 0:
        gerar_nome_rua = nome_feminino[random.randrange(1,33)]
    gerar_sobre_nome_rua = nome_rua[random.randrange(1,9)]
    gerar_sobre_nome_2_rua = sobre_nome[random.randrange(1,37)]
    if gerar_sobre_nome_2_rua == gerar_sobre_nome:
        gerar_sobre_nome_2_rua = sobre_nome[random.randrange(1,37)]
    return "Rua " + gerar_nome_rua + " " +gerar_sobre_nome_rua + " " + gerar_sobre_nome_2_rua


def generate_cep():                                                      
    rg = [random.randrange(1, 9) for x in range(6)]                              
                                                                                
    for _ in range(2):                                                          
        val = sum([(len(rg) + 1 - i) * v for i, v in enumerate(rg)]) % 11      
                                                                                
        rg.append(11 - val if val > 1 else 0)                                                                                                            
    return " %s%s%s%s%s-%s%s%s" % tuple(rg)


gerar_sobre_nome = sobre_nome[random.randrange(1,37)]
gerar_sobre_nome_2 = sobre_nome[random.randrange(1,37)]
if gerar_sobre_nome_2 == gerar_sobre_nome:
	gerar_sobre_nome_2 = sobre_nome[random.randrange(1,37)]

gerar_idade = random.randrange(18,38)
data_atual = date.today()
gerar_ano_nasc = data_atual.year - gerar_idade
gerar_mes_nasc = random.randrange(1,12)
gerar_dia_nasc = random.randrange(1,28)
gerar_sigla = estados[random.randrange(1,27)]

def generate_email():
    a = random.randrange(0,2)
    if a == 1:
        email = gerar_nome + "@" + dominios_email[random.randrange(1,12)];
    else:
        email = gerar_nome +str(random.randrange(1,9999))+ "@" + dominios_email[random.randrange(1,12)];
    return email

maximo_leght = random.randrange(5,10)

def generate_senha():
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" + gerar_nome
    passwd = ""
    while len(passwd) != maximo_leght:
        passwd = passwd + random.choice(char)
        if len(passwd) == maximo_leght:
            return "Password: %s" % passwd



print("=========== Coded By Dr3xey ========")
print("-")

print(" Nome completo: "+gerar_nome + " " +gerar_sobre_nome + " " +gerar_sobre_nome_2)
print(" Idade: "+str(gerar_idade) + " Anos.")
print(" Sexo: "+tipo_sexo)
print(" Data de Nascimento: "+str(gerar_dia_nasc)+"/"+str(gerar_mes_nasc)+"/"+str(gerar_ano_nasc))
print(" CPF: " + generate_cpf() )
print(" RG: " + generate_rg() )
print(" Celular: " + generate_cell())
print(" Celular²: " + generate_cell())
print(" Estado: "+gerarate_estado(gerar_sigla))
print(" Cidade: "+generate_cidade(gerar_sigla))
print(" CEP: "+generate_cep())
print(" Rua: " + generate_nome_rua() )
print(" Numero: " +str(random.randrange(1111,9999)))
print(" Email: " + generate_email())
print(" Senha: " + str(generate_senha()))
