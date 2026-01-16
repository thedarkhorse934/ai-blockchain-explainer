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

Stage 2: Blockchain Transaction Fetcher

In this stage, I built a Python tool that connects to the Sepolia Ethereum testnet using Web3.py and an Infura RPC URL. The tool:

- Fetches a transaction by its hash
- Retrieves and displays key details including:
- From and To addresses
- Value in Wei
- Gas used
- Block number
- Transaction hash
- Uses a .env file to securely manage API keys, demonstrating best practices for handling secrets

This stage showcases my ability to:

- Programmatically interact with the Ethereum blockchain
- Parse and handle blockchain data in Python
- Write reusable, modular code (fetch_transaction.py as a standalone module)
- Use environment variables for secure API management

Note: This tool was prototyped in Google Colab and then refactored into a modular Python project for portfolio purposes.

---

## Motivation

I built this project to:
- Better understand how to interpret on-chain activity
- Explore practical uses of AI in blockchain tooling
- Create a user-friendly layer on top of raw blockchain data



*This project is tested with web3==6.15.1.


