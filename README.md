# biblioteka-g13

# Bem-vindo(a) ao projeto BiblioteKa! 

## Introdução
<p> Este projeto tem como objetivo desenvolver uma aplicação para a gestão de uma biblioteca, 
  proporcionando funcionalidades tanto para estudantes quanto para colaboradores da mesma. </p>

## Funcionalidades

### Usuários
- A aplicação permite o cadastro de dois tipos de usuários: Estudante e Colaborador da biblioteca.
- Estudantes têm acesso a funcionalidades como verificar o próprio histórico de livros emprestados, obter informações sobre livros (como título, autor, número de páginas, ano de publicação, imagem e descrição do livro ) e seguir livros para receber notificações por e-mail.  É possível buscar uma lista completa de livros cadastrados, bem como buscar por um livro específico através do ID.
- Colaboradores têm acesso a funcionalidades adicionais como realizar empréstimos, cadastrar novos livros, verificar o histórico de empréstimos de cada estudante e verificar o status de um estudante (se está bloqueado ou não).

### Acesso Público
- Usuários não autenticados também podem acessar a plataforma para visualizar informações sobre os livros, como disponibilidade, título, etc.
  
### Empréstimo de Livros
- Cada livro pode ser emprestado por um período fixo de tempo.
- Implementamos uma lógica que permite a modificação da data de retorno caso ela caia em um fim de semana (sábado ou domingo). A nova data de retorno será o próximo dia útil.

### Devolução de Livros
- Todos os livros emprestados devem ser devolvidos até a data estipulada.
- Se um estudante não devolver o livro até o prazo determinado, ele será bloqueado e não poderá solicitar novos empréstimos.


## Instalação e Execução
Para executar a aplicação localmente, siga estas etapas:

1. Clone este repositório.
2. Instale as dependências necessárias usando o gerenciador de pacotes de sua preferência.
3. Configure as credenciais de acesso no arquivo `.env`.
4. Execute o comando de inicialização da aplicação.
5. Acesse a aplicação no seu navegador através do endereço fornecido.

Além disso, você também pode explorar a aplicação através do seguinte link de deploy: [Link de Deploy](https://).


## Contato
Este projeto foi desenvolvido por uma equipe apaixonada por tecnologia. Se você tiver alguma dúvida, sugestão ou feedback em relação a este projeto, sinta-se à vontade para entrar em contato conosco por e-mail:
- Suene Queiroz Fuzzo: [suenequeiroz@hotmail.com]
- Julles Kuhn: [kuhnnhuk@outlook.com]
- Claudineir Neto: [devneto576@gmail.com]
- Jorge Sousa: [abel.jorge3@outlook.com]

Agradecemos por utilizar a Biblioteka! ✨

  
  
