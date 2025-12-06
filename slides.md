---
marp: true
theme: custom
paginate: true
footer: "23f2001288@ds.study.iitm.ac.in"
---

<!-- Custom Theme Definition -->
<style>
:root {
  --primary: #1565c0;
  --text: #333;
  --bg: #f5f7fa;
}

section {
  background: var(--bg);
  font-family: "Inter", sans-serif;
  color: var(--text);
}

h1, h2, h3 {
  color: var(--primary);
}

.custom-box {
  border: 2px solid var(--primary);
  padding: 20px;
  border-radius: 10px;
  background: white;
}
</style>

# Product Documentation  
### Prepared by: Ayush Dayal  
### Email: **23f2001288@ds.study.iitm.ac.in**

---

# Documentation Overview

- Git-based version control  
- Marp-based presentation  
- Export to **PDF**, **PPTX**, **HTML**  
- Custom themes for consistency  
- Math support & background images  

---

---
background: "https://picsum.photos/1600/900"
---

# Background Image Slide

A proper YAML `background:` directive, fully compatible with Marp CLI.

---

# Algorithmic Complexity

Using KaTeX math:

\[
T(n) = 2T\left(\frac{n}{2}\right) + O(n)
\]

\[
T(n) = O(n \log n)
\]

---

# Custom Styling Example

<div class="custom-box">

## Styled Content Block

Marp allows custom CSS inside slides using `<style>` and HTML blocks.

</div>

---

# Version Control Workflow

1. Store presentation in GitHub  
2. Use pull requests for documentation updates  
3. Export using Marp CLI:  
   ```bash
   marp slides.md --pdf
