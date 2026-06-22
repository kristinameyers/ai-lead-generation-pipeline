# 🎯 Autonomous B2B Lead Gen & Enrichment Engine

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://ai-lead-generation-pipeline.streamlit.app/)
[![Powered by Gemini](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-blue)](https://aistudio.google.com/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-green)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Most cold outreach fails because it lacks context. This project introduces a sequential multi-agent execution framework that turns raw business metadata into deeply personalized account strategies.

By chaining three specialized AI subsystems together, the application moves beyond generic templates:

- The Corporate Analyst: Isolates exact market positioning and tech stack realities.

- The Strategy Consultant: Maps out specific executive operational headaches.

- The B2B Conversion Copywriter: Synthesizes the downstream intelligence into a bespoke outreach asset.

---

## 📺 Live Demo & Walkthrough

> [!TIP]
> **Click the thumbnail below** to watch a short video demonstration of this agentic pipeline executing in real-time, displaying structural state handshakes and real-time generation outputs.

[![Watch the Demo](https://img.shields.io/badge/▶_Watch_Video_Demo-Click_To_Play-blueviolet?style=for-the-badge&logo=youtube)](https://youtu.be/qIWdfOG6U5o)

---

## 🧠 Multi-Agent Architecture & Data Handshake

This pipeline avoids bloated, heavy frameworks by utilizing a high-throughput, sequential design built directly on the official, modern `google-genai` SDK. Each agent acts as an isolated operational tier, passing state downstream:

```text
  [Raw Context Input]
          │
          ▼
┌─────────────────────────────────┐
│ 🕵️ Agent 1: Corporate Intel     │ ───► Distills value props, monetization models,
└─────────────────────────────────┘      and core milestones into a structured profile.
          │
          ▼ (Passes Corporate Profile)
┌─────────────────────────────────┐
│ 📐 Agent 2: Persona Architect   │ ───► Diagnoses specific executive operational 
└─────────────────────────────────┘      bottlenecks & anxiety friction points.
          │
          ▼ (Passes Friction Profile)
┌─────────────────────────────────┐
│ ✍️ Agent 3: B2B Copywriter     │ ───► Compiles all data points into zero-fluff,
└─────────────────────────────────┘      highly tailored, short-form outreach copy.
