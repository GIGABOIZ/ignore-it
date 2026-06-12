<div align="center">

# 🚫 Ignore-It

*Stop Googling for .gitignore files. Generate them instantly from your terminal.*

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Terminal](https://img.shields.io/badge/CLI-Terminal-black.svg?style=for-the-badge&logo=windows-terminal&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)

</div>

<hr>

## 💡 The Problem
Every time you start a new project, you need a `.gitignore` file. Manually searching for the right templates, copying, and pasting them is tedious and breaks your flow.

## ✨ The Solution
**Ignore-It** is a blazing-fast CLI tool that pulls official, up-to-date `.gitignore` templates directly from GitHub's repository and saves them to your project folder instantly. 

## 🚀 Key Features
- ⚡ **Instant Fetch:** Pulls templates in milliseconds.
- ➕ **Combine Templates:** Need Python AND Node.js in the same project? Fetch both at the same time.
- 🛡️ **Safe Append:** If a `.gitignore` already exists, it safely appends the new rules without overwriting your existing ones.

---

## 🛠️ Installation

Install it globally using `pip`:

\`\`\`bash
pip install git+https://github.com/GIGABOIZ/ignore-it.git
\`\`\`

---

## 💻 Usage

Navigate to your project directory and tell the CLI which templates you need:

**1. Generate for a single language:**
\`\`\`bash
ignore-it Python
\`\`\`

**2. Generate for multiple technologies at once:**
\`\`\`bash
ignore-it Node React Go
\`\`\`

*(Note: The tool automatically handles capitalization to match GitHub's exact template names).*

---

<div align="center">
  <b>Built with 💻 by <a href="https://github.com/GIGABOIZ">GIGABOIZ</a></b>
</div>
