from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('DarkPurple4')
layout = [
#Linha 1 Visor
    [sg.Input('0',size=(30,1),justification='right',key='Result')],
#Linha 2 Tag do grupo
    [sg.Text('Calc. by Hackers Inc. © 2021')],
#Linha 3
    [sg.Button('C', size=(5,1),key='LIMPAR'),
     sg.Button('ˣ√',size=(5,1),key='SQRT'),
     sg.Button('xˣ',size=(5,1),key='POW'),
     sg.Button('÷',size=(5,1),key='DIVI')],
#Linha 4
    [sg.Button('7',size=(5,1),key='SETE'),
     sg.Button('8',size=(5,1),key='OITO'),
     sg.Button('9',size=(5,1),key='NOVE'),
     sg.Button('×',size=(5,1),key='MULT')],
#Linha 5
    [sg.Button('4',size=(5,1),key='QUATRO'),
     sg.Button('5',size=(5,1),key='CINCO'),
     sg.Button('6',size=(5,1),key='SEIS'),
     sg.Button('-',size=(5,1),key='MENOS')],
#Linha 6
    [sg.Button('1',size=(5,1),key='UM'),
     sg.Button('2',size=(5,1),key='DOIS'),
     sg.Button('3',size=(5,1),key='TRES'),
     sg.Button('+',size=(5,1),key='PLUS')],
#Linha 7
    [sg.Button('00',size=(5,1),key='CEM'),
     sg.Button('0',size=(5,1),key='ZERO'),
     sg.Button('=',size=(13,1),key='EQUAL')],
]

#Janela
class App():
    def __init__(self):
        self.window = sg.Window(
            'Calculadora', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=False
        )
        self.result = 0
        self.oper = ''
        self.window.read(timeout=1)
        for i in range(0, 7):
            for button in layout[i]:
                button.expand(expand_x=True, expand_y=True)

#Operações
    def resultados(self):
        global resultado
        if self.oper == '+':
            resultado = float(self.result) + float(self.valores['Result'])
        if self.oper == '-':
            resultado = float(self.result) - float(self.valores['Result'])
        if self.oper == '/':
            resultado = float(self.result) / float(self.valores['Result'])
        if self.oper == '*':
            resultado = float(self.result) * float(self.valores['Result'])
        if self.oper == '^':
            resultado = float(self.result) ** (float(self.valores['Result']))
        if self.oper == '√':
            resultado = float(self.result) ** (1 / (float(self.valores['Result'])))
        print(resultado)
        return resultado

#Manter rodando
    def start(self):
        while True:
            evento, self.valores = self.window.read()

            if evento in (None, sg.WINDOW_CLOSED): #Pra fechar o programa
                break
#Números no Visor
            if evento == 'UM':
                print(1)
                if self.valores['Result'] == '0':
                    self.window['Result'].update(value='1')
                else:
                    self.window['Result'].update(value=self.valores['Result'] + '1')

            if evento == 'DOIS':
                print(2)
                if self.valores['Result'] == '0':
                    self.window['Result'].update(value='2')
                else:
                    self.window['Result'].update(value=self.valores['Result'] + '2')

            if evento == 'TRES':
                print(3)
                if self.valores['Result'] == '0':
                    self.window['Result'].update(value='3')
                else:
                    self.window['Result'].update(value=self.valores['Result'] + '3')

            if evento == 'QUATRO':
                print(4)
                if self.valores['Result'] == '0':
                    self.window['Result'].update(value='4')
                else:
                    self.window['Result'].update(value=self.valores['Result'] + '4')

            if evento == 'CINCO':
                print(5)
                if self.valores['Result'] == '0':
                    self.window['Result'].update(value='5')
                else:
                    self.window['Result'].update(value=self.valores['Result'] + '5')

            if evento == 'SEIS':
                print(6)
                if self.valores['Result'] == '0':
                    self.window['Result'].update(value='6')
                else:
                    self.window['Result'].update(value=self.valores['Result'] + '6')

            if evento == 'SETE':
                print(7)
                if self.valores['Result'] == '0':
                    self.window['Result'].update(value='7')
                else:
                    self.window['Result'].update(value=self.valores['Result'] + '7')

            if evento == 'OITO':
                print(8)
                if self.valores['Result'] == '0':
                    self.window['Result'].update(value='8')
                else:
                    self.window['Result'].update(value=self.valores['Result'] + '8')

            if evento == 'NOVE':
                print(9)
                if self.valores['Result'] == '0':
                    self.window['Result'].update(value='9')
                else:
                    self.window['Result'].update(value=self.valores['Result'] + '9')

            if evento == 'ZERO':
                print('0')
                if self.valores['Result'] == '0':
                    self.window['Result'].update(value='0')
                else:
                    self.window['Result'].update(value=self.valores['Result'] + '0')

            if evento == 'CEM':
                print('00')
                if self.valores['Result'] == '0':
                    self.window['Result'].update(value='00')
                else:
                    self.window['Result'].update(value=self.valores['Result'] + '00')

#Comando Clear
            if evento == 'LIMPAR':
                print('C')
                self.result = 0
                self.window['Result'].update(value=self.result)

#Operações + - * / √ x²
            #SOMA
            if evento == 'PLUS':
                print('+')
                if self.oper != '':
                    self.result = self.resultados()
                else:
                    self.oper = '+'
                    self.result = self.valores['Result']
                self.window['Result'].update(value='')

            #SUBTRAÇÃO
            if evento == 'MENOS':
                print('-')
                if self.oper != '':
                    self.result = self.resultados()
                else:
                    self.oper = '-'
                    self.result = self.valores['Result']
                self.window['Result'].update(value='')

            #MULTIPLICAÇÃO
            if evento == 'MULT':
                print('×')
                if self.oper != '':
                    self.result = self.resultados()
                else:
                    self.oper = '*'
                    self.result = self.valores['Result']
                self.window['Result'].update(value='')

            #DIVISÃO
            if evento == 'DIVI':
                print('÷')
                if self.oper != '':
                    self.result = self.resultados()
                else:
                    self.oper = '/'
                    self.result = self.valores['Result']
                self.window['Result'].update(value='')

            #POTENCIAÇÃO
            if evento == 'POW':
                print('^')
                if self.oper != '':
                    self.result = self.resultados()
                else:
                    self.oper = '^'
                    self.result = self.valores['Result']
                self.window['Result'].update(value='')

            #RAIZ_QUADRADA
            if evento == 'SQRT':
                print('√')
                if self.oper != '':
                    self.result = self.resultados()
                else:
                    self.oper = '√'
                    self.result = self.valores['Result']
                self.window['Result'].update(value='')

            #Botão de igualdade
            if evento == 'EQUAL':
                print('=')
                self.result = self.resultados()
                self.window['Result'].update(value=self.result)
                self.result = 0
                self.oper = ''

App().start()
