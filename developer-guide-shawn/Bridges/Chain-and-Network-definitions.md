# Chain and Network definitions

### Intro

The ThunderCore bridge allows user to transfer assets between 2 chains in the Ethereum ecosystem. The bridge is a customized version of POA network bridge.

#### **Production asset-transfer bridges**

The following bridges are fully functioned in production environments:

**Ethereum Network** (ThunderCore network to ETH mainnet): Cost effective

**BSC Network** (ThunderCore mainnet to BSC Network): A bridge service providing access to inter-blockchain liquidity for Binance Chain, Binance Smart Chain decentralized applications.

**HECO Network** (ThunderCore mainnet to HECO Network): A decentralized and cost-efficient public chain that Ethereum developers can easily get started with and smart contracts are seamlessly compatible.





A bridge is created between 2 networks, referred to as a Native (or Home) Network and Foreign network.

**Home**: A network with fast and inexpensive operations. This side of bridge collects validator confirmations. **Foreign**: Can be any chain, but generally refers to Ethereum mainnet.

**Bridge components** The bridge consists of several components, including smart contracts, an event handler, and an optional UI. All components are located in the repository.

**TokenBridge**: Listens to events and sends transactions to authorize asset transfers. Bridge UI Application: A DApp GUI to transfer tokens and coins between chains.

**Bridge Monitor**: A tool for checking balances and unprocessed events in bridged networks Bridge Deployment Playbooks: Optional playbook which can manage token-bridge configuration instructions for remote deployments.

**Bridge Smart Contracts**: Manages bridge validators, collects signatures, and confirms assets relay and disposal.
