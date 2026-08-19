# Hey, I'm Shweta Rao 👋

**Product leader building at the intersection of AI, developer platforms, payments, and commerce.**

I started my career as a Java backend developer, which gave me a foundation in systems, APIs, integrations, and data flows. I later moved into product management and have spent 11+ years building products across fintech, payments, eCommerce, and digital experiences.

Most recently, I was a Staff Product Manager at Samsung Electronics America, where I worked on personalization, acquisition, and commerce experiences for the Shop Samsung app. Earlier, I worked on merchant integrations, payments, onboarding, and developer-platform experiences at PhonePe and Financial Data Exchange.

Today, I'm going deeper into AI by **learning through building** — understanding not just how to use LLMs, but how AI applications actually work underneath.

## What I'm building

### 🔎 DevDocs AI — RAG-powered developer documentation assistant

Developers integrating APIs often spend significant time searching documentation, understanding errors, and finding the right implementation guidance.

I'm building **DevDocs AI** to explore how AI can make developer documentation easier to navigate.

The current prototype:

* Ingests and chunks developer documentation
* Creates semantic embeddings using Voyage AI
* Retrieves relevant documentation using cosine similarity
* Provides retrieved context to Claude for grounded answers
* Displays the documentation source
* Uses relevance thresholds to handle unsupported questions

The first implementation uses curated Stripe API documentation covering authentication, PaymentIntents, idempotency, API errors, test/live environments, and webhooks.

`Python` `Claude` `Voyage AI` `RAG` `Embeddings` `Semantic Search`

**Currently exploring:** persistent embeddings, retrieval evaluation, multi-document retrieval, vector databases, source attribution, and developer-feedback loops.

---

## What I'm learning

I'm working through the AI application stack from first principles:

`LLM APIs` → `Prompting` → `Memory` → `Embeddings` → `Retrieval` → `RAG` → `Vector Databases` → `Evaluation` → `Agents`

I document what I build, what breaks, and what I learn along the way.

---

## Background

* **Software Engineering** — Java/backend systems
* **Fintech & Payments** — APIs, merchant integrations, onboarding, payment experiences
* **Commerce** — acquisition, personalization, conversion, and customer journeys
* **Developer Platforms** — API integrations and developer experiences
* **AI** — currently building hands-on applications and learning the underlying systems

---

## Why I'm building in public

AI concepts became much clearer to me once I stopped only reading about them and started building them.

My goal is to understand AI deeply enough to **build it, explain it, evaluate it, and make better product decisions around it**.

This GitHub documents that journey.
