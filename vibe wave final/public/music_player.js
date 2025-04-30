'use strict';

/**
 * Global Variables
 */
let musicData = [];
let currentMusic = 0;
let isShuffled = false;
const audioSource = new Audio();

/**
 * Utility Functions
 */

// Format time in MM:SS
const getTimecode = (duration) => {
  if (isNaN(duration) || duration === Infinity) return '0:00'; // Fallback for invalid durations
  const minutes = Math.floor(duration / 60);
  const seconds = Math.floor(duration % 60);
  return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
};

// Get query parameters from the URL
const getQueryParam = (param) => {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(param);
};

/**
 * DOM Elements
 */
const playerBanner = document.querySelector('[data-player-banner]');
const playerTitle = document.querySelector('[data-title]');
const playerArtist = document.querySelector('[data-artist]');
const playerSeekRange = document.querySelector('[data-seek]');
const playerRunningTime = document.querySelector('[data-running-time]');
const playerDuration = document.querySelector('[data-duration]');
const playerVolumeRange = document.querySelector('[data-volume]');
const playerVolumeBtn = document.querySelector('[data-volume-btn]');
const playBtn = document.querySelector('[data-play-btn]');
const playerSkipNextBtn = document.querySelector('[data-skip-next]');
const playerSkipPrevBtn = document.querySelector('[data-skip-prev]');
const playerShuffleBtn = document.querySelector('[data-shuffle]');
const playerRepeatBtn = document.querySelector('[data-repeat]');

/**
 * Player Functions
 */

// Update the player UI with the current song's information
const updatePlayerInfo = () => {
  const song = musicData[currentMusic];
  if (!song) {
    console.error('Song data not found for the current index.');
    return;
  }

  // Update the player UI
  playerBanner.src = song.poster || '../images/default.jpg';
  playerBanner.setAttribute('alt', `${song.title} Album Poster`);
  playerTitle.textContent = song.title;
  playerArtist.textContent = song.artist || 'Unknown Artist';

  // Update audio source
  audioSource.src = song.link;

  // Handle cases where the song link is invalid
  if (!song.link || song.link === '#') {
    console.warn('Song link is not available.');
    audioSource.pause();
    playerDuration.textContent = '0:00'; // Fallback for invalid songs
    return;
  }

  // Update seek bar and duration when metadata is loaded
  audioSource.addEventListener('loadedmetadata', () => {
    console.log('Audio metadata loaded. Duration:', audioSource.duration); // Debugging
    const durationText = getTimecode(audioSource.duration || 0);
    console.log('Updating playerDuration with:', durationText); // Debugging
    playerDuration.textContent = durationText; // Set duration
    updateSeekBar(); // Update seek bar
  });
};

// Update the seek bar and duration
const updateSeekBar = () => {
  console.log('Updating seek bar...');
  const seekFill = document.querySelector('.seek-fill'); // Add a fill effect to the seek bar
  playerSeekRange.max = Math.ceil(audioSource.duration) || 0; // Set max value of the range
  playerSeekRange.value =
    (audioSource.currentTime / audioSource.duration) * 100 || 0; // Set current value of the range
  playerRunningTime.textContent = getTimecode(audioSource.currentTime || 0); // Update running time

  // Update the seek bar fill
  const seekPercentage =
    (audioSource.currentTime / audioSource.duration) * 100 || 0;
  seekFill.style.width = `${seekPercentage}%`;
  console.log('Seek bar updated:', seekPercentage); // Debugging
};

// Event listener for updating the seek bar as the song plays
audioSource.addEventListener('timeupdate', updateSeekBar);

// Ensure metadata is loaded before updating the seek bar
audioSource.addEventListener('loadedmetadata', () => {
  console.log('Audio metadata loaded. Duration:', audioSource.duration); // Debugging
  playerDuration.textContent = getTimecode(audioSource.duration || 0); // Set duration
  updateSeekBar(); // Update seek bar
});

