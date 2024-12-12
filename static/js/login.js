function loginSubmit(event) {
    event.preventDefault();  // Impede o envio do formulário para evitar o comportamento padrão.
  
    // Aqui você pode adicionar a lógica para verificar o login (por exemplo, validação de e-mail e senha).
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
  
    // Exemplo simples de verificação (pode ser adaptado para algo mais seguro).
    if (email === "josias@exemplo.com" && senha === "12345") {
      // Redireciona para a página da Área do Candidato após o login bem-sucedido.
      window.location.href = "area-candidato.html";
    } else {
      alert("Credenciais inválidas! Tente novamente.");
    }
  }
  