# 🎨 Talk to the Painter – AI Conversations with Famous Artists

Welcome to **Talk to the Painter**, an experimental project that merges the power of conversational AI with the soul of art history.

## 🧠 Project Goal

To build an AI system that lets users **converse with legendary painters** about their artworks — asking questions like:
- *“What inspired this painting?”*
- *“Why are these colors so dark?”*
- *“What emotion were you feeling while creating this?”*

The AI replies in the **persona and voice** of the selected painter, enriched with metadata and biographical context.

---

## 💬 How It Works

> **Input:** User question + selected painting  
> **Output:** Natural AI response from the painter's persona

- 🎯 Painter and artwork selection
- 🧠 Painter persona embedding from biography + metadata
- 🎨 Image and metadata features as context
- 🤖 LLM-based conversational agent

---

## 📚 Dataset

A curated subset from the **PainterPalette Dataset**, featuring:
- ✅ Paintings
- 👨‍🎨 Multiple famous painters
- 🎨 Rich metadata (style, genre, theme, medium)
- 📘 Biographical info from Wikipedia/WikiArt

Painter biographies stored separately in `data/biographies/`.

---

## 📌 Current Status

- [x] Dataset cleaning and selection
- [ ] Biographical enrichment from Wikipedia
- [ ] LLM persona modeling (painter character)
- [ ] Conversational engine development
- [ ] UI/UX prototype (optional frontend)

---

## 🛠 Tools & Stack

- 🧠 GPT or LLaMA for dialogue generation
- 🎨 CLIP for image+text understanding
- 📂 Python + PyTorch
- 🗃️ HuggingFace Datasets or custom CSV loaders
- ✅ Project tracking: Trello + GitHub Issues

---

## 🧪 Sample Use Case

> **User:** “Why did you paint the Minotaur so sad?”  
> **AI (as Picasso):** “That sadness reflects the darkness I felt in 1934… The Minotaur was a symbol of myself.”

---

## 🤝 Contributing

If you're into AI, art, or creative tech — join the conversation!

- 👤 Christos Loukas Ntais  
- 📧 christos.loukas.ntais@gmail.com
