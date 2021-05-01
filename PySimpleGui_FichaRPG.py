import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text("Nome"),sg.Input(key = "nome")],
            [sg.Text("Idade"),sg.Input(key = "Idade")],
            [sg.Text("Qual é a raça do seu personagem?")],
            [sg.Checkbox("Humano", key = "raça1"), sg.Checkbox("Orc", key = "raça2"), sg.Checkbox("Dragão", key = "raça3"), sg.Checkbox("Bretão", key = "raça4")],
            [sg.Text("Qual é a classe do seu personagem?")],
            [sg.Checkbox("Ladino", key = "classe1"), sg.Checkbox("Paladino", key = "classe2"), sg.Checkbox("Pyromancer", key = "classe3"), sg.Checkbox("necromante", key = "classe4"), sg.Checkbox("Guerreiro", key = "classe5")],
            [sg.Text("Escolha uma skill, ela será aprimorada em +10: ")],
            [sg.Checkbox("Inteligencia", key = "skill1"), sg.Checkbox("Agilidade", key = "skill2"), sg.Checkbox("Força", key = "skill3"), sg.Checkbox("Mana", key = "skill4"), sg.Checkbox("Vida", key = "skill5")],
            [sg.Button("Enviar ficha")],
            ]
        #janela
        Janela = sg.Window("Ficha RPG").layout(layout)
        #Extraindo Dados
        self.Button, self.values = Janela.Read()

    def Iniciar(self):
        nome = self.values["nome"]
        idade = self.values["Idade"]
        raca1 = self.values["raça1"]
        raca2 = self.values["raça2"]
        raca3 = self.values["raça3"]
        raca4 = self.values["raça4"]
        classe1 = self.values["classe1"]
        classe2 = self.values["classe2"]
        classe3 = self.values["classe3"]
        classe4 = self.values["classe4"]
        classe5 = self.values["classe5"]
        skill1 = self.values["skill1"]
        skill2 = self.values["skill2"]
        skill3 = self.values["skill3"]
        skill4 = self.values["skill4"]
        skill5 = self.values["skill5"]

        print(f'Nome: {nome}\n')

        print(f'Idade: {idade}\n')

        print("Raça Escolhida: ")
        if (raca1 == True and raca2 == False and raca3 == False and raca4 == False):
            print(f'Humano\n')
        elif (raca2 == True and raca1 == False and raca3 == False and raca4 == False):
            print(f'Orc\n')
        elif (raca3 == True and raca1 == False and raca2 == False and raca4 == False):
            print(f'Dragão\n')
        elif (raca4 == True and raca1 == False and raca2 == False and raca3 == False):
            print(f'Bretão\n')
        elif (raca1 == False and raca2 == False and raca3 == False and raca4 == False):
            print("O jogador não selecionou nenhuma raça \n")
        else:
            print("Multiplas raças não são aceitas, selecione novamente\n")

        print("Classe Escolhida: ")
        if (classe1 == True and classe2 == False and classe3 == False and classe4 == False and classe5 == False):
            print(f'Ladino\n')
        elif (classe2 == True and classe1 == False and classe3 == False and classe4 == False and classe5 == False):
            print(f'Paladino\n')
        elif (classe3 == True and classe1 == False and classe2 == False and classe4 == False and classe5 == False):
            print(f'Pyromancer\n')
        elif (classe4 == True and classe1 == False and classe2 == False and classe3 == False and classe5 == False):
            print(f'Necromante\n')
        elif (classe5 == True and classe1 == False and classe2 == False and classe3 == False and classe4 == False):
            print(f'Guerreiro\n')
        elif (classe1 == False and classe2 == False and classe3 == False and classe4 == False and classe5 == False):
            print("O jogador não selecionou nenhuma classe \n")
        else:
            print("Multiplas classes não são aceitas, selecione novamente\n")

        print("Skill Aprimorada em +10: ")
        if (skill1 == True and skill2 == False and skill3 == False and skill4 == False and skill5 == False):
            print(f'Inteligencia\n')
        elif (skill2 == True and skill1 == False and skill3 == False and skill4 == False and skill5 == False):
            print(f'Agilidade\n')
        elif (skill3 == True and skill1 == False and skill2 == False and skill4 == False and skill5 == False):
            print(f'Força\n')
        elif (skill4 == True and skill1 == False and skill2 == False and skill3 == False and skill5 == False):
            print(f'Mana\n')
        elif (skill5 == True and skill1 == False and skill2 == False and skill3 == False and skill4 == False):
            print(f'Vida\n')
        elif (skill1 == False and skill2 == False and skill3 == False and skill4 == False and skill5 == False):
            print("O jogador não selecionou nenhuma Skill para Aprimorar \n")
        else:
            print("Multiplas Skills não são aceitas, selecione novamente\n")

tela = TelaPython()
tela.Iniciar()