---
marp: true
theme: custom-theme
paginate: true
footer: "Ayush Dayal — 23f2001288@ds.study.iitm.ac.in"
---

<!-- Custom Theme -->
<style>
section {
  font-family: "Inter", sans-serif;
}

h1 {
  color: #1e88e5;
}

p {
  font-size: 1.1em;
}

footer {
  color: #777;
  font-size: 0.8em;
}

:root {
  --bg-gradient: linear-gradient(135deg, #1e3c72, #2a5298);
}

section.custom-bg {
  background: var(--bg-gradient);
  color: white;
}
</style>

# Product Documentation  
### Technical Writer: Ayush Dayal  
#### Email: **23f2001288@ds.study.iitm.ac.in**

---

# Overview

- Version-controlled documentation  
- Marp-based slides  
- Exportable to PDF / PPTX / HTML  
- Custom themes & math support  

---

<!-- Slide with Background Image -->
<!-- You may replace the path with a URL or repo asset -->
![bg](https://picsum.photos/1600/900)

# Background Image Slide
### Custom visuals enhance documentation clarity.

---

# Algorithmic Complexity

Using Marp's KaTeX math:

Time complexity of merge sort:

\[
T(n) = 2T(n/2) + O(n)
\]

\[
T(n) = O(n \log n)
\]

---

# Custom Themed Slide
class: custom-bg

# Custom Theme in Action
This slide uses a gradient background from the custom theme.

---

# Version Control Workflow

1. Store docs in GitHub  
2. Use pull requests for updates  
3. Export via Marp CLI  
4. Automate via CI/CD  

---

# Thank You  
### Documentation powered by **Marp + GitHub**
