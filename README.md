# AI Blockchain Explainer 🤖🧩

An AI-assisted tool that explains Ethereum transactions and smart contracts in plain English.

This project bridges raw on-chain data with human-readable explanations by combining blockchain data parsing with a Large Language Model (LLM).

---

## Overview

Blockchain data is powerful but difficult to interpret without technical knowledge.  
This project fetches real on-chain data (transactions, events, contract details) and uses AI to generate clear explanations that are easy to understand.

---

## Features (Planned)

- Explain Ethereum transactions from a transaction hash
- Detect ETH and ERC-20 transfers
- Summarize contract interactions
- Highlight notable or privileged actions
- Plain-English AI explanations

---

## Tech Stack

- **Blockchain:** Ethereum (Sepolia testnet)
- **On-chain access:** RPC provider (e.g. Infura / Alchemy)
- **AI:** LLM API (e.g. OpenAI)
- **Backend:** Python or Node.js (to be decided)

---

## How It Will Work

1. User provides a transaction hash
2. Backend fetches transaction + receipt data
3. Relevant events and actions are extracted
4. Structured data is passed to an LLM
5. AI returns a clear explanation of what happened

---

## Project Status

🚧 This project is under active development.  
Initial focus is on transaction explanation before expanding to contract and wallet analysis.

---

## Motivation

I built this project to:
- Better understand how to interpret on-chain activity
- Explore practical uses of AI in blockchain tooling
- Create a user-friendly layer on top of raw blockchain data

