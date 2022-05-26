# Bibliotecas
import os
from tkinter import filedialog
from zipfile import ZipFile, ZIP_DEFLATED


def compactar_tudo(diretorio, ignore_zips=True):
    nomesarquivos = os.listdir(diretorio)

    # Ignora arquivos que já estão compactados/zipados.
    if ignore_zips:
        nomesarquivos = [fn for fn in nomesarquivos if not fn.endswith('.zip')]

    # lista todos os arquivos e pastas do caminho informado.
    for nome in nomesarquivos:
        fullpath = os.path.join(diretorio, nome)
        # print(f"FullPath {fullpath}")

        # Quanto for pasta 
        if os.path.isdir(fullpath):
            nomezip = os.path.join(diretorio, nome + '.zip')
            arquivozip = ZipFile(nomezip, "a", compression=ZIP_DEFLATED)
            # print(f"NomeZip {nomezip}")

            # Percorre o diretório para encontrar arquivos dentro das pastas (caminho normal e relativo)
            for raiz, dirs, arquivos in os.walk(fullpath):
                for arq in arquivos:
                    relativo = os.path.relpath(raiz, diretorio)
                    arquivozip.write(os.path.join(raiz, arq),
                                     os.path.join(relativo, arq))
            arquivozip.close()

        # Quanto for arquivo 
        else:
            semextensao = nome.split('.')[0]
            nomezip = os.path.join(diretorio, semextensao + '.zip')
            arquivozip = ZipFile(nomezip, "w", compression=ZIP_DEFLATED)
            arquivozip.write(fullpath, nome)
            arquivozip.close()

    # Retorna o número de arquivos compactados.
    return len(nomesarquivos)

if __name__ == '__main__':
    # pasta = input("Digite o endereço da pasta a ser compactada: ")
    pasta = filedialog.askdirectory()
    print(f"Compactando arquivos em {pasta}")
    n = compactar_tudo(pasta)
    print(f"{n} arquivos compactados com sucesso")