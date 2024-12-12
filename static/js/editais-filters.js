  // Elementos do DOM
  const searchTitle = document.getElementById('searchTitle');
  const filterArea = document.getElementById('filterArea');
  const filterDate = document.getElementById('filterDate');
  const searchButton = document.getElementById('searchButton');
  const resetButton = document.getElementById('resetButton');
  
  // Modal
  const resultsModal = new bootstrap.Modal(document.getElementById('resultsModal'));
  const modalMessage = document.getElementById('modalMessage');
  const resultList = document.getElementById('resultList');

  // Função para buscar editais
  function searchEditals() {
    const title = searchTitle.value.trim();
    const area = filterArea.value;
    const date = filterDate.value;

    // Simulação de busca: você pode substituir por dados reais
    const sampleData = [
      { id: 1, title: 'Edital de Convocação - Saúde', date: '2024-11-15', area: 'saude' },
      { id: 2, title: 'Edital de Convocação - Tecnologia', date: '2024-11-10', area: 'tecnologia' }
    ];

    const filteredData = sampleData.filter(edital => {
      const matchTitle = title ? edital.title.toLowerCase().includes(title.toLowerCase()) : true;
      const matchArea = area ? edital.area === area : true;
      const matchDate = date ? edital.date === date : true;
      return matchTitle && matchArea && matchDate;
    });

    // Exibir resultados no modal
    if (filteredData.length > 0) {
      modalMessage.classList.add('d-none');
      resultList.classList.remove('d-none');
      resultList.innerHTML = ''; // Limpa resultados anteriores
      filteredData.forEach(edital => {
        const listItem = document.createElement('li');
        listItem.className = 'list-group-item';
        listItem.textContent = `#${edital.id} - ${edital.title} (${edital.date})`;
        resultList.appendChild(listItem);
      });
    } else {
      modalMessage.textContent = 'Nenhum edital encontrado para os filtros aplicados.';
      modalMessage.classList.remove('d-none');
      resultList.classList.add('d-none');
    }

    // Abre o modal
    resultsModal.show();
  }

  // Função para resetar filtros
  function resetFilters() {
    searchTitle.value = '';
    filterArea.value = '';
    filterDate.value = '';

    // Feedback no console ou outras ações desejadas
    console.log('Filtros resetados!');
  }

  // Eventos
  searchButton.addEventListener('click', searchEditals);
  resetButton.addEventListener('click', resetFilters);

  // Também adiciona busca ao pressionar "Enter" no campo de título
  searchTitle.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
      searchEditals();
    }
  });
