from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_usuario import Controller_Usuario
from controller.controller_perfil import Controller_Perfil
from controller.controller_agenda import Controller_Agenda


tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_usuario = Controller_Usuario()
ctrl_perfil = Controller_Perfil()
ctrl_agenda = Controller_Agenda()


def reports(opcao_relatorio: int = 0):
   
    if opcao_relatorio == 1:
        relatorio.get_relatorio_usuario()
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_perfils_usado()
    elif opcao_relatorio == 3:
        relatorio.get_relator1io_perfil()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_agenda()


def inserir(opcao_inserir: int = 0):

    if opcao_inserir == 1:
        novo_usuario = ctrl_usuario.inserir_usuario()
    elif opcao_inserir == 2:
        novo_perfil = ctrl_perfil.inserir_perfil()
    elif opcao_inserir == 3:
        novo_agenda = ctrl_agenda.inserir_agenda()


def atualizar(opcao_atualizar: int = 0):

    if opcao_atualizar == 1:
        usuario_atualizado = ctrl_usuario.atualizar_usuario()
    elif opcao_atualizar == 2:
        perfil_atualizado = ctrl_perfil.atualizar_perfil()


def excluir(opcao_excluir: int = 0):
    
    if opcao_excluir == 1:
        ctrl_usuario.excluir_usuario()
    elif opcao_excluir == 2:   
        ctrl_perfil.excluir_perfil()
    elif opcao_excluir == 3:
        ctrl_agenda.excluir_agenda()


def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)

        if opcao == 1:  # Relatórios

            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-3]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2:  # Inserir Novos Registros

            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [0-3]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3:  # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-3]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)


if __name__ == "__main__":
    run()
