import os
from datetime import datetime

def salvar_relatorio(tipo, nome_arquivo, dados, resultados=[]):
    pasta = "relatorios"
    os.makedirs(pasta, exist_ok=True)

    caminho = os.path.join(pasta, f"{nome_arquivo}.txt")
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("====================================\n")
        f.write("        RELATÓRIO HACKMETER\n")
        f.write("====================================\n\n")
        f.write(f"🕵️ Tipo de investigação: {tipo.upper()}\n")
        f.write(f"📅 Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")

        for chave, valor in dados.items():
            f.write(f"{chave.capitalize()}: {valor}\n")

        if resultados:
            f.write("\n🔎 Resultados encontrados:\n")
            for item in resultados:
                f.write(f"- {item}\n")

    return caminho
