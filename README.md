# 📝 Blog Code Examples

**Code companion for [Impact Learning Lab](https://impactlearninglab.io) tutorials**  
*Organized by category • Ready to run • Open source*

## 🗂️ Browse by Category

### 🤖 **AI & Machine Learning**
- [TensorFlow Basics](ai-ml/tensorflow-basics) - Your first neural network
- [OpenAI API Examples](ai-ml/openai-api-examples) - Chatbots and assistants
- [Computer Vision Starter](ai-ml/computer-vision-basics) - Image processing

### 🐍 **Python Development**
- [FastAPI REST API](python/api-fastapi-tutorial) - Modern Python backend
- [Web Scraping Guide](python/web-scraping) - Data extraction techniques
- [Automation Scripts](python/automation-scripts) - Practical Python utilities

### 🌐 **Web Development**
- [React Tutorial](web-dev/react-tutorial) - Components and hooks
- [Next.js Starter](web-dev/nextjs-starter) - Full-stack framework
- [CSS Animations](web-dev/css-animations) - Interactive UI effects

### ⚙️ **Tools & DevOps**
- [Docker Guide](tools-devops/docker-guide) - Containerization basics
- [Git Advanced](tools-devops/git-advanced) - Collaboration workflows
- [CI/CD with GitHub Actions](tools-devops/ci-cd-github-actions) - Automation pipelines

## 🚀 How to Use

1. **Find an article** on [our blog](https://impactlearninglab.io/blog)
2. **Click the GitHub link** in the article
3. **Navigate** to the corresponding folder
4. **Follow instructions** in the folder's README

## 📁 Repository Structure
blog-code-examples/
├── ai-ml/ # AI & Machine Learning tutorials
├── python/ # Python projects and scripts
├── web-dev/ # Frontend and full-stack web
├── tools-devops/ # DevOps, Docker, Git, CI/CD
└── _template/ # Template for new tutorials

text

## 🆕 Adding a New Tutorial

Use the `_template/` folder as a starting point:

```bash
cp -r _template/ python/new-tutorial-name
# Then customize the files
🔗 Connect
Website: impactlearninglab.io

Blog: impactlearninglab.io/blog

Twitter: @ImpactLearnLab

YouTube: Impact Learning Lab

📄 License
This repository is licensed under the MIT License - see the LICENSE file for details.

Making tech learning accessible through practical code examples.
Part of the Impact Learning Lab ecosystem.

text

### **3. Créer la structure de dossiers**
Il faut créer les dossiers **via l'interface web** :

**Méthode :**
1. Cliquez sur **Add file → Create new file**
2. Dans le champ de nom, tapez : `ai-ml/placeholder.md`
   - GitHub créera automatiquement le dossier `ai-ml/`
3. Dans le fichier, mettez juste `# Coming soon`
4. **Commit** avec "Create category folders"
5. Répétez pour :
   - `python/placeholder.md`
   - `web-dev/placeholder.md`
   - `tools-devops/placeholder.md`
   - `_template/README.md`

---

## 📦 **Template à créer :**

Créez le dossier `_template/` avec ces fichiers :

**`_template/README.md` :**
```markdown
# [Tutorial Title]

Brief description of what this tutorial covers.

## 🎯 Learning Objectives
- Objective 1
- Objective 2
- Objective 3

## 📁 Project Structure
project/
├── src/ # Source code
├── data/ # Sample data (optional)
├── tests/ # Test files (optional)
├── README.md # This file
├── requirements.txt # Python dependencies
└── .env.example # Environment variables template

text

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ / Node.js 16+
- Git installed

### Installation
```bash
# Clone this specific tutorial
git clone https://github.com/impactlearninglab/blog-code-examples.git
cd blog-code-examples/[category]/[tutorial-name]

# Install dependencies
pip install -r requirements.txt
# or
npm install
Running the Project
bash
python src/main.py
# or
npm start
📚 Related Resources
Blog Article

Video Tutorial

🤝 Contributing
Found a bug or have a suggestion? Open an Issue or Pull Request!

📄 License
MIT - see main repository LICENSE file.

Part of Impact Learning Lab tutorial series.

text

**`_template/requirements.txt` :**
```txt
# Python dependencies example
fastapi==0.104.1
uvicorn==0.24.0
python-dotenv==1.0.0
_template/.env.example :

env
# Environment variables
API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:password@localhost/dbname
DEBUG=True
