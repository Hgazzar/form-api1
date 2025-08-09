import express from "express";
import cors from "cors";

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// POST endpoint for form submission
app.post("/register", (req, res) => {
  const { title, name, email, phone, institution, city, scfhsNo, plan } = req.body;

  if (!title || !name || !email || !phone || !institution || !city || !scfhsNo || !plan) {
    return res.status(400).json({ error: "All fields are required" });
  }

  // Here you could save to DB or send email, etc.
  console.log("New registration:", req.body);

  res.json({
    message: "Registration received successfully",
    data: req.body
  });
});

// Default route
app.get("/", (req, res) => {
  res.send("Registration API is running");
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
