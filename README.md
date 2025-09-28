# rabbitmq1
Ambiente Rabbitmq que o "produtor" envia a mensagem hello world para o "Destinatário"

Nesse trabalho possui um ambiente que um "remetente" envia a mensagem hello world para um
"destinatário" em python. Esse é um ambiente básico da aplicação Rabbitmq que consiste em um message broker
de código aberto que implementa o protocolo AMQP que facilita a comunicação assíncrona entre
as aplicações e serviços, tal ambiente possui arquivos que foram feitos atráves da seção do site
oficial do Rabbitmq chamada "Hello World" onde possui os códigos básicos para envio de mensagem de um "produtor"
e um "destinatário". Para que ocorresse a troca de mensagem foi-se necessário 
a criação de um ambiente a partir do Conda que é um sistema de gerenciamentode pacotes de código aberto, 
um compilador em que pode-se utilizar o python, e um computador que aguente o ambiente. 
Sobre o processo foi necessário a instalação do conda e do rabbit no desktop, após instalação foi feita a criação do ambiente
conda em um prompt de comando depois foi criado dois arquivos: producer.py e receiver.py. 
Onde o arquivo producer basicamente é o arquivo que vai enviar a mensagem 
e o receiver é o que vai recebe-la, após a finalização de cada arquivo foi criado mais um ambiente em outro prompt
um deles fará o papel de enviar e o outro de receber a mensagem, para isso utilizei o comando pra executar um arquivo
em cada ambiente e o resultado esperado é que o ambiente em que seja executado o arquivo receiver receba a mensagem
Hello World do producer.  
