// Caminho do arquivo PDF
const pdfPath = '/assets/docs/modeloeditalfab.pdf';

// Função de visualizar PDF
function visualizarPDF() {
  window.open(pdfPath, '_blank');  // Abre o PDF em uma nova aba
}

// Função de download do PDF
function downloadPDF() {
  const link = document.createElement('a');
  link.href = pdfPath;
  link.download = 'modeloeditalfab.pdf'; // Nome do arquivo para o download
  link.click();
}

// Event Listeners para os botões de visualização e download
document.getElementById('visualizarBtn1').addEventListener('click', visualizarPDF);
document.getElementById('downloadBtn1').addEventListener('click', downloadPDF);

document.getElementById('visualizarBtn2').addEventListener('click', visualizarPDF);
document.getElementById('downloadBtn2').addEventListener('click', downloadPDF);
