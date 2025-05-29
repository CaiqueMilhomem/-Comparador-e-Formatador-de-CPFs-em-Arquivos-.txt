def formatar_cpf(cpf):
    cpf = cpf.strip()
    return cpf if len(cpf) == 11 and cpf.isdigit() else None

def carregar_cpfs_formatados(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.read().splitlines()
    return set(
        cpf_formatado
        for linha in linhas
        if (cpf_formatado := formatar_cpf(linha))
    )

def comparar_cpfs_txt(arquivo_txt1, arquivo_txt2):
    cpfs1 = carregar_cpfs_formatados(arquivo_txt1)
    cpfs2 = carregar_cpfs_formatados(arquivo_txt2)

    diferentes = cpfs1.symmetric_difference(cpfs2)

    if diferentes:
        print("CPFs diferentes encontrados:")
        for cpf in sorted(diferentes):
            print(cpf)
    else:
        print("Todos os CPFs coincidem entre os dois arquivos.")

# 🔧 Função para corrigir/ajustar os CPFs no arquivo (completa com zeros se necessário)
def ajustar_cpfs_arquivo(arquivo_txt):
    with open(arquivo_txt, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    linhas_formatadas = []
    for linha in linhas:
        cpf = linha.strip()
        if cpf.isdigit():
            linhas_formatadas.append(cpf.zfill(11) + "\n")

    with open(arquivo_txt, 'w', encoding='utf-8') as f:
        f.writelines(linhas_formatadas)

# Exemplo de uso
arquivo_txt1 = "caminho_arquivo_txt1"
arquivo_txt2 = "caminho_arquivo_txt2"

# Primeiro ajusta os arquivos
ajustar_cpfs_arquivo(arquivo_txt1)
ajustar_cpfs_arquivo(arquivo_txt2)

# Depois compara os dois arquivos
comparar_cpfs_txt(arquivo_txt1, arquivo_txt2)
