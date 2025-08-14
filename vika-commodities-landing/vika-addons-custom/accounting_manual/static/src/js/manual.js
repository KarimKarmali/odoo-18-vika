/* Manual de Contabilidade VIKA - JavaScript */

document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scrolling para links internos
    initSmoothScrolling();
    
    // Adicionar funcionalidades de busca
    initSearchFunctionality();
    
    // Adicionar botão de impressão
    initPrintButton();
    
    // Adicionar navegação por teclado
    initKeyboardNavigation();
    
    // Adicionar progress indicator
    initProgressIndicator();
    
    // Highlight de código
    initCodeHighlight();
    
    console.log('Manual de Contabilidade VIKA carregado com sucesso!');
});

/**
 * Inicializa scroll suave para links internos
 */
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Atualizar URL sem scroll jump
                history.pushState(null, null, `#${targetId}`);
            }
        });
    });
}

/**
 * Inicializa funcionalidade de busca no manual
 */
function initSearchFunctionality() {
    // Criar caixa de pesquisa
    const searchContainer = document.createElement('div');
    searchContainer.className = 'search-container mb-3';
    searchContainer.innerHTML = `
        <div class="input-group">
            <span class="input-group-text">
                <i class="fa fa-search"></i>
            </span>
            <input type="text" class="form-control" id="manual-search" 
                   placeholder="Pesquisar no manual..." autocomplete="off">
            <button class="btn btn-outline-secondary" type="button" id="clear-search">
                <i class="fa fa-times"></i>
            </button>
        </div>
        <div id="search-results" class="search-results mt-2"></div>
    `;
    
    // Inserir após o header
    const header = document.querySelector('.manual-header');
    if (header) {
        header.after(searchContainer);
        
        const searchInput = document.getElementById('manual-search');
        const clearButton = document.getElementById('clear-search');
        const resultsDiv = document.getElementById('search-results');
        
        // Event listener para pesquisa
        searchInput.addEventListener('input', debounce(function() {
            const query = this.value.trim().toLowerCase();
            if (query.length >= 2) {
                performSearch(query, resultsDiv);
            } else {
                resultsDiv.innerHTML = '';
            }
        }, 300));
        
        // Limpar pesquisa
        clearButton.addEventListener('click', function() {
            searchInput.value = '';
            resultsDiv.innerHTML = '';
            searchInput.focus();
        });
    }
}

/**
 * Realiza pesquisa no conteúdo do manual
 */
function performSearch(query, resultsDiv) {
    const content = document.querySelector('.manual-content');
    if (!content) return;
    
    const textNodes = getTextNodes(content);
    const results = [];
    
    textNodes.forEach(node => {
        const text = node.textContent.toLowerCase();
        if (text.includes(query)) {
            const heading = findNearestHeading(node);
            const context = getContextAroundMatch(node.textContent, query, 100);
            
            results.push({
                heading: heading ? heading.textContent : 'Sem título',
                context: context,
                element: heading || node.parentElement
            });
        }
    });
    
    displaySearchResults(results.slice(0, 10), resultsDiv, query); // Limitar a 10 resultados
}

/**
 * Exibe resultados da pesquisa
 */
function displaySearchResults(results, container, query) {
    if (results.length === 0) {
        container.innerHTML = `
            <div class="alert alert-info">
                <i class="fa fa-info-circle"></i> 
                Nenhum resultado encontrado para "${query}"
            </div>
        `;
        return;
    }
    
    const resultsHtml = results.map((result, index) => `
        <div class="search-result p-2 border-bottom" data-result="${index}">
            <h6 class="mb-1">${highlightText(result.heading, query)}</h6>
            <p class="mb-0 small text-muted">${highlightText(result.context, query)}</p>
        </div>
    `).join('');
    
    container.innerHTML = `
        <div class="search-results-container border rounded p-2 bg-light">
            <div class="small text-muted mb-2">
                <i class="fa fa-search"></i> ${results.length} resultado(s) encontrado(s)
            </div>
            ${resultsHtml}
        </div>
    `;
    
    // Adicionar click listeners aos resultados
    container.querySelectorAll('.search-result').forEach((result, index) => {
        result.addEventListener('click', function() {
            results[index].element.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
            container.innerHTML = ''; // Limpar resultados após clique
        });
        
        result.style.cursor = 'pointer';
        result.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#e9ecef';
        });
        result.addEventListener('mouseleave', function() {
            this.style.backgroundColor = 'transparent';
        });
    });
}

