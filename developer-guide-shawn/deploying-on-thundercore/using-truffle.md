# Using Truffle

> Truffle is a tool that creates a development environment for Ethereum developers to test framework and asset pipeline, compile, deploy and debug for blockchains using EVM.

#### **Setting up Truffle**

Please install the following technical requirements before we start.

* [Node.js v8+ LTS and npm ](https://nodejs.org/en/)(comes with Node)
* [Git](https://git-scm.com)
* [Yarn](https://yarnpkg.com) (optional)

Once we have those installed, we only need one command to install Truffle:

```
npm install -g truffle
# or
yarn global add truffle
```

To make sure Truffle is installed properly, type `truffle version`or `truffle -v`on terminal. If you see an error, make sure your npm modules are added to your path.

> To learn more about setting up Truffle environment, please go to [Truffle tutorial](https://www.trufflesuite.com/tutorial).

#### **Truffle config**

**1. Go to truffle-config.js** 

**2. Update the truffle-config with thunder-testnet-network-crendentials** 

``` javascript=
const HDWalletProvider = require('@truffle/hdwallet-provider');
const fs = require('fs');
let privateKeys;
try {
  privateKeys = fs.readFileSync('.private-keys', {encoding: 'ascii'}).split('\n').filter(x => x.length > 0);
} catch (err) {
    if (err.code === 'ENOENT') {
        privateKeys = null;
    } else {
        throw err;
    }
}
module.exports = {
  plugins: [
    "truffle-plugin-save-per-network-deployment-record"
  ],
  /**
   * Networks define how you connect to your ethereum client and let you set the
   * defaults web3 uses to send transactions. If you don't specify one truffle
   * will spin up a development blockchain for you on port 9545 when you
   * run `develop` or `test`. You can ask a truffle command to use a specific
   * network from the command line, e.g
   *
   * $ truffle test --network <network-name>
   */
  networks: {
    'development': {
      host: "127.0.0.1",
      port: 9545,
      network_id: "5777",
    },
    'thunder-testnet': {
      network_id: 18,
      gasPrice: 20 * 1e9, // 20 gwei, default 100 gwei
      provider: () => {
        if (privateKeys === null) {
          throw (new Error('Create a .private-keys file'))
        }
        return new HDWalletProvider(privateKeys, 'https://testnet-rpc.thundercore.com', 0 /*address_index*/, privateKeys.length/*num_addresses*/);
      },
    },
    'thunder-mainnet': {
      network_id: 108,
      provider: () => {
        if (privateKeys === null) {
          throw (new Error('Create a .private-keys file'))
        }
        return new HDWalletProvider(privateKeys, 'https://mainnet-rpc.thundercore.com', 0 /*address_index*/, privateKeys.length/*num_addresses*/);
      },
    },
    // Useful for testing. The `development` name is special - truffle uses it by default
    // if it's defined here and no other network is specified at the command line.
    // You should run a client (like ganache-cli, geth or parity) in a separate terminal
    // tab if you use this network and you must also set the `host`, `port` and `network_id`
    // options below to some value.
    //
    // development: {
    //  host: "127.0.0.1",     // Localhost (default: none)
    //  port: 8545,            // Standard Ethereum port (default: none)
    //  network_id: "*",       // Any network (default: none)
    // },
    // Another network with more advanced options...
    // advanced: {
      // port: 8777,             // Custom port
      // network_id: 1342,       // Custom network
      // gas: 8500000,           // Gas sent with each transaction (default: ~6700000)
      // gasPrice: 20000000000,  // 20 gwei (in wei) (default: 100 gwei)
      // from: <address>,        // Account to send txs from (default: accounts[0])
      // websockets: true        // Enable EventEmitter interface for web3 (default: false)
    // },
    // Useful for deploying to a public network.
    // NB: It's important to wrap the provider as a function.
    // ropsten: {
      // provider: () => new HDWalletProvider(mnemonic, `https://ropsten.infura.io/v3/YOUR-PROJECT-ID`),
      // network_id: 3,       // Ropsten's id
      // gas: 5500000,        // Ropsten has a lower block limit than mainnet
      // confirmations: 2,    // # of confs to wait between deployments. (default: 0)
      // timeoutBlocks: 200,  // # of blocks before a deployment times out  (minimum/default: 50)
      // skipDryRun: true     // Skip dry run before migrations? (default: false for public nets )
    // },
    // Useful for private networks
    // private: {
      // provider: () => new HDWalletProvider(mnemonic, `https://network.io`),
      // network_id: 2111,   // This network is yours, in the cloud.
      // production: true    // Treats this network as if it was a public net. (default: false)
    // }
  },
  // Set default mocha options here, use special reporters etc.
  mocha: {
    // timeout: 100000
  },
  // Configure your compilers
  compilers: {
    solc: {
      version: "0.4.25",    // Fetch exact version from solc-bin (default: truffle's version)
      docker: false,        // Use "0.5.1" you've installed locally with docker (default: false)
      settings: {          // See the solidity docs for advice about optimization and evmVersion
        optimizer: {
          enabled: true,
          runs: 200
        },
        evmVersion: "byzantium"
      }
    }
  }
}
``` 
connecting to the wallet by ==HDWalletProvider==
If you want to set up your Dapp ,you can export your private keys from your wallet to .private-keys, then you can directly connect to either thunder testnet or mainnet network.


# Deploying on Thunder-testnet or Thunder-mainnet network
Run this command in root of the project directory:

``` 
$ truffle migrate --network thunder-testnet 
$ truffle migrate --network thunder-mainnet

``` 
Contract will be deployed on Thundercore's Testnet or Mainnet, it look like this:
```
2_deploy_contracts.js
=====================

   Replacing 'hellothundercore'
   ------------------
   > transaction hash:    0x1c94d095a2f629521344885910e6a01076188fa815a310765679b05abc09a250
   > Blocks: 5            Seconds: 5
   > contract address:    0xbFa33D565Fcb81a9CE8e7a35B61b12B04220A8EB
   > block number:        2371252
   > block timestamp:     1578238698
   > account:             0x9fB29AAc15b9A4B7F17c3385939b007540f4d791
   > balance:             79.409358061899298312
   > gas used:            1896986
   > gas price:           0 gwei
   > value sent:          0 ETH
   > total cost:          0.0000196026 ETH

   Pausing for 2 confirmations...
   ------------------------------
   > confirmation number: 5 (block: 2371262)
initialised!

   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:                   0.00361367 ETH


Summary
=======
> Total deployments:   2
> Final cost:          0.00418849 ETH
```

**Congratulations!** You have successfully deployed your first ever tt20 token smart contract.

You can check the deployment status at: https://scan-testnet.thundercore.com/(testnet) or https://viewblock.io/thundercore(mainnet) you can check if you have successfully deployed your smart contract by typing the command below in your truffle console. By doing so, you can check the contract address and contract block number you've deployed lately.

