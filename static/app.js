// 전역 상태
const state = {
    allRunes: [],
    selectedRunes: [],
    filters: {
        grade: '',
        property: '',
        part: '',
        set_name: ''
    }
};

// 한글 매핑
const translations = {
    grade: {
        legendary: '전설',
        epic: '영웅',
        rare: '희귀',
        common: '일반'
    },
    property: {
        fire: '화',
        water: '수',
        wind: '풍',
        earth: '지',
        light: '광',
        dark: '암'
    },
    part: {
        head: '머리',
        chest: '가슴',
        gloves: '장갑',
        boots: '신발',
        weapon: '무기',
        accessory: '장신구'
    },
    stat: {
        hp: 'HP',
        atk: '공격력',
        def: '방어력',
        crit_rate: '치명타 확률',
        crit_dmg: '치명타 피해',
        speed: '속도',
        accuracy: '정확도',
        resistance: '저항'
    }
};

// API 호출
async function fetchRunes(filters = {}) {
    const params = new URLSearchParams();
    Object.entries(filters).forEach(([key, value]) => {
        if (value) params.append(key, value);
    });
    
    const response = await fetch(`/api/runes?${params}`);
    return await response.json();
}

async function calculateSynergy(runeIds) {
    if (runeIds.length === 0) {
        return null;
    }
    
    const params = new URLSearchParams();
    runeIds.forEach(id => params.append('rune_ids', id));
    
    const response = await fetch(`/api/calculate?${params}`);
    return await response.json();
}

// UI 렌더링
function renderRuneCard(rune, isSelected = false) {
    const card = document.createElement('div');
    card.className = `rune-card ${isSelected ? 'selected' : ''}`;
    card.dataset.runeId = rune.id;
    
    const gradeText = translations.grade[rune.grade] || rune.grade;
    const propertyText = translations.property[rune.property] || rune.property;
    const partText = translations.part[rune.part] || rune.part;
    
    const statsHtml = rune.base_stats.map(stat => {
        const statName = translations.stat[stat.stat_type] || stat.stat_type;
        return `
            <div class="stat-item">
                <span class="stat-name">${statName}</span>
                <span class="stat-value-item">+${stat.value}</span>
            </div>
        `;
    }).join('');
    
    card.innerHTML = `
        <div class="rune-header">
            <div class="rune-name">${rune.name}</div>
            <div class="rune-badges">
                <span class="badge grade-${rune.grade}">${gradeText}</span>
                <span class="badge property-${rune.property}">${propertyText}</span>
            </div>
        </div>
        <div class="rune-info">
            <div class="rune-set">🎴 ${rune.set_name}</div>
            <div class="rune-part">📍 ${partText}</div>
        </div>
        <div class="rune-stats">
            ${statsHtml}
        </div>
    `;
    
    card.addEventListener('click', () => toggleRuneSelection(rune));
    
    return card;
}

function renderRunes(runes, containerId, selected = false) {
    const container = document.getElementById(containerId);
    container.innerHTML = '';
    container.classList.remove('loading');
    
    if (runes.length === 0) {
        container.innerHTML = '<div class="empty-state"><p>조건에 맞는 룬이 없습니다</p></div>';
        return;
    }
    
    runes.forEach(rune => {
        container.appendChild(renderRuneCard(rune, selected));
    });
}

function renderSynergyDashboard(stats) {
    const synergyContainer = document.getElementById('synergy-dashboard');
    const statsContainer = document.getElementById('total-stats');
    
    if (!stats || state.selectedRunes.length === 0) {
        synergyContainer.innerHTML = '<div class="empty-state"><p>룬을 선택하면 시너지가 표시됩니다</p></div>';
        statsContainer.innerHTML = '<div class="empty-state"><p>룬을 선택하면 스탯이 표시됩니다</p></div>';
        return;
    }
    
    // 시너지 렌더링
    synergyContainer.innerHTML = '';
    if (stats.active_set_effects.length === 0) {
        synergyContainer.innerHTML = '<div class="empty-state"><p>활성화된 시너지가 없습니다</p></div>';
    } else {
        stats.active_set_effects.forEach(effect => {
            const card = document.createElement('div');
            card.className = `synergy-card ${effect.is_active ? 'active' : 'inactive'}`;
            
            const bonusHtml = effect.is_active && effect.bonus_stats.length > 0 
                ? `<div class="synergy-bonus">
                    ${effect.bonus_stats.map(stat => {
                        const statName = translations.stat[stat.stat_type] || stat.stat_type;
                        return `<div class="bonus-stat">✨ ${statName} +${stat.value}${stat.stat_type.includes('rate') || stat.stat_type.includes('dmg') ? '%' : ''}</div>`;
                    }).join('')}
                   </div>`
                : '';
            
            card.innerHTML = `
                <div class="synergy-header">
                    <div class="synergy-title">${effect.set_name}</div>
                    <div class="synergy-progress">${effect.current_count}/${effect.required_count}</div>
                </div>
                <div class="synergy-description">${effect.description}</div>
                ${bonusHtml}
            `;
            
            synergyContainer.appendChild(card);
        });
    }
    
    // 총합 스탯 렌더링
    statsContainer.innerHTML = '';
    Object.entries(stats.total_stats).forEach(([statType, value]) => {
        const statName = translations.stat[statType] || statType;
        const badge = document.createElement('div');
        badge.className = 'stat-badge';
        badge.innerHTML = `
            <span class="stat-label">${statName}</span>
            <span class="stat-value">${Math.round(value)}</span>
        `;
        statsContainer.appendChild(badge);
    });
}