// Update the volume control
const updateVolume = () => {
  const volumeFill = document.querySelector('.volume-fill'); // Add a fill effect to the volume bar
  const volumePercentage = playerVolumeRange.value * 100;
  volumeFill.style.width = `${volumePercentage}%`;

  if (audioSource.volume <= 0.1) {
    playerVolumeBtn.children[0].textContent = 'volume_mute';
  } else if (audioSource.volume <= 0.5) {
    playerVolumeBtn.children[0].textContent = 'volume_down';
  } else {
    playerVolumeBtn.children[0].textContent = 'volume_up';
  }
};

// Play or pause the music
const playMusic = () => {
  console.log('playMusic function called');
  if (audioSource.paused) {
    audioSource.play();
    playBtn.classList.add('active');
  } else {
    audioSource.pause();
    playBtn.classList.remove('active');
  }
};

// Skip to the next song
const skipNext = () => {
  currentMusic = isShuffled
    ? Math.floor(Math.random() * musicData.length)
    : (currentMusic + 1) % musicData.length;
  updatePlayerInfo();
  playMusic();
};

// Skip to the previous song
const skipPrev = () => {
  currentMusic =
    currentMusic === 0
      ? musicData.length - 1
      : isShuffled
      ? Math.floor(Math.random() * musicData.length)
      : currentMusic - 1;
  updatePlayerInfo();
  playMusic();
};

// Toggle shuffle mode
const shuffle = () => {
  isShuffled = !isShuffled;
  playerShuffleBtn.classList.toggle('active', isShuffled);
};

// Toggle repeat mode
const repeat = () => {
  audioSource.loop = !audioSource.loop;
  playerRepeatBtn.classList.toggle('active', audioSource.loop);
};

// Seek music
const seek = (e) => {
  const seekValue = e.target.value;
  console.log('Seek value:', seekValue); // Debugging
  audioSource.currentTime = (seekValue / 100) * audioSource.duration; // Map slider value to audio duration
  console.log('Updated currentTime:', audioSource.currentTime); // Debugging
  updateSeekBar(); // Update the seek bar UI
};

// Change volume
const changeVolume = (e) => {
  audioSource.volume = e.target.value;
  updateVolume();
};

// Mute or unmute volume
const muteVolume = () => {
  audioSource.muted = !audioSource.muted;
  playerVolumeBtn.children[0].textContent = audioSource.muted
    ? 'volume_off'
    : 'volume_up';
};

/**
 * Initialize the Player
 */
const initializePlayer = async () => {
  try {
    const response = await fetch('music.json');
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    musicData = await response.json();

    // Debugging: Log the fetched music data
    console.log('Fetched music data:', musicData);

    loadMusicFromQuery(); // Load the music based on the query parameter
  } catch (error) {
    console.error('Error fetching music data:', error);
  }
};

// Function to load music based on the query parameter
const loadMusicFromQuery = () => {
  const songIndex = getQueryParam('song');
  console.log('Song index from query parameter:', songIndex); // Debugging

  if (songIndex !== null && musicData[songIndex]) {
    currentMusic = parseInt(songIndex, 10);
    console.log('Current music data:', musicData[currentMusic]); // Debugging
    updatePlayerInfo(); // Update the player with the selected song
  } else {
    console.error('Invalid song index or song data not found.');
  }
};

/**
 * Event Listeners
 */
playBtn.addEventListener('click', playMusic);
playerSkipNextBtn.addEventListener('click', skipNext);
playerSkipPrevBtn.addEventListener('click', skipPrev);
playerShuffleBtn.addEventListener('click', shuffle);
playerRepeatBtn.addEventListener('click', repeat);
playerSeekRange.addEventListener('input', seek);
playerVolumeRange.addEventListener('input', changeVolume);
playerVolumeBtn.addEventListener('click', muteVolume);

// Start the player initialization when the page loads
document.addEventListener('DOMContentLoaded', initializePlayer);
