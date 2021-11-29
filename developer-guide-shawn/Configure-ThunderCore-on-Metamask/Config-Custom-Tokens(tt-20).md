# Config Custom Tokens(tt-20)

## **Deploy Your Own ERC-20**

**ERC20** tokens are one of the most popular DApps in the blockchain community. This tutorial will guide you through deploying an ERC-20 smart contract on ThunderCore in 5 simple steps. It's super easy and fast!

#### **Requirements**

This tutorial expects you to have some basic knowledge of Truffle, Ethereum, Metamask and Solidity.

#### **Install development tools**

Please install the following:

```
Node.js v8+ LTS and npm (comes with Node)
Git
Yarn (optional)
```

Once we have those installed, we only need one command to install Truffle:

```
npm install -g truffle
# or
yarn global add truffle
```

To verify that Truffle is installed properly, type truffle version on a terminal.

#### **Install MetaMask**&#x20;

MetaMask is a browser extension that serves as a “wallet” that safely stores your cryptocurrencies such as Ether (ETH) and Thunder Tokens (TT). It also serves as a “bridge” that connects the web application with the blockchain. You can download and learn more about [Metamask](https://metamask.io).

Get Thunder Tokens or Testnet Tokens to get started, you will need to get Thunder Tokens (Mainnet) or Testnet Tokens (Testnet) to deploy your smart contracts on ThunderCore. Please follow this instruction to get your tokens.

#### **Steps** in this tutorial we will be covering:

* Cloning tt20 repository and installing dependencies
* Updating config file of ERC20 Token
* Compiling and deploying the smart contract on ThunderCore
* Transfering your ERC20 to others

#### **1. Cloning TT20 repository and installing dependencies **

To make it easier to get started with ThunderCore, we've created a ERC20 contract, TT20. You can download the contract with git command.​ On a terminal, input the following command to download the repository

> git clone https://github.com/thundercore/tt20

Next, we'll update the required dependencies for deploying the contract.

```
npm install
# or
yarn install
```

#### **2. Updating config file of ERC20 Token**

Since we've finished the contract already, the only thing we need to do is to update the config file config.json in tt20 folder. The config.json should look like the following:

```
{
    "name": "SampleToken",
    "symbol": "SPT",
    "decimals": 9,
    "initialSupply": 1.5e9
}
```

Change these fields to whatever you want, for example:

```
{
    "name": "MyToken",
    "symbol": "MT",
    "decimals": 8,
    "initialSupply": 1.5e9
}
```

Things to note:

* The name and symbol fields give our token a unique identity.
* The decimals field determines the degree to which this token can be subdivided.
* The initialSupply field determines the number of tokens created when this contract is deployed. In this case, the number is arbitrary. Now, we have our own tokens!

#### **3. Compiling and deploying the smart contract**&#x20;

In the migrations/2\_deploy\_contracts.js, we load the configuration from config.js of ERC20 and deploy the contract. Before we compile and deploy our own ERC20, we can setup a local chain. By using a local blockchain, we can test our contract without consuming real tokens. We recommend using Ganache. Refer to thundercore/ganache and build the Ganache GUI or using the CLI tool thundercore/ganache-cli with the following command.

```
# in tt20 repository
npm install -g thundercore/ganache-cli#tt
```

After install the dependencies of ganache-cli, we can launch a local blockchain with the following command.

```
cd tt20
cd node_modules
cd / .bin
ganache-cli --networkId 5777 -p 9545
```

With our blockchain launched, run the following command to compile and deploy the contract

```
# deploy Token contract to network 'development'
./deploy-contracts --network development
```

You will see output that looks similar to this:

```
Command: [ 'truffle', 'migrate', '--network', 'development' ]
Compiling your contracts...
===========================
> Everything is up to date, there is nothing to compile.


Starting migrations...
======================
> Network name:    'development'
> Network id:      5777
> Block gas limit: 6721975 (0x6691b7)


1_initial_migration.js
======================

   Replacing 'Migrations'
   ----------------------
   > transaction hash:    0x604136ec8bb8d95a819f6f1c962c622583a9c6f2bf91a7616e9a137ab278c6a6
   > Blocks: 0            Seconds: 0
   > contract address:    0xeae24EB27F866225cF6f29370054F7470A94417F
   > block number:        1
   > block timestamp:     1628560607
   > account:             0xa2b543E95EC730A61D40D1cCeb41C68aDe60072c
   > balance:             99.9967579
   > gas used:            162105 (0x27939)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.0032421 ETH


   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:           0.0032421 ETH


2_deploy_token.js
=================

   Replacing 'Token'
   -----------------
   > transaction hash:    0x737c5536c25c44c9cd8a40a8a0c0b25986e2d3d49a4823ea52e7d15c30f66e87
   > Blocks: 0            Seconds: 0
   > contract address:    0x0A7e26D081ffbe772791fC312101210c495b4550
   > block number:        3
   > block timestamp:     1628560608
   > account:             0xa2b543E95EC730A61D40D1cCeb41C68aDe60072c
   > balance:             99.9608271
   > gas used:            1739114 (0x1a896a)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.03478228 ETH


   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:          0.03478228 ETH


Summary
=======
> Total deployments:   2
> Final cost:          0.03802438 ETH
```

Now, your `MyToken` is deployed and mint to your first address in ganache.

With our blockchain launched, run the following command to compile and deploy the contract.

```
# deploy Token contract to network 'development'
./deploy-contracts --network development
```

You will see output that looks similar to this:

```
Command: [ 'truffle', 'migrate', '--network', 'development' ]


Compiling your contracts...
===========================
> Everything is up to date, there is nothing to compile.


Starting migrations...
======================
> Network name:    'development'
> Network id:      5777
> Block gas limit: 6721975 (0x6691b7)


1_initial_migration.js
======================

   Replacing 'Migrations'
   ----------------------
   > transaction hash:    0x604136ec8bb8d95a819f6f1c962c622583a9c6f2bf91a7616e9a137ab278c6a6
   > Blocks: 0            Seconds: 0
   > contract address:    0xeae24EB27F866225cF6f29370054F7470A94417F
   > block number:        1
   > block timestamp:     1628560607
   > account:             0xa2b543E95EC730A61D40D1cCeb41C68aDe60072c
   > balance:             99.9967579
   > gas used:            162105 (0x27939)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.0032421 ETH


   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:           0.0032421 ETH


2_deploy_token.js
=================

   Replacing 'Token'
   -----------------
   > transaction hash:    0x737c5536c25c44c9cd8a40a8a0c0b25986e2d3d49a4823ea52e7d15c30f66e87
   > Blocks: 0            Seconds: 0
   > contract address:    0x0A7e26D081ffbe772791fC312101210c495b4550
   > block number:        3
   > block timestamp:     1628560608
   > account:             0xa2b543E95EC730A61D40D1cCeb41C68aDe60072c
   > balance:             99.9608271
   > gas used:            1739114 (0x1a896a)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.03478228 ETH


   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:          0.03478228 ETH


Summary
=======
> Total deployments:   2
> Final cost:          0.03802438 ETH
```

Now, your **MyToken** is deployed and mint to your first address in ganache.&#x20;

#### **4. Deploy to the ThunderCore Testnet and Mainnet**

Now, you can prepare to deploy your token to ThunderCore testnet or mainnet. Please make sure you have ThunderCore Testnet Token (TST) or ThunderToken (TT). First you set up the control of your account to truffle. You can set either by:

* Write your 12-word mnemonic (seed phrase) to a file named .mnemonic
* Export your account private keys, one per line, to a file named .private-keys

```
# If you use private keys
mv .private-keys.template .private-keys

# in .private-keys file, put your private keys
e59cb5e369b65eee650f90f3280cbe8039db81335943ac7a88df5f4df...
d92a96fa691a7c31b2e2891de05cacc85d562b128afa6bb8f7108aac7...

# If you prefer mnemonic
mv .mnemonic.template .mnemonic

# In .mnemonic file, put your mnemonic
dog cat apple bird ...
```

1. If you use metamask to control your address, you can check how to export the private key here. The address you used will be filled your `MyToken` .
2. Compile and migrate your contract for testnet and mainnet

```
# Deploy to testnet
./deploy-contracts --network thunder-testnet

# or Deploy to mainnet
./deploy-contracts --network thunder-mainnet
```

1. After deploying your own token, `totalSupply` will be added to your accounts. Check out MetaMask to see how to add custom token on MetaMask. The token contract address should be in the stdout after you executed the deployment command.

```
2_deploy_token.js
=================

   Replacing 'Token'
   -----------------
   > transaction hash:    0x737c5536c25c44c9cd8a40a8a0c0b25986e2d3d49a4823ea52e7d15c30f66e87
   > Blocks: 0            Seconds: 0
   > contract address:    0x0A7e26D081ffbe772791fC312101210c495b4550
   > block number:        3
   > block timestamp:     1628560608
   > account:             0xa2b543E95EC730A61D40D1cCeb41C68aDe60072c
   > balance:             99.9608271
   > gas used:            1739114 (0x1a896a)
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.03478228 ETH


   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:          0.03478228 ETH
```

#### **5. Transferring your ERC20 token to others**&#x20;

If you have already added MyToken to your MetaMask, try to send your tokens to other accounts. See more detail on MetaMask doc Note If you try on your local ganache, make sure to set the custom network to your localchain. For exmaple, set rpc url to http://localhost:9545 and chain id 5777. Then you can import private key from ganache to metamask or open a browser without MetaMask (such as incognito window) to see your tokens. Learning more about DApps It’s beyond the scope of this tutorial to go over the code, but if you’d like to learn more about smart contract programming and building DApps in general, we recommend the official Solidity documentation and truffle tutorial. For questions, please join to our Discord channel. Happy Coding! 😆
