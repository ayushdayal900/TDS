---
marp: true
theme: custom
paginate: true
footer: "23f2001288@ds.study.iitm.ac.in"
---

<!-- Define a custom theme via style -->
<style>
/* Custom theme variables */
:root {
  --color-background: #f5f7fa;
  --color-accent: #1976d2;
  --color-text: #333;
}

section {
  background: var(--color-background);
  font-family: "Inter", sans-serif;
  color: var(--color-text);
}

h1 {
  color: var(--color-accent);
}

.custom-bg {
  background: url('https://picsum.photos/1600/900') center/cover no-repeat;
  color: white;
}
</style>

# Product Documentation  
### Prepared by: Ayush Dayal  
### Email: **23f2001288@ds.study.iitm.ac.in**

---

# Version-Controlled Documentation

- Stored in GitHub  
- Easy collaboration  
- Converts to PDF, PPTX, HTML using Marp CLI  
- Theme-based styling  

---

<!-- Slide with Background Image -->
<!-- Marp background directive -->
<!-- We use a class here to ensure compatibility -->
<section class="custom-bg">

# Background Image Slide  
Enhances visual clarity and engagement.

</section>

---

# Mathematical Example

Time complexity of Merge Sort:

\[
T(n) = 2T\left(\frac{n}{2}\right) + O(n)
\]

\[
T(n) = O(n \log n)
\]

---

# Custom Themed Slide

<section style="background: linear-gradient(135deg, #1565c0, #42a5f5); color: white; padding: 50px;">

# Custom Gradient Theme  
This slide uses custom inline Marp styling.

</section>

---

---
marp: true
theme: default
paginate: true
footer: "23f2001288@ds.study.iitm.ac.in"
---

# Product Documentation

---

---
background: "https://picsum.photos/1600/900"
---

# Background Image Slide
This slide uses a YAML `background:` directive.



# Summary

- Marp enables version-controlled documentation  
- Custom themes improve maintainability  
- CLI exports PDFs for release notes  
- Backgrounds & equations improve clarity  
---

# Thank You  
### Documentation Powered by **Marp + GitHub**
