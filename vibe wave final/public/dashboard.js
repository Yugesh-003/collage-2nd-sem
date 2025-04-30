'use strict';

const container = document.getElementById('music-container');
const defaultPoster = '../images/default.jpg'; // Set your default image path

// Function to redirect to the player page with the selected song
const redirectToPlayer = (songIndex) => {
  window.location.href = `music_player.html?song=${songIndex}`;
};

// Function to handle image errors
const handleImageError = (img) => {
  img.onerror = null; // Prevent infinite loop
  img.src = defaultPoster;
};

// Function to fetch and load music data
const loadMusicCards = () => {
  fetch('music.json')
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((musicData) => {
      container.innerHTML = ''; // Clear existing content

      musicData.forEach((music, index) => {
        const musicCard = document.createElement('div');
        musicCard.classList.add('music-link');

        musicCard.innerHTML = `
          <div class="music-info">
            <img 
              src="${music.poster}" 
              alt="${music.title} by ${music.artist}" 
              class="music-img" 
              onerror="handleImageError(this)"
            />
            <div class="music-name">
              <p class="title">${music.title}</p>
              <p class="artist">${music.artist}</p>
            </div>
          </div>
        `;

        // Add click event to redirect to the player page with the song index
        musicCard.addEventListener('click', () => redirectToPlayer(index));

        container.appendChild(musicCard);
      });
    })
    .catch((error) => {
      console.error('Error loading music:', error);
      container.innerHTML =
        '<p>Error loading music data. Please try again later.</p>';
    });
};

// Load the music cards when the page loads
document.addEventListener('DOMContentLoaded', loadMusicCards);