// 룬 선택/해제
function toggleRuneSelection(rune) {
    const index = state.selectedRunes.findIndex(r => r.id === rune.id);
    
    if (index >= 0) {
        state.selectedRunes.splice(index, 1);
    } else {
        state.selectedRunes.push(rune);
    }
    
    updateUI();
}

function clearSelection() {
    state.selectedRunes = [];
    updateUI();
}

// UI 업데이트
async function updateUI() {
    // 선택된 룬 개수 업데이트
    document.getElementById('selected-count').textContent = state.selectedRunes.length;
    
    // 선택된 룬 표시
    const selectedContainer = document.getElementById('selected-runes-container');
    if (state.selectedRunes.length === 0) {
        selectedContainer.innerHTML = '<div class="empty-state"><p>선택된 룬이 없습니다</p></div>';
    } else {
        renderRunes(state.selectedRunes, 'selected-runes-container', true);
    }
    
    // 전체 룬 목록에서 선택 상태 업데이트
    document.querySelectorAll('#runes-container .rune-card').forEach(card => {
        const runeId = card.dataset.runeId;
        const isSelected = state.selectedRunes.some(r => r.id === runeId);
        card.classList.toggle('selected', isSelected);
    });
    
    // 시너지 계산 및 표시
    if (state.selectedRunes.length > 0) {
        const runeIds = state.selectedRunes.map(r => r.id);
        const stats = await calculateSynergy(runeIds);
        renderSynergyDashboard(stats);
    } else {
        renderSynergyDashboard(null);
    }
    
    // URL 업데이트 (히스토리에 추가하지 않음)
    updateURL();
}

// 필터 적용
async function applyFilters() {
    const filteredRunes = await fetchRunes(state.filters);
    renderRunes(filteredRunes, 'runes-container');
}

function resetFilters() {
    state.filters = {
        grade: '',
        property: '',
        part: '',
        set_name: ''
    };
    
    document.getElementById('filter-grade').value = '';
    document.getElementById('filter-property').value = '';
    document.getElementById('filter-part').value = '';
    document.getElementById('filter-set').value = '';
    
    applyFilters();
}

// URL 공유 기능
function updateURL() {
    const params = new URLSearchParams();
    if (state.selectedRunes.length > 0) {
        state.selectedRunes.forEach(rune => {
            params.append('rune', rune.id);
        });
    }
    
    const newUrl = params.toString() 
        ? `${window.location.pathname}?${params.toString()}`
        : window.location.pathname;
    
    window.history.replaceState({}, '', newUrl);
}

function getShareURL() {
    return window.location.href;
}

function loadFromURL() {
    const params = new URLSearchParams(window.location.search);
    const runeIds = params.getAll('rune');
    
    if (runeIds.length > 0) {
        state.selectedRunes = state.allRunes.filter(rune => runeIds.includes(rune.id));
        updateUI();
    }
}

// 모달 관리
function showShareModal() {
    const modal = document.getElementById('share-modal');
    const shareUrlInput = document.getElementById('share-url');
    shareUrlInput.value = getShareURL();
    modal.classList.add('show');
}

function hideShareModal() {
    const modal = document.getElementById('share-modal');
    modal.classList.remove('show');
}

// 초기화
async function init() {
    // 모든 룬 로드
    state.allRunes = await fetchRunes();
    renderRunes(state.allRunes, 'runes-container');
    
    // 세트 필터 옵션 채우기
    const setNames = [...new Set(state.allRunes.map(r => r.set_name))];
    const setFilter = document.getElementById('filter-set');
    setNames.forEach(setName => {
        const option = document.createElement('option');
        option.value = setName;
        option.textContent = setName;
        setFilter.appendChild(option);
    });
    
    // URL에서 선택된 룬 로드
    loadFromURL();
    
    // 이벤트 리스너 등록
    document.getElementById('filter-grade').addEventListener('change', (e) => {
        state.filters.grade = e.target.value;
        applyFilters();
    });
    
    document.getElementById('filter-property').addEventListener('change', (e) => {
        state.filters.property = e.target.value;
        applyFilters();
    });
    
    document.getElementById('filter-part').addEventListener('change', (e) => {
        state.filters.part = e.target.value;
        applyFilters();
    });
    
    document.getElementById('filter-set').addEventListener('change', (e) => {
        state.filters.set_name = e.target.value;
        applyFilters();
    });
    
    document.getElementById('reset-filters').addEventListener('click', resetFilters);
    document.getElementById('clear-selection').addEventListener('click', clearSelection);
    document.getElementById('share-build').addEventListener('click', showShareModal);
    
    // 모달 닫기
    document.querySelector('.close').addEventListener('click', hideShareModal);
    document.getElementById('share-modal').addEventListener('click', (e) => {
        if (e.target.id === 'share-modal') {
            hideShareModal();
        }
    });
    
    // URL 복사
    document.getElementById('copy-url').addEventListener('click', () => {
        const shareUrlInput = document.getElementById('share-url');
        shareUrlInput.select();
        document.execCommand('copy');
        
        const button = document.getElementById('copy-url');
        button.textContent = '복사됨!';
        setTimeout(() => {
            button.textContent = '복사';
        }, 2000);
    });
}

// 페이지 로드 시 초기화
document.addEventListener('DOMContentLoaded', init);
