# 🎭 AI Monologue Generator

Welcome to the **AI Monologue Generator**, a research-driven project that explores the intersection of visual art, emotion, and language generation using advanced machine learning techniques. 

This project takes a painting and a set of metadata (title, artist, style, theme, period, field, date, etc.) as input, and generates a **first-person monologue** that imagines what the subject of the painting might say — as if coming to life.

## 🧠 Project Goal

To build a custom multi-modal AI model that learns to generate expressive, emotionally rich monologues conditioned on both image (painting) and text (metadata). Unlike traditional captioning models, this model aims for **artistic storytelling and emotional depth**.

---

## 🧩 How It Works

> **Input:** An image of a painting + metadata  
> **Output:** A generated first-person monologue expressing the painting’s inner voice

The model pipeline includes:
- **Vision Encoder** to extract features from the painting
- **Text Encoder** to process metadata like title, artist, style, genre
- **Fusion Mechanism** to combine visual + textual features
- **Text Decoder** to generate the monologue

---

## 📚 Dataset

This project uses a curated subset derived from the **PainterPalette dataset**, the most extensive public dataset of painters.  
Approximately **261 samples** have been selected, each featuring rich metadata.

Each entry in the dataset includes:

- 🖼️ `Path`: Relative path to the painting image
- 🖊️ `painting_name`: Title of the painting
- 🎨 `Style`: Artistic style (e.g., Surrealism, Cubism)
- 🧑‍🎨 `author_name`: Painter's full name
- 📜 `Genre`: Type of painting (e.g., Mythological, Portrait, Landscape)
- 📚 `Theme`: Key themes associated with the painting
- 🏛️ `Period`: Art period (e.g., Modernism, Renaissance)
- 🖌️ `Field`: Area of art (e.g., painting, sculpture)
- 📅 `Date`: Year of creation

---

## ✅ Current Status

- [x] Dataset selection and cleaning completed
- [x] Project structure and design finalized
- [ ] Model development in progress (encoders, fusion module, decoder)
- [ ] Training and evaluation pipeline (coming soon)

---

## 🤝 Contributing

This is an independent, experimental research initiative.  
If you're passionate about AI storytelling, creative generation, or wish to contribute ideas, datasets, or models — let’s connect!

## 📫 Contact

- Created with curiosity by Christos Loukas Ntais
- 📧 christos.loukas.ntais@gmail.com

---
