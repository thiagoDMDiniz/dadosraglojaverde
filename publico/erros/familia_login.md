---
doc_id: "LV-PUB-COD-0008"
titulo: "Códigos de erro: Cadastro e login"
categoria: "codigos_de_erro"
acesso: "publico"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
familia: "login"
---

# Códigos de erro: Cadastro e login

Este catálogo reúne os códigos de erro que aparecem ao criar uma conta, entrar no aplicativo ou no site e manter a sessão ativa. Eles tratam de senha, bloqueios, e-mail, CPF, verificação por SMS, token, dispositivos e cadastro incompleto. Cada código tem quatro dígitos, e códigos parecidos podem ter causas diferentes. A Loja Verde nunca pede senha, token ou código de segurança por telefone, e-mail ou mensagem, então desconfie de qualquer contato que peça esses dados. Para ajuda, o SAC atende pelo 0800 700 0100, de segunda a sexta, das 8h às 20h, e aos sábados, das 8h às 14h.

A maior parte dos problemas de acesso tem solução simples e rápida. Em geral, basta conferir os dados digitados, atualizar o aplicativo e reconectar o aparelho à internet. Quando a mensagem aparece com frequência, vale observar em que momento ela surge, como ao trocar de rede Wi-Fi, depois de uma atualização ou ao usar a conta em outro aparelho. Essas informações ajudam a equipe de atendimento a entender o caso mais rapidamente. Guarde também o e-mail cadastrado e o telefone que recebe os códigos de verificação, pois eles são usados em quase todas as etapas de recuperação de acesso.

## ERR-2105: senha incorreta

O código ERR-2105 indica que a senha digitada não confere com a senha da conta. O erro é comum após trocas de senha feitas em outro aparelho ou quando a tecla de maiúsculas está ativada sem perceber.

**O que fazer:**

1. Confira se a tecla de maiúsculas está desligada e digite a senha com calma.
2. Se não lembrar a senha, use a opção de recuperação pelo e-mail cadastrado.
3. Evite tentativas repetidas, pois elas podem levar ao bloqueio temporário da conta.

## ERR-2114: conta bloqueada por tentativas excessivas

O código ERR-2114 indica que a conta foi bloqueada temporariamente depois de várias tentativas de acesso sem sucesso. O bloqueio é uma proteção contra acessos indevidos e é removido automaticamente depois de um período.

**O que fazer:**

1. Aguarde o tempo indicado na tela antes de tentar novamente.
2. Recupere a senha pelo e-mail cadastrado, depois que o bloqueio terminar.
3. Procure o SAC se a conta continuar bloqueada sem que você tenha tentado acessá-la.

## ERR-2117: e-mail já cadastrado

O código ERR-2117 indica que o e-mail informado no cadastro já pertence a outra conta da Loja Verde. Cada e-mail pode ser usado em apenas uma conta, o que simplifica o histórico de pedidos.

**O que fazer:**

1. Tente entrar com esse e-mail, caso a conta seja sua.
2. Recupere a senha se não lembrar o acesso.
3. Use outro e-mail para criar uma nova conta, se a existente não for sua.

## ERR-2118: CPF inválido

O código ERR-2118 indica que o CPF informado não passou na validação. A checagem confere a quantidade de dígitos e os dígitos verificadores, e um número digitado errado já gera o erro.

**O que fazer:**

1. Confira o CPF no documento e digite somente os números.
2. Verifique se o campo não contém espaços ou pontos extras.
3. Procure o SAC se o CPF estiver correto e o cadastro continuar recusado.

## ERR-2130: SMS de verificação não entregue

O código ERR-2130 indica que a mensagem com o código de verificação não chegou ao telefone cadastrado. A falha pode ocorrer por sinal fraco, número incorreto ou bloqueio de mensagens pela operadora.

**O que fazer:**

1. Confira se o número de telefone está correto e com DDD.
2. Solicite o reenvio do código depois de alguns instantes.
3. Se a mensagem continuar sem chegar, procure o SAC para validar o contato por outro canal.

## ERR-2139: token de acesso expirado

O código ERR-2139 indica que o token de acesso da sessão expirou. Por segurança, o token tem validade limitada, e a renovação exige um novo login.

**O que fazer:**

1. Saia da conta e entre novamente com o seu e-mail e senha.
2. Atualize o aplicativo se a mensagem aparecer com frequência.
3. Procure o SAC se o problema se repetir logo após o login.

## ERR-2140: dispositivo não reconhecido

O código ERR-2140 indica que a conta está sendo acessada por um aparelho que ainda não foi reconhecido. Essa verificação ajuda a proteger a conta quando há um novo acesso.

**O que fazer:**

1. Confirme o acesso pelo código enviado ao seu contato cadastrado.
2. Se o aparelho for seu, marque-o como reconhecido ao confirmar o acesso.
3. Se não reconhecer o acesso, troque a senha e procure o SAC.

## ERR-2171: cadastro incompleto

O código ERR-2171 indica que o cadastro não tem todas as informações obrigatórias para concluir o acesso. Campos como nome completo, CPF, endereço e telefone precisam estar preenchidos.

**O que fazer:**

1. Abra Meus Dados e verifique os campos marcados como pendentes.
2. Preencha as informações obrigatórias com os dados corretos.
3. Salve o cadastro e tente acessar a conta novamente.

## ERR-2186: sessão expirada

O código ERR-2186 indica que a sessão ficou inativa por tempo suficiente para ser encerrada. Esse encerramento acontece por segurança, principalmente em aparelhos compartilhados.

**O que fazer:**

1. Entre novamente na conta com seu e-mail e senha.
2. Evite deixar a conta aberta em aparelhos de uso público.
3. Refaça o carrinho, caso ele não tenha sido salvo após a sessão.

## ERR-2195: conta pendente de verificação

O código ERR-2195 indica que a conta foi criada, mas ainda não teve o e-mail ou o telefone verificado. Sem essa verificação, algumas funções ficam indisponíveis.

**O que fazer:**

1. Procure no e-mail a mensagem de confirmação da conta, inclusive na caixa de spam.
2. Solicite o reenvio do código, se a mensagem não chegar.
3. Conclua a verificação e entre novamente na conta.
