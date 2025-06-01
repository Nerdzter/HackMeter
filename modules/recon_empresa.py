from duckduckgo_search import DDGS
from rich.console import Console
from rich.table import Table
import requests
import time

console = Console()

def buscar_empresa(nome=None, site=None, cnpj=None):
    console.print("\n[bold yellow]Iniciando busca da empresa...[/bold yellow]\n")

    resultados_final = []

    if cnpj:
        data = consultar_cnpj(cnpj)
        if data:
            for campo in ["nome", "fantasia", "abertura", "situacao", "tipo", "uf", "municipio", "telefone", "email"]:
                resultados_final.append(f"{campo.capitalize()}: {data.get(campo, 'N/A')}")

    if nome or site:
        links = buscar_online(nome or site)
        if links:
            resultados_final.extend([f"{titulo} → {url}" for titulo, url in links])

    return resultados_final

def consultar_cnpj(cnpj):
    try:
        url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
        headers = {"User-Agent": "HackMeter Bot"}
        response = requests.get(url, headers=headers)
        data = response.json()

        if "status" in data and data["status"] == "ERROR":
            console.print(f"[red]Erro:[/red] {data['message']}")
            return None

        # (mantém a exibição na tela)
        # ...
        return data

    except Exception as e:
        console.print(f"[red]Erro ao consultar CNPJ:[/red] {e}")
        return None

def buscar_online(termo):
    console.print(f"\n[bold cyan]Buscando online por:[/bold cyan] {termo}")
    resultados = []

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(termo, max_results=5):
                resultados.append((r['title'], r['href']))
    except Exception as e:
        console.print(f"[red]Erro na busca DuckDuckGo:[/red] {e}")
        console.print("[yellow]Aguardando 10 segundos antes de continuar...[/yellow]")
        time.sleep(10)
        return []

    if resultados:
        # exibe na tela
        table = Table(title="🌐 Resultados Online")
        table.add_column("Título", style="cyan")
        table.add_column("Link", style="magenta")

        for titulo, link in resultados:
            table.add_row(titulo, link)
        console.print(table)

    return resultados
