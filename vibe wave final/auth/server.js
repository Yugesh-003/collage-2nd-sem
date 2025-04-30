const express = require('express');
const fs = require('fs');
const bcrypt = require('bcrypt');

const app = express();
app.use(express.json());

const AUTH_FILE = 'auth.json';
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'auth', 'login.html'));
});
// Function to read user data
const readUsers = () => {
  if (!fs.existsSync(AUTH_FILE)) return [];
  return JSON.parse(fs.readFileSync(AUTH_FILE, 'utf8'));
};

// Function to write user data
const writeUsers = (users) => {
  fs.writeFileSync(AUTH_FILE, JSON.stringify(users, null, 2));
};

// ✅ Signup Endpoint
app.post('/auth/signup', async (req, res) => {
  const { name, email, password } = req.body;
  let users = readUsers();

  // Check if email already exists
  if (users.some((user) => user.email === email)) {
    return res.status(400).json({ error: 'Email already registered!' });
  }

  // Hash the password before storing
  const hashedPassword = await bcrypt.hash(password, 10);
  users.push({ name, email, password: hashedPassword });
  writeUsers(users);

  res.json({ message: 'Signup successful!' });
});

// ✅ Login Endpoint
app.post('/auth/login', async (req, res) => {
  const { email, password } = req.body;
  let users = readUsers();

  const user = users.find((u) => u.email === email);
  if (!user) return res.status(400).json({ error: 'User not found!' });

  // Check password
  const isMatch = await bcrypt.compare(password, user.password);
  if (!isMatch) return res.status(400).json({ error: 'Invalid password!' });

  res.json({ message: 'Login successful!' });
});

// Start Server
app.listen(3000, () => console.log('Server running on port 3000'));