/**
 * Inicializa botão de impressão
 */
function initPrintButton() {
    const printButton = document.createElement('button');
    printButton.className = 'btn btn-outline-primary position-fixed';
    printButton.style.cssText = 'bottom: 20px; right: 20px; z-index: 1000; border-radius: 50px;';
    printButton.innerHTML = '<i class="fa fa-print"></i> Imprimir';
    printButton.title = 'Imprimir manual';
    
    printButton.addEventListener('click', function() {
        window.print();
    });
    
    document.body.appendChild(printButton);
}

/**
 * Inicializa navegação por teclado
 */
function initKeyboardNavigation() {
    document.addEventListener('keydown', function(e) {
        // Ctrl + F para focar na pesquisa
        if (e.ctrlKey && e.key === 'f') {
            e.preventDefault();
            const searchInput = document.getElementById('manual-search');
            if (searchInput) {
                searchInput.focus();
                searchInput.select();
            }
        }
        
        // Ctrl + P para imprimir
        if (e.ctrlKey && e.key === 'p') {
            // Deixar comportamento padrão do browser
        }
        
        // Escape para limpar pesquisa
        if (e.key === 'Escape') {
            const searchInput = document.getElementById('manual-search');
            const resultsDiv = document.getElementById('search-results');
            if (searchInput && searchInput === document.activeElement) {
                searchInput.value = '';
                if (resultsDiv) resultsDiv.innerHTML = '';
                searchInput.blur();
            }
        }
    });
}

/**
 * Inicializa indicador de progresso de leitura
 */
function initProgressIndicator() {
    const progressBar = document.createElement('div');
    progressBar.className = 'reading-progress';
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        z-index: 9999;
        transition: width 0.3s ease;
    `;
    
    document.body.appendChild(progressBar);
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.scrollY;
        const documentHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercentage = (scrollTop / documentHeight) * 100;
        
        progressBar.style.width = Math.min(scrollPercentage, 100) + '%';
    });
}

/**
 * Inicializa highlight de código
 */
function initCodeHighlight() {
    // Adicionar números de linha aos blocos de código
    const codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach(block => {
        const lines = block.textContent.split('\n');
        if (lines.length > 1) {
            const numberedLines = lines.map((line, index) => {
                if (index === lines.length - 1 && line === '') return '';
                return `<span class="line-number">${(index + 1).toString().padStart(2, ' ')}</span> ${line}`;
            }).join('\n');
            
            block.innerHTML = numberedLines;
        }
    });
    
    // Adicionar estilos para números de linha
    const style = document.createElement('style');
    style.textContent = `
        .line-number {
            color: #7f8c8d;
            margin-right: 1rem;
            user-select: none;
        }
    `;
    document.head.appendChild(style);
}

// Funções utilitárias

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function getTextNodes(element) {
    const textNodes = [];
    const walker = document.createTreeWalker(
        element,
        NodeFilter.SHOW_TEXT,
        null,
        false
    );
    
    let node;
    while (node = walker.nextNode()) {
        if (node.textContent.trim().length > 0) {
            textNodes.push(node);
        }
    }
    
    return textNodes;
}

function findNearestHeading(node) {
    let current = node.parentElement;
    
    while (current && current !== document.body) {
        const heading = current.querySelector('h1, h2, h3, h4, h5, h6');
        if (heading) return heading;
        
        const prevHeading = current.previousElementSibling;
        if (prevHeading && /^H[1-6]$/.test(prevHeading.tagName)) {
            return prevHeading;
        }
        
        current = current.parentElement;
    }
    
    return null;
}

function getContextAroundMatch(text, query, maxLength) {
    const lowerText = text.toLowerCase();
    const lowerQuery = query.toLowerCase();
    const index = lowerText.indexOf(lowerQuery);
    
    if (index === -1) return text.substring(0, maxLength) + '...';
    
    const start = Math.max(0, index - Math.floor(maxLength / 2));
    const end = Math.min(text.length, start + maxLength);
    
    let context = text.substring(start, end);
    
    if (start > 0) context = '...' + context;
    if (end < text.length) context = context + '...';
    
    return context;
}

function highlightText(text, query) {
    if (!query) return text;
    
    const regex = new RegExp(`(${escapeRegExp(query)})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

