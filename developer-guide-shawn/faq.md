# FAQ

## Technical FAQ <a href="__docusaurus" id="__docusaurus"></a>

### Is ThunderCore compatible with Ethereum? <a href="is-thundercore-compatible-with-ethereum" id="is-thundercore-compatible-with-ethereum"></a>

ThunderCore and Ethereum use the same virtual machine (EVM). As such, smart contracts that run on Ethereum can run on ThunderCore as well, which means that ThunderCore supports languages that Ethereum supports; including Solidity, Vyper, etc.

Furthermore, ThunderCore exposes Ethereum's [JSON RPC](https://github.com/ethereum/wiki/wiki/JSON-RPC), which makes it compatible with tools that use the JSON RPC, such as web3.js, MetaMask, Truffle, etc.

In general, any DApp that runs on Ethereum can be made to run on ThunderCore with very few or minor modifications. Visit the[ tutorial ](integrate-with-thundercore/migrate-from-ethereum.md)on how to migrate from Ethereum to ThunderCore.

### Is ThunderCore decentralized? <a href="is-thundercore-decentralized" id="is-thundercore-decentralized"></a>

Yes, ThunderCore is based on decentralized trust. Users have to trust neither the consensus nodes, nor the accelerator. Users only need to trust the honest majority for ThunderCore to be secure (which is the same for standard blockchains). To understand the consensus algorithm, see the [Whitepaper](https://docs.thundercore.com/thunder-whitepaper.pdf).

### How do I write smart contracts for ThunderCore? <a href="how-do-i-write-smart-contracts-for-thundercore" id="how-do-i-write-smart-contracts-for-thundercore"></a>

Since ThunderCore is compatible with Ethereum smart contracts, you can write smart contracts the same way you would for Ethereum. Most people use Truffle, but other tools should work as well. Check out our tutorial to [deploy your own game](integrate-with-thundercore/deploy-a-dapp.md).

### How do I deploy smart contracts for ThunderCore? <a href="how-do-i-deploy-smart-contracts-for-thundercore" id="how-do-i-deploy-smart-contracts-for-thundercore"></a>

The same way you deploy to Ethereum. Most people use Truffle, but other tools should work as well. See our tutorials on building and [migrating Ethereum DApps ](integrate-with-thundercore/migrate-from-ethereum.md)to ThunderCore.

### What if I already developed a DApp or smart contracts on Ethereum? <a href="what-if-i-already-developed-a-dapp-or-smart-contracts-on-ethereum" id="what-if-i-already-developed-a-dapp-or-smart-contracts-on-ethereum"></a>

Since ThunderCore is compatible with Ethereum, it’s easy to migrate DApps and smart contracts to ThunderCore in just a few steps. Check out our [migrate Ethereum DApps to ThunderCore tutorial](integrate-with-thundercore/migrate-from-ethereum.md).

### How much does it cost to use ThunderCore? <a href="how-much-does-it-cost-to-use-thundercore" id="how-much-does-it-cost-to-use-thundercore"></a>

On the ThunderCore Mainnet, Thunder Tokens (TT) are used to pay gas fees. ThunderCore doesn't rely on an expensive Proof-of-Work (PoW) algorithm and is therefore able to produce blocks at a lower cost.

Get Thunder Tokens (TT) and Testnet Tokens [here](https://thundercore.zendesk.com/hc/en-us/articles/900006700383-Get-Tokens)

### Can I mine or stake Thunder Tokens (TT)? <a href="can-i-mine-or-stake-thunder-tokens-tt" id="can-i-mine-or-stake-thunder-tokens-tt"></a>

ThunderCore utilizes Proof-of-Stake. As such, Thunder Tokens are premined. No new tokens can be mined as we do not mint new tokens as part of our consensus process. ThunderCore validators, called committee node members, earn rewards through gas/txn fees. People can take part in the ThunderCore consensus mechanism and participate in securing the ThunderCore blockchain upon its public launch.

Read more about our Staking Pool Service [here](https://medium.com/thundercore/thundercore-super-node-staking-pool-service-launched-c391c1dbcaff)! Go [here](https://supernode.thundercore.com) now to stake your Thunder Tokens (TT) and earn up to 24% APY.

### How can I get access to ThunderCore?

ThunderCore is a public chain. The ThunderCore Mainnet is easily accessible via the published network addresses found [here](https://developers.thundercore.com/docs/migrate-to-thunder).

### Is ThunderCore available for DApp development? <a href="is-thundercore-available-for-dapp-development" id="is-thundercore-available-for-dapp-development"></a>

Yes. We encourage DApp developers to experience a boost in performance while leveraging full EVM compatibility. DApps can be migrated to ThunderCore in as little as five minutes.

Thunder Tokens are available to individuals and teams desiring to try the ThunderCore Mainnet. The ThunderCore Testnet has been running and available since February 2019 for DApp development. You can get started by obtaining ThunderTokens from the [here](https://thundercore.zendesk.com/hc/en-us/articles/900006700383-Get-Tokens). Please also stay on the lookout for incentives to port your DApps to ThunderCore!

Right now you will have to configure most of the wallets to point to any one of the custom RPC url of ThunderCore:

| RPC | Reference                                                                    |
| --- | ---------------------------------------------------------------------------- |
|     | [https://mainnet-rpc.thundercore.com](https://mainnet-rpc.thundercore.com)   |
|     | [https://mainnet-rpc.thundertoken.net](https://mainnet-rpc.thundertoken.net) |
|     | [https://mainnet-rpc.thundercore.io](https://mainnet-rpc.thundercore.io)     |

### Is Thunder Token an ERC-20 token? <a href="is-thunder-token-an-erc-20-token" id="is-thunder-token-an-erc-20-token"></a>

No, Thunder Token is the native currency of an independent public blockchain, ThunderCore.

ThunderCore is an Ethereum Virtual Machine (EVM) compliant blockchain. Tokens based on the ERC-20 standard can be minted and deployed on ThunderCore.

### What can I do with Thunder Tokens? <a href="what-can-i-do-with-thunder-tokens" id="what-can-i-do-with-thunder-tokens"></a>

Thunder Token is the native currency of an independent public blockchain, ThunderCore. Thunder Token can be used to build and monetize decentralized applications on the ThunderCore blockchain. Thunder Tokens can be used to pay for gas costs, execute transactions and underwrite smart contracts on the ThunderCore blockchain.

### Why is MetaMask showing my tokens as ETH and a large USD amount as its value? <a href="why-is-metamask-showing-my-tokens-as-eth-and-a-large-usd-amount-as-its-value" id="why-is-metamask-showing-my-tokens-as-eth-and-a-large-usd-amount-as-its-value"></a>

When adding a custom RPC URL in MetaMask, MetaMask by default treats any token/coin as ETH and shows the portfolio value using the USD price of ETH.

To correct this, use the "Show Advanced Options" menu when adding the custom URL for Thunder Core ([https://mainnet-rpc.thundercore.com](https://mainnet-rpc.thundercore.com)). Add 108 (0x6c) as Chain ID and TT as the Symbol.

Once you do that your Thunder Tokens will appear as TT on the MetaMask.

### Gas Fees <a href="gas-fees" id="gas-fees"></a>

#### Gas Price <a href="gas-price" id="gas-price"></a>

* Use the [eth\_gasPrice RPC](https://eth.wiki/json-rpc/API) call to get the moving average of recent price

#### Gas Limit <a href="gas-limit" id="gas-limit"></a>

* Use the [eth\_estimateGas RPC](https://github.com/ethereum/wiki/wiki/JSON-RPC#eth\_estimategas) call to estimate the computation and storage cost required by the transaction. If you know for sure the destination address is a regular account and not a smart contract, you can use specify a gas limit of 21 K (21,000)

### How to Prevent Rate Limit? <a href="how-to-prevent-rate-limit" id="how-to-prevent-rate-limit"></a>

* Optimize application program logic and reduce the frequency of query
* Use batch query

### The ability to query ancient states <a href="the-ability-to-query-ancient-states" id="the-ability-to-query-ancient-states"></a>

* Balancing network performance by trading off the ability to query ancient states, such as account balances from months ago. Querying RPC with block numbers may fail if the timestamp of that block was processed a long time ago. Including:
  * eth\_getBalance
  * eth\_getCode
  * eth\_getTransactionCount
  * eth\_getStorage
  * eth\_call

### Address Generation <a href="address-generation" id="address-generation"></a>

* ThunderCore addresses use the same format as Ethereum e.g. 0x519A3B21130Eb8496F7a8E4782fa3106aE4cFF27
* HD Wallet derivation path to obtain private keys from a 12-word mnemonic is (BIP32 Derivation Path): m/44'/1001'/0'/0

| Golang (go-ethereum)                                                                               | Javascript (web3.js)                                                                                                 |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [crtypo.GenerateKey()](https://github.com/ethereum/go-ethereum/blob/v1.9.12/crypto/crypto.go#L193) | [web3.eth.accounts.create()](https://github.com/thundercore/field-support/blob/private-key-to-address/src/key.js#L9) |
|                                                                                                    | [test](https://github.com/thundercore/field-support/blob/private-key-to-address/test/testPrivateKeyToAddress.js#L12) |

### Sending Transactions <a href="sending-transactions" id="sending-transactions"></a>

| Protocol | Transfers                       | References                                                                                                                                                                                                  |
| -------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TT       | Native Cryptocurrency Transfers | See [submitTx()](https://github.com/thundercore/field-support/blob/transfer/src/transfer.js#L29) example [(test)](https://github.com/thundercore/field-support/blob/transfer/test/testTransfer.js#L11)      |
| TT20     | TT20 Token Transfers            | See [transferToken()](https://github.com/thundercore/field-support/blob/transfer/src/transfer.js#L54) example [(test)](https://github.com/thundercore/field-support/blob/transfer/test/testTransfer.js#L13) |

### Where to Ask Questions <a href="where-to-ask-questions" id="where-to-ask-questions"></a>

* For short questions, ThunderCore [Discord](https://discordapp.com/invite/5EbxXfw)
* For longer questions, use the "thundercore" tag on [StackOverflow](https://stackoverflow.com/questions/tagged/thundercore)

### Is your question still not answered? <a href="is-your-question-still-not-answered" id="is-your-question-still-not-answered"></a>

Please get in touch with our team at the [Discord channel](https://discord.gg/5EbxXfw). For urgent support, please contact: [support@thundercore.com](mailto:support@thundercore.com).
