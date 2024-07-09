a = {'questions': [{'question': 'O que devemos fazer ao receber um e-mail solicitando nossas senhas ou dados pessoais?\n\n', 'answer': 'C'}, {'question': 'Qual das seguintes opções é uma boa prática para criar uma senha forte?\n\n', 'answer': 'C'}, {'question': 'Qual é uma boa prática em relação ao compartilhamento de senhas?\n\n', 'answer': 'B'}, {'question': 'O que é 2FA?\n\n', 'answer': 'A'}, {'question': 'Por que devemos evitar usar redes Wi-Fi públicas para acessar nossos dispositivos?\n\n', 'answer': 'B'}]}


for i in a['questions']:
    print(i['question'])
    print(i['answer'])