const mongoose = require("mongoose");

const songSchema = new mongoose.Schema({
    title: String,
    filePath: String
});

module.exports = mongoose.model("Song", songSchema);