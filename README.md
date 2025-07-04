# 🤖 Automated Question Builder

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

An AI-powered system that automatically generates objective questions and answers from input topics.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Smart Question Generation** | Automatically creates multiple-choice questions from any topic |
| 🔍 **Answer Synthesis** | Generates correct answers with plausible distractors |
| 🛠️ **Customizable Input** | Works with any subject matter or keywords |
| 🌐 **Web Interface** | User-friendly Flask web application |

## 🏗️ Project Structure

```bash
Automated-Question-Builder/
├── app.py              # Main Flask application
├── objective.py        # Question generation logic
├── requirements.txt    # Dependencies
└── templates/          # HTML templates
    ├── index.html
    └── results.html
```
## 🚀 Quick Start

```
# Clone repository
git clone https://github.com/ArmanAhmed00/Automated-Question-Builder.git
cd Automated-Question-Builder

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Launch application
flask run
```


## 🧠 How It Works

```mermaid
graph TD
    A[Input Topic] --> B(NLP Processing)
    B --> C[Question Generation]
    C --> D[Answer Synthesis]
    D --> E[Distractor Creation]
    E --> F[Output Formatting]
```

### Sample Output Section
```markdown
## 📊 Sample Output

```json
{
  "topic": "Cryptography",
  "questions": [
    {
      "question": "Which is symmetric encryption?",
      "options": ["A) RSA", "B) AES (✓)", "C) ECC", "D) DSA"],
      "explanation": "AES uses same key for encryption/decryption"
    }
  ]
}
```

### License Section
```markdown
## 📜 License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**Permissions**:
- Commercial use
- Modification
- Distribution

**Limitations**:
- Liability
- Warranty
```
## 🤝 Contributing

```diff
# Recommended Workflow:
+ 1. Open an issue to discuss changes
+ 2. Fork the repository
+ 3. Create feature branch (git checkout -b feat/xyz)
+ 4. Commit changes (git commit -m 'feat: add xyz')
+ 5. Push to branch (git push origin feat/xyz)
+ 6. Open pull request
```

## 📬 Contact
<div align="center">

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:armanofficial2401@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/armanahmed24)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ArmanAhmed00)

</div>
