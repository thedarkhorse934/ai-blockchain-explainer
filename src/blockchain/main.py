# ===============================
# 1. Install and import dependencies
# ===============================
!pip install web3

import os
from web3 import Web3
from web3.types import TxParams
from dotenv import load_dotenv

# ===============================
# 2. Load environment variables
# ===============================
# Make sure you have a .env file in the Colab working directory with:
# PRC_URL="https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID"

load_dotenv()  # load variables from .env
RPC_URL = os.getenv("PRC_URL")

if RPC_URL is None:
    raise ValueError("RPC_URL not found in environment variables")

# ===============================
# 3. Connect to Web3
# ===============================
w3 = Web3(Web3.HTTPProvider(RPC_URL))

if not w3.is_connected():
    raise ConnectionError("Web3 failed to connect to the Sepolia node")
print("Connected to Web3:", w3.is_connected())

# ===============================
# 4. Helper function (fetch_transaction)
# ===============================
def fetch_transaction(tx_hash: str):
    """
    Fetch a transaction from Sepolia by its hash
    Returns: AttributeDict of transaction details
    """
    try:
        tx = w3.eth.get_transaction(tx_hash)
        return tx
    except Exception as e:
        print("Error fetching transaction:", e)
        return None

# ===============================
# 5. Fetch a transaction
# ===============================
# Replace this with any real Sepolia transaction hash
tx_hash = "0x20c4b5ac97f191a7d7e2859766306dd95c60a8d580afdcb6b990b8b5b6723231"

tx = fetch_transaction(tx_hash)

if tx is None:
    print("Failed to fetch transaction")
else:
    print("Transaction fetched successfully!\n")
    # ===============================
    # 6. Print basic info
    # ===============================
    print("From:", tx["from"])
    print("To:", tx["to"])
    print("Value (wei):", tx["value"])
    print("Gas:", tx["gas"])
    print("Gas Price (wei):", tx["gasPrice"])
    print("Block Number:", tx["blockNumber"])
    print("Transaction Hash:", tx["hash"].hex())
    print("Input (first 100 chars):", tx["input"][:100] + "..." if tx["input"] else "")
