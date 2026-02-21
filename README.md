# 🧠 Basic Quiz App

A lightweight and interactive quiz application built with **Python** and **Streamlit**. Designed to be simple, extensible, and easy to customize — with a structure that supports future feature additions.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [How It Works](#how-it-works)
- [Adding Questions](#adding-questions)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 Overview

**Basic Quiz App** is a simple, browser-based quiz application that leverages the power of Streamlit to deliver an interactive user experience without the need for complex frontend development. Questions are stored separately for easy management, making it straightforward to expand or modify the quiz content.

---

## ✨ Features

- ✅ Interactive quiz interface in the browser
- ✅ Clean and minimal UI powered by Streamlit
- ✅ Modular question management via a dedicated `questions/` folder
- ✅ Instant score/result display after submission
- ✅ Easy to extend with new questions or features

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core programming language |
| Streamlit | Web UI framework |

---

## 📁 Project Structure

```
Basic-Quiz-App/
│
├── questions/          # Contains quiz question data files
│
├── app.py              # Main Streamlit application entry point
├── requirement.txt     # Python dependencies
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DeepTensor-3070/Basic-Quiz-App.git
   cd Basic-Quiz-App
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   venv\Scripts\activate           # On Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirement.txt
   ```

### Running the App

```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`.

---

## 💡 How It Works

1. The app reads quiz questions from the `questions/` directory on startup.
2. Questions are displayed one by one (or all at once) in the Streamlit interface.
3. The user selects or types their answers.
4. Upon submission, the app calculates and displays the final score.

---

## ➕ Adding Questions

To add new questions, navigate to the `questions/` folder and follow the existing format of the question files. This modular approach makes it easy to:

- Add questions without touching the main app logic
- Organize questions by topic or difficulty
- Swap question sets for different quiz sessions

---

## 🔮 Future Improvements

- [ ] Support for multiple quiz categories
- [ ] Timer functionality per question
- [ ] User authentication and score history
- [ ] Difficulty levels (Easy / Medium / Hard)
- [ ] Leaderboard / scoreboard feature
- [ ] Import questions from CSV or JSON files
- [ ] Dark mode support

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please make sure your code follows clean coding practices and is well-commented.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
  Made with ❤️ using Python & Streamlit
  Create By DeepTensor
</div>
