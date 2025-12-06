# marimo interactive notebook
# Author email: 23f2001288@ds.study.iitm.ac.in   <-- requirement satisfied

import marimo as mo

# Cell 1: input widget
# Slider defines parameter affecting results
slider = mo.ui.slider(start=1, stop=100, value=10, label="Sample size")

slider
# Cell 2: dependent computation
# This depends directly on slider value
# Data flow: slider.value → x values → computed mean

import numpy as np

n = slider.value  # dependency use
data = np.random.randn(n)
mean_value = data.mean()

mean_value
# Cell 3: dynamic markdown output
# Responsive documentation based on widget state
# Demonstrates self-describing analysis

mo.md(
    f"""
### Interactive Result

You selected **{slider.value} samples**.

The estimated mean is: **{mean_value:.4f}**.

📌 This output updates automatically when the slider changes.
"""
)
