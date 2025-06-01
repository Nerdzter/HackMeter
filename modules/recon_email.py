from duckduckgo_search import DDGS
from rich.console import Console
import time
import os

console = Console()

def verificar_email(email):
    console.print(f"\n[cyan]Buscando na web por rastros de:[/cyan] {email}")
    resultados = []

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(email, max_results=10):
                console.print(f"[bold green]{r['title']}[/bold green]\n{r['href']}\n")
                resultados.append(f"{r['title']} → {r['href']}")
    except Exception as e:
        console.print(f"[red]Erro na busca DuckDuckGo:[/red] {e}")
        console.print("[yellow]Aguardando 10 segundos antes de continuar...[/yellow]")
        time.sleep(10)
        return []

    salvar_em_arquivo(email, resultados)

    return resultados  # ← agora retorna pra salvar no relatório

def salvar_em_arquivo(email, resultados):
    pasta = "relatorios"
    os.makedirs(pasta, exist_ok=True)

    nome_arquivo = os.path.join(pasta, f"resultados_{email.replace('@', '_at_').replace('.', '_')}.txt")
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(f"Resultados de busca para: {email}\n\n")
        for item in resultados:
            f.write(item + "\n")

    console.print(f"\n[blue]Arquivo salvo como:[/blue] {nome_arquivo}")
