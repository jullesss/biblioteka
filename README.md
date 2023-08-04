# Bem-vinde ao projeto Biblioteka API!

## Introdução

<p> Este projeto tem como objetivo desenvolver uma aplicação (API) para a gestão de uma biblioteca, 
  proporcionando funcionalidades tanto para estudantes quanto para pessoas colaboradoras da mesma. </p>

## Funcionalidades

### Usuários

- A aplicação permite o cadastro de dois tipos de pessoas usuárias: Estudante e Pessoa Colaboradora da biblioteca.
- Estudantes têm acesso a funcionalidades como vizualizar as informações da própria conta, atualiza-las, verificar o próprio histórico de livros emprestados, obter informações sobre livros (como título, autor, número de páginas, ano de publicação, imagem e descrição do livro) e favoritar livros para receber notificações por e-mail e desfavoritar. É possível buscar a lista completa de livros cadastrados, bem como buscar por um livro específico através do ID.
- Colaboradories têm acesso a funcionalidades adicionais como criar contas para estudantes ou demais colaboradories, realizar empréstimos para estudantes, realizar devoluções de exemplares, cadastrar novos livros, cadastrar novas cópias de um livro, verificar o histórico de empréstimos de cada estudante e acessar informações sobre cada estudante.

### Acesso Público

- Pessoas sem conta também podem acessar a plataforma para visualizar informações sobre os livros, como disponibilidade, título, etc.

### Empréstimo de Livros

- Cada livro (exemplar) pode ser emprestado por um período de 3 dias úteis (desconsiderando, portanto, fins de semana e feriados brasileiros).

### Devolução de Livros

- Todos os livros (exemplares) emprestados devem ser devolvidos até a data estipulada.
- Se a pessoa estudante não devolver o livro até o prazo determinado, será bloqueada e não poderá solicitar novos empréstimos.

## Instalação e Execução

Para executar a aplicação localmente, siga estas etapas:

1. Clone este repositório.
2. Instale as dependências necessárias usando o gerenciador de pacotes de sua preferência.
3. Configure as credenciais de acesso no arquivo `.env`.
4. Execute o comando de inicialização da aplicação.
5. Se desejar, utilize o nosso workspace do Insomnia para testes. Ele se encontra em nosso repositório, basta importar.

Além disso, você também pode explorar a aplicação através do seguinte link de deploy: [Link de Deploy](https://biblioteka-g13-production.up.railway.app/api/docs/).

## Sobre a criação de contas

É necessário criar antes de tudo um Super User. Abra a shell e insira:
python manage.py createsuperuser
Preencha todos os campos requisitados e após isso você pode fazer o login dessa conta via Insomnia, por exemplo, e criar outras contas (admins ou não).

## Contato

Este projeto foi desenvolvido por uma equipe apaixonada por tecnologia. Se você tiver alguma dúvida, sugestão ou feedback em relação a este projeto, sinta-se à vontade para entrar em contato conosco:

- Suene Queiroz Fuzzo: [suenequeiroz@hotmail.com]
- Claudineir Neto: [devneto576@gmail.com]
- Jorge Sousa: [abel.jorge3@outlook.com]
- Julles Kuhn [https://www.linkedin.com/in/julleskuhn/]

Agradecemos por utilizar a Biblioteka! ✨
