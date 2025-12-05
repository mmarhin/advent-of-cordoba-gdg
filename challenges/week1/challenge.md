# Week X: Roman Bridge Stability

Welcome to this week's challenge! Get ready to dive into the engineering and history of one of Córdoba's most iconic monuments.


## 📜 Story: Roman Bridge Maintenance

Córdoba's Roman Bridge, a powerful symbol of the city, has withstood the test of time and the floods of the Guadalquivir river for nearly two millennia. Its resilience is a testament to Roman engineering and the continuous maintenance and restoration efforts throughout the centuries.

You are part of the digital engineering team tasked with monitoring its structure. A recent analysis has generated a list representing the "stability index" of the voussoirs (the key wedge-shaped stones of the arches that bear the weight) along a vital section of the bridge.

Each voussoir has a stability index ranging from **1** (very unstable, risk of collapse) to **10** (perfectly stable). A voussoir is considered **"vulnerable"** if its stability index is strictly less than a predefined `security_threshold` (for example, if the threshold is 4, voussoirs with indices 1, 2, or 3 are vulnerable).

A **"vulnerable section"** is a *contiguous* group of voussoirs where *all* voussoirs within that group are vulnerable. If stable voussoirs separate vulnerable groups, these interruptions mark the end of one vulnerable section and the potential beginning of another.


## 🎯 The Challenge: Count Vulnerable Sections

Given a list of integers (`stabilities`) representing the stability indices of the voussoirs in a part of the bridge, and an integer `security_threshold`, your task is to implement a function that calculates and returns the **total number of vulnerable sections** that exist in that part of the bridge.


## ✍🏼 Examples
Here are some examples to help you test your solution locally. Your code must pass private tests that will be run automatically.

For these examples, we will assume a voussoir is vulnerable if its stability is strictly less than 4 (i.e., indices 1, 2, or 3 are vulnerable).

### Example 1: One vulnerable sections
stabilities = [8, 7, 3, 5, 6, 9]
security_threshold = 4

The vulnerable sections are: [3]
Expected output: 1

### Example 2: Multiple vulnerable sections
stabilities = [8, 7, 3, 2, 5, 1, 1, 1, 6, 4, 3, 9]
security_threshold = 4

The vulnerable sections are: [3, 2], [1, 1, 1], [3]
Expected output: 3
