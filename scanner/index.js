const express = require("express");
const multer = require("multer");
const axios = require("axios");
const FormData = require("form-data");

const app = express();
const port = 3000;

// Set up Multer for handling file uploads
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

const storageUrl = process.env.STORAGE_URL;
// Serve the HTML form
app.get("/", (req, res) => {
    res.sendFile(__dirname + "/index.html");
});

// Handle file uploads
app.post("/upload", upload.single("image"), async (req, res) => {
    try {
        if (!req.file) {
            return res.status(400).send("No file uploaded.");
        }
        
        const formData = new FormData();
        formData.append("image", req.file.buffer, {
            filename: "image.jpg",
            contentType: req.file.mimetype,
        });

    const response = await axios.post(storageUrl, formData, {
      headers: {
        ...formData.getHeaders(),
        "Content-Type": `multipart/form-data; boundary=${formData.getBoundary()}`,
      },
    });

    console.log("External API response:", response.data);

    res.send("Image uploaded successfully.");
  } catch (error) {
    console.error("Error uploading image:", error.message);
    res.status(500).send("Internal Server Error");
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
