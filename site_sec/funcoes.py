def gerar_perguntas_html(perguntas):
    pergunta = perguntas.split("--")
    pergunta_titulo = pergunta[0]
    a,b,c,d =  pergunta[1], pergunta[2], pergunta[3], pergunta[4]

    html = f'<p>{pergunta_titulo}</p><br>'
    html += f'<div><input type="radio" id="q{pergunta_titulo}0" name="q{pergunta_titulo}" value="A"><label for="q{pergunta_titulo}0">{a}</label></div>'
    html += f'<div><input type="radio" id="q{pergunta_titulo}1" name="q{pergunta_titulo}" value="B"><label for="q{pergunta_titulo}1"> {b}</label></div>'
    html += f'<div><input type="radio" id="q{pergunta_titulo}2" name="q{pergunta_titulo}" value="C"><label for="q{pergunta_titulo}2">{c}</label></div>'
    html += f'<div><input type="radio" id="q{pergunta_titulo}3" name="q{pergunta_titulo}" value="D"><label for="q{pergunta_titulo}3">{d}</label></div>'

    return html
    
    
    
texto = """
O que é 2FA? --A) Uma senha que é usada duas vezes. --B) Um sistema de backup automático. --C) Autenticação de dois fatores.--D) Um tipo de firewall.
"""    
    
    

print(gerar_perguntas_html(texto))