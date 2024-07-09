from .admin import *
from .models import *

def gerar_perguntas_html(perguntas):
    html = []
    contador = 0
    for i in list(perguntas):
        pergunta = str(i['pergunta']).split("--")
        pergunta_titulo = i['pergunta_index']
        a,b,c,d =  pergunta[1], pergunta[2], pergunta[3], pergunta[4]

        html.append(f'''
            <div class="question-block">
                <p class="question-text">{pergunta_titulo}</p><br>
                <div><input type="radio" id="q{pergunta_titulo}0" name="q{contador}" value="A"><label for="q{pergunta_titulo}0">{a}</label></div>
                <div><input type="radio" id="q{pergunta_titulo}1" name="q{contador}" value="B"><label for="q{pergunta_titulo}1"> {b}</label></div>
                <div><input type="radio" id="q{pergunta_titulo}2" name="q{contador}" value="C"><label for="q{pergunta_titulo}2">{c}</label></div>
                <div><input type="radio" id="q{pergunta_titulo}3" name="q{contador}" value="D"><label for="q{pergunta_titulo}3">{d}</label></div>
           </div>
            '''
        )
        contador += 1
    return html
    
    
def gerar_nota_aluno(respostas,email):
    nota = 0
    for resposta in list(respostas['questions']):
        gabarito = buscar_resposta(resposta['question'])
        gabarito_resp = list(gabarito)[0]['resposta']
        if str(resposta['answer']).upper() == str(gabarito_resp).upper():
            nota += 1
    if nota >= 5:
        try:
            usuario = Usuario.objects.get(email=email)
            certificado = Certificado(id_usuario_certificado=usuario, tipo='Aluno')
            certificado.save()
            print(f'Certificado de tipo Aluno criado para o usuário {email}.')
        
        except Usuario.DoesNotExist:
            print(f'Usuário com o e-mail {email} não encontrado.')
    print('nota:', nota)

    
# texto = """
# O que é 2FA? --A) Uma senha que é usada duas vezes. --B) Um sistema de backup automático. --C) Autenticação de dois fatores.--D) Um tipo de firewall.
# """    
    
    

# print(gerar_perguntas_html([texto]))