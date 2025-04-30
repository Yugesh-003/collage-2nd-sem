document.addEventListener("DOMContentLoaded", () => {
  fetchSongs(); // Fetch and display songs when the page loads

  document.querySelector("button[type='submit']").addEventListener("click", uploadSong);
});

// Function to upload a song
function uploadSong() {
  const title = document.getElementById("title").value.trim();
  const artist = document.getElementById("artist").value.trim();
  const posterFile = document.getElementById("posterUpload").files[0];
  const musicFile = document.getElementById("musicUpload").files[0];

  if (!title || !artist || !posterFile || !musicFile) {
      alert("Please fill all fields and upload both poster and song!");
      return;
  }

  const formData = new FormData();
  formData.append("title", title);
  formData.append("artist", artist);
  formData.append("poster", posterFile);
  formData.append("music", musicFile);

  fetch("/upload", {
      method: "POST",
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          alert("Song uploaded successfully!");
          fetchSongs(); // Refresh the displayed song list
      } else {
          alert("Error uploading song!");
      }
  })
  .catch(error => console.error("Error uploading:", error));
}

// Function to fetch and display uploaded songs
function fetchSongs() {
  fetch("/get-songs")
      .then(response => response.json())
      .then(songs => {
          const userSongsDiv = document.getElementById("userSongs");
          userSongsDiv.innerHTML = ""; // Clear the list before updating

          songs.forEach(song => {
              const songCard = document.createElement("div");
              songCard.classList.add("song-card");

              songCard.innerHTML = `
                  <img src="${song.poster}" alt="${song.title}" width="100">
                  <p><strong>${song.title}</strong> by ${song.artist}</p>
                  <button onclick="playSong('${song.link}')">▶ Play</button>
              `;

              userSongsDiv.appendChild(songCard);
          });
      })
      .catch(error => console.error("Error fetching songs:", error));
}

// Function to play a song using the global audio player
function playSong(songUrl) {
  const audioPlayer = document.getElementById("audioPlayer");
  console.log("Playing:", songUrl); // Debugging output
  audioPlayer.src = songUrl.startsWith("/") ? songUrl : `/${songUrl}`;
  audioPlayer.play().catch(error => console.error("Playback error:", error));
}
