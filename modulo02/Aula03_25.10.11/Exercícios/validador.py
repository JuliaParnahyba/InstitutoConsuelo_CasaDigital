import string

# Recebe o argumento pelo terminal
frst_input = input("Digite sua senha: ")

# Função de validação
def validador_senha(senha):
    """
    Função que recebe um argumento, passado pelo usuário e valida de acordo às regras de negócio:

    Argumento:
        senha: senha do usuário, recebida via argumento
    
    Regras de negócio:
        Mínimo de 8 caracteres
        Letra maiúscula
        Letra minúscula
        Número
        Caractere especial
    """ 

    # Flags de controle
    has_error_length = False
    has_error_upper = False
    has_error_lower = False
    has_error_num = False
    has_error_char = False

    # Array para receber mensagens de erro
    error_msg = []

    # Verfica o tamanho
    if len(senha) < 8:
        if not has_error_length:
            error_msg.append("mínimo de 8 caracteres;")
            has_error_length = True
    
    # Verifica se contém caracteres maiúsculos
    if not any(char.isupper() for char in senha):
        if not has_error_upper:
            error_msg.append("necessário letra maiúscula;")
            has_error_upper = True
    
    # Verifica se contém caracteres minúsculos
    if not any(char.islower() for char in senha):
        if not has_error_lower:
            error_msg.append("necessário letra minúscula;")
            has_error_lower = True
    
    # Verifica se contém caracteres numéricos
    if not any(char.isdigit() for char in senha):
        if not has_error_num:
            error_msg.append("necessário caracter numérico;")
            has_error_num = True
    
    # Verifica se contém caracteres especiais
    if not any(char in string.punctuation for char in senha):
        if not has_error_char:
            error_msg.append("necessário caracter especial;")
            has_error_char = True

    # Verifica se array de mensagem está populado
    if error_msg:
        print("\nForam encontrados erros na validação da senha:")
        for i in error_msg:
            print(f"{i}")
        
        # Solicita nova senha ao usuário
        print("\n---------------------------------------\n")
        novo_input = input("Digite nova senha: ")
        validador_senha(novo_input)
    
    # Verifica se array de mensagem está vazia e notifica que senha foi aceita
    if not error_msg:
        print("\nSua senha passou no validador.")

# Chama função de validação
validador_senha(frst_input)

        