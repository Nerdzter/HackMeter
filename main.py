import os
import time
from pyfiglet import Figlet
from rich.console import Console
from rich.prompt import Prompt

from modules.recon_email import verificar_email
from modules.recon_social import buscar_social
from modules.recon_empresa import buscar_empresa
from modules.generate_report import salvar_relatorio

console = Console()
figlet = Figlet(font='slant')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_banner():
    clear_screen()
    banner = figlet.renderText('HackMeter')
    console.print(banner, style="bold green")
    console.print("Versão: 1.0 - Investigador Digital\n", style="bold white")
    console.print("Autor: Nayderson Silva\n", style="italic blue")
    console.print("-" * 50)


def main_menu():
    console.print("\n[bold cyan]Menu Principal:[/bold cyan]")
    console.print("[1] Investigar Pessoa")
    console.print("[2] Investigar Empresa")
    console.print("[0] Sair")

    escolha = Prompt.ask("\nEscolha uma opção", choices=["1", "2", "0"])
    return escolha


def coletar_dados(tipo):
    console.print(f"\n[bold yellow]Investigação de {tipo} iniciada...[/bold yellow]\n")
    dados = {}
    resultados = []

    if tipo == "Pessoa":
        dados['nome'] = input("Nome completo (ou parcial): ")
        dados['email'] = input("E-mail (opcional): ")
        dados['telefone'] = input("Telefone (opcional): ")
        dados['instagram'] = input("Instagram (opcional): ")
        dados['facebook'] = input("Facebook (opcional): ")

        if dados['email']:
            email_resultados = verificar_email(dados['email'])
            resultados.extend(email_resultados)

        social_resultados = buscar_social(
            nome=dados.get('nome'),
            instagram=dados.get('instagram'),
            facebook=dados.get('facebook')
        )
        resultados.extend(social_resultados)

    else:
        dados['empresa'] = input("Nome da empresa: ")
        dados['site'] = input("Website oficial (opcional): ")
        dados['cnpj'] = input("CNPJ (opcional): ")

        empresa_resultados = buscar_empresa(
            nome=dados.get("empresa"),
            site=dados.get("site"),
            cnpj=dados.get("cnpj")
        )
        resultados.extend(empresa_resultados)

    console.print("\n[green]Análise concluída.[/green]")

    salvar = input("\nDeseja salvar este relatório? (S/N): ").strip().lower()
    if salvar == "s":
        nome_arquivo = input("Digite o nome do relatório (sem espaços): ").strip()
        caminho = salvar_relatorio(tipo, nome_arquivo, dados, resultados)
        console.print(f"[bold green]Relatório salvo em:[/bold green] {caminho}")

    input("Pressione Enter para voltar ao menu...")


if __name__ == "__main__":
    while True:
        show_banner()
        escolha = main_menu()

        if escolha == "1":
            coletar_dados("Pessoa")
        elif escolha == "2":
            coletar_dados("Empresa")
        elif escolha == "0":
            console.print("\n[red]Encerrando HackMeter. Até a próxima![/red]")
            break
