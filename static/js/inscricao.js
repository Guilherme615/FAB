// Script para exibir o modal após a inscrição
document.getElementById('inscricaoForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário para não recarregar a página

    // Exibe o modal de confirmação
    var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
    confirmationModal.show();

    // Após o clique no botão de confirmação, redireciona o usuário para a área do candidato
    document.getElementById('redirectButton').addEventListener('click', function() {
        // Substitua 'area_do_candidato.html' pela URL real da área do candidato
        window.location.href = 'login.html';
    });
});
