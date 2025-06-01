from duckduckgo_search import DDGS
from rich.console import Console
from rich.table import Table
import time

console = Console()

def buscar_social(nome=None, instagram=None, facebook=None):
    console.print(f"\n[bold green]Buscando perfis sociais...[/bold green]")

    termos = []
    if nome:
        termos.append(nome)
    if instagram:
        termos.append(f"site:instagram.com {instagram}")
    if facebook:
        termos.append(f"site:facebook.com {facebook}")

    resultados = []

    try:
        with DDGS() as ddgs:
            for termo in termos:
                console.print(f"[yellow]🔍 Procurando por:[/yellow] {termo}")
                for r in ddgs.text(termo, max_results=5):
                    resultados.append((r['title'], r['href']))
    except Exception as e:
        console.print(f"[red]Erro na busca DuckDuckGo:[/red] {e}")
        console.print("[yellow]Aguardando 10 segundos antes de continuar...[/yellow]")
        time.sleep(10)
        return []

    if resultados:
        table = Table(title="Resultados de Perfis Sociais")
        table.add_column("Título", style="cyan")
        table.add_column("Link", style="magenta")

        for titulo, link in resultados:
            table.add_row(titulo, link)

        console.print(table)
    else:
        console.print("[red]Nenhum perfil relevante encontrado.[/red]")

    # Transforma em string formatada para salvar
    return [f"{titulo} → {link}" for titulo, link in resultados]
