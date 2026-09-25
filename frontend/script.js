const API_BASE = window.location.origin.startsWith("http") ? window.location.origin : "http://127.0.0.1:8000";

const elements = {
    select: document.getElementById('movie-select'),
    btn: document.getElementById('recommend-btn'),
    loading: document.getElementById('loading'),
    resultsSection: document.getElementById('results-section'),
    likedTitle: document.getElementById('liked-movie-title'),
    likedMeta: document.getElementById('liked-movie-meta'),
    grid: document.getElementById('recommendations-grid')
};

async function fetchMovies() {
    try {
        const response = await fetch(`${API_BASE}/movies`);
        const movies = await response.json();
        
        elements.select.innerHTML = '<option value="" disabled selected>Select a masterpiece...</option>';
        movies.forEach(movie => {
            const option = document.createElement('option');
            option.value = movie.id;
            // truncate title if needed, though they are short
            option.textContent = movie.title;
            elements.select.appendChild(option);
        });
    } catch (error) {
        console.error("Error fetching movies:", error);
        elements.select.innerHTML = '<option value="" disabled>Error loading movies. Is backend running?</option>';
    }
}

async function getRecommendations() {
    const movieId = elements.select.value;
    if (!movieId) return;

    // Show loading
    elements.loading.classList.remove('hidden');
    elements.resultsSection.classList.add('hidden');
    elements.grid.innerHTML = '';
    
    // Disable button
    elements.btn.disabled = true;
    elements.btn.textContent = 'Processing...';

    try {
        const response = await fetch(`${API_BASE}/recommendations/${movieId}?top_n=5`);
        const data = await response.json();
        
        // Populate Liked Movie Info
        const liked = data.movie;
        elements.likedTitle.textContent = liked.title;
        elements.likedMeta.innerHTML = `
            <strong>Director:</strong> ${liked.director} &bull; 
            <strong>Genre:</strong> ${liked.genre} <br>
            <strong>Starring:</strong> ${liked.actors}
        `;

        // Populate Recommendations
        data.recommendations.forEach(rec => {
            const simPercentage = (rec.similarity_score * 100).toFixed(0);
            
            const card = document.createElement('div');
            card.className = 'movie-card';
            card.innerHTML = `
                <div class="card-image-wrap">
                    <img src="${rec.poster_url || 'https://via.placeholder.com/500x750?text=No+Poster'}" alt="${rec.title}" class="card-image" onerror="this.src='https://via.placeholder.com/500x750?text=No+Poster'">
                    <div class="sim-score">${simPercentage}% Match</div>
                </div>
                <div class="card-content">
                    <h4 class="card-title">${rec.title}</h4>
                    <p class="card-genre">${rec.genre}</p>
                    <p class="card-desc">${rec.description}</p>
                </div>
            `;
            elements.grid.appendChild(card);
        });

        // Show results
        elements.resultsSection.classList.remove('hidden');
        
        // Scroll to results smoothly
        elements.resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

    } catch (error) {
        console.error("Error fetching recommendations:", error);
        alert("Failed to get recommendations. Make sure the backend server is running.");
    } finally {
        elements.loading.classList.add('hidden');
        elements.btn.disabled = false;
        elements.btn.textContent = 'Get Recommendations';
    }
}

// Event Listeners
document.addEventListener('DOMContentLoaded', fetchMovies);
elements.btn.addEventListener('click', getRecommendations);
