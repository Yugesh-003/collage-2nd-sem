const express = require("express");
const multer = require("multer");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = 3000;

// Serve static files from the "public" folder
//app.use(express.static("public"));
// Serve static files from "public"
app.use(express.static(path.join(__dirname, "public")));

app.use("/uploads", express.static(path.join(__dirname, "uploads")));

// Route to serve the upload page
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "upload.html"));
});
app.use(express.json());

// File paths
const uploadsDir = path.join(__dirname, "uploads");
const musicDir = path.join(uploadsDir, "music");
const posterDir = path.join(uploadsDir, "poster");
const musicJsonPath = path.join(uploadsDir, "music.json");

// Ensure necessary directories exist
if (!fs.existsSync(uploadsDir)) fs.mkdirSync(uploadsDir);
if (!fs.existsSync(musicDir)) fs.mkdirSync(musicDir);
if (!fs.existsSync(posterDir)) fs.mkdirSync(posterDir);
if (!fs.existsSync(musicJsonPath)) fs.writeFileSync(musicJsonPath, "[]", "utf8");

// Multer storage configuration for files
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        if (file.mimetype.startsWith("image/")) {
            cb(null, posterDir);
        } else if (file.mimetype.startsWith("audio/")) {
            cb(null, musicDir);
        } else {
            cb(new Error("Invalid file type"), null);
        }
    },
    filename: (req, file, cb) => {
        const uniqueName = `${Date.now()}-${file.originalname}`;
        cb(null, uniqueName);
    },
});

const upload = multer({ storage });

// 🔹 Handle song upload
app.post("/upload", upload.fields([{ name: "poster" }, { name: "music" }]), (req, res) => {
    const { title, artist } = req.body;
    const posterFile = req.files["poster"] ? req.files["poster"][0] : null;
    const musicFile = req.files["music"] ? req.files["music"][0] : null;

    if (!title || !artist || !posterFile || !musicFile) {
        return res.status(400).json({ error: "All fields are required" });
    }

    // Construct file paths
    const posterPath = `/uploads/poster/${posterFile.filename}`;
    const musicPath = `/uploads/music/${musicFile.filename}`;

    // Read existing songs
    fs.readFile(musicJsonPath, "utf8", (err, data) => {
        let songs = [];
        if (!err && data) {
            try {
                songs = JSON.parse(data);
            } catch (parseError) {
                console.error("Error parsing music.json:", parseError);
                return res.status(500).json({ error: "Error parsing song list" });
            }
        }

        // Add new song entry
        const newSong = { title, artist, poster: posterPath, link: musicPath };
        songs.push(newSong);

        // Write updated song list
        fs.writeFile(musicJsonPath, JSON.stringify(songs, null, 2), "utf8", (writeErr) => {
            if (writeErr) {
                console.error("Error writing music.json:", writeErr);
                return res.status(500).json({ error: "Error saving song" });
            }
            res.json({ message: "Song uploaded successfully", song: newSong });
        });
    });
});

// 🔹 Get all songs
app.get("/get-songs", (req, res) => {
    fs.readFile(musicJsonPath, "utf8", (err, data) => {
        if (err) {
            console.error("Error reading music.json:", err);
            return res.status(500).json({ error: "Error reading song list" });
        }
        try {
            const songs = JSON.parse(data);
            res.json(songs);
        } catch (parseError) {
            console.error("Error parsing music.json:", parseError);
            res.status(500).json({ error: "Error parsing song list" });
        }
    });
});

// Start the server
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
