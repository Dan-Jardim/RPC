# RPC

Traballho de aula de **Sistemas Distribuidos** do Curso de graduação em Ciência da Computação da Universidade Federal Fluminense (UFF), lecionado pela Professora Flavia Coimbra Delicato.

Nesse projeto iremos implementar uma Chamada de Procedimento Remoto (do inglês, *Remote Procedure Call*, ou RPC) usando a biblioteca RPyC de Python, utilizando modelo orientado a serviços.

Os desenvolvedores:
- Daniel Azevedo Jardim
- Flávio Mateus Pereira Francisco 


## Execução

Antes de executar é preciso instalar a biblioteca rpyc:

`pip install rpyc`

Uma vez instalada, abra o terminal, va até a pasta do projeto e execute os comandos:
- Para o servidor: `python MyService.py`
- Para o cliente: `python Client.py localhost`
