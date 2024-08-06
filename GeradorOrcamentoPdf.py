import fpdf
import os

class GeradorOrcamento():

    #Construtor
    def __init__(self):
        self.nome_projeto = input('Digite a descrição do projeto: ')
        self.horas_previstas = int(input('Digite a quantidade de horas previstas: '))
        self.valor_hora_trabalhadas = int(input('Digite o valor da hora trabalhada: '))
        self.prazo_estimado_do_projeto = input('Digite o prazo estimado: ')
        self.valor_do_projeto = self.horas_previstas * self.valor_hora_trabalhadas
        self.texto = 'Orçamento gerado com sucesso !'
        self.pdf  = fpdf.FPDF()
        self.template = r'C:/Users/plati/OneDrive/Área de Trabalho/GeradorOrcamento/template.png'
        self.x = 115
        self.y = [145,160,175,190,205]
            
    #Método

    #Função para limpar tela:
    def limpar_console(self):
        """Limpa a tela do console, adaptando-se ao sistema operacional."""
        os.system('cls' if os.name == 'nt' else 'clear')

    #Método para pegar entrada do usuario e imprir no console:
    def gerarOrcamento(self):
        self.limpar_console()
        return f'{self.texto}\nValor do Orcamento R${self.valor_do_projeto:,.2f}'

    # Método gerador em pdf:
    def gerarPdf(self):
        try:
            self.pdf
            self.pdf.add_page()
            self.pdf.set_font('Arial')
            self.pdf.image(self.template,x=0,y=0)
            self.pdf.text(self.x,self.y[0],self.nome_projeto)
            self.pdf.text(self.x,self.y[1],str(self.horas_previstas))
            self.pdf.text(self.x,self.y[2],str(self.valor_hora_trabalhadas))
            self.pdf.text(self.x,self.y[3],self.prazo_estimado_do_projeto)
            self.pdf.text(self.x,self.y[4],str(self.valor_do_projeto))
            self.pdf.output('orcamento.pdf')  # Especificar o nome do arquivo
            print('Pdf gerado com sucesso !')
        except:
            print('Erro ao gerar PDF !')

    
