


# Getting started: developing on Thundercore blockchain

[TOC]

###### tags: `developer guide`

----

## Overview

Welcome to the most exciting and state-of-the-art platform to build your blockchain application on ThunderCore Blockchain. If you are an Ethereum developer, developing on ThunderCore should be seamless and smooth as ThunderCore is fully Ethereum Virtual Machine (EVM) compatible and inherits most of the tools and libraries from Ethereum.


This page acts as a quick guide into the ThunderCore developer platform. You will find links to some useful resources and websites to set you off on the journey of building applications on ThunderCore.
Feel free to reach out to us on Telegram/Discord when you need any help!

** Developer quick start**

* Since ThunderCore is a fork of geth, our blockchain natively supports EVM compatible smart contracts. The following briefly describes the steps required to develop on ThunderCore.
* Setup Metamask Wallet or other web wallet
* Deploy your contracts on ThunderCore

   * Using Remix
   * Using Truffle
   * Using Hardhat Connecting to Thundercore with RPC by adding ThunderCore on Metamask.



**Already have a Dapp?**
* Migrate from Ethereum chain or other EVM based chain

    As long as it’s EVM compatible, you are all set!
    Deploying your Dapp on Thundercore  ==--->hyperlink to integration page==

* ####  Using Thundercore as a faster transaction layer

    Using Thundercore as a transaction layer in your DApp deployed on Mainnet, you can get started with getting your tokens mapped by us.


**Building a new Dapp on ThunderCore?**

#### Overview
  Let's use 5-10 minutes to deploy a complete game through ThunderCore that is easily accessible to your own friends and family -- accessible to anyone with internet access. We will release a simple coin toss game where players will receive twice as many bets if the coin is facing up. In the case of coins facing down, players will lose their bets, but still have a chance to double the bet.

#### Exploring the Game
To begin, we will obtain a wallet and gain access to the Thunder network. With either Metamask or TrustWallet pointed to the Thunder RPC, navigate [HERE](https://thundercore.github.io/DoubleOrNothing/) to play the game we will build in this tutorial!

![](https://i.imgur.com/IbBIWXd.png)

To make your own version of the page, just check out the [repo](https://github.com/thundercore/DoubleOrNothing) and follow the instructions in the readme.

At the end of those instructions, you should be able to access the game with either your mobile device through Metamask or any ThunderCore compatible mobile DApp browsers.

#### Deploying Your Own Contract

Now, let's get your game running on your own copy of the contract, so you can get started developing your own killer DApp!

First we will install all the dependencies.
```
node -v
# Let's make sure our node is v8 or v10
```

If you haven't downloaded node.js, go to [node.js](https://nodejs.org/en/download/) download the version 8 or version 10.
If you have downloaded it before but your version is incompatible, install it with [nvm](https://github.com/nvm-sh/nvm), and follow the instructions below.
```
nvm install [v8 or v10]
nvm use [v8 or v10]

node -v  #Make double check our node is v8 or v10 (recommend node version:10.24.1)
```
* [references---how to change to an old version of node.js](https://stackoverflow.com/questions/7718313/how-to-change-to-an-older-version-of-node-js)

```
cd ./smart-contracts
yarn install

# or
npm install
```
Next grab your mnemonic or  import your private key from metamask and create a file called .private-keys under  “./smart-contracts ” or Trust Wallet and add it to the HDWallet in truffle-config.js
```
testnet
yarn migrate --network thunder-testnet --reset
# or
npm run migrate -- --network thunder-testnet --reset
```
```
mainnet
yarn migrate --network thunder-mainnet --reset
# or
npm run migrate -- --network thunder-mainnet --reset
```
In the console, you will see the price you've paid for its deployment, the contract address, and additional stats. Well done! Your contract is now up and running ready to be used by anyone.
If the contract address of DoubleOrNothing didn’t show up in the console after the migration ,you can check the contract address by typing the command below.
```
mainnet
$ Truffle console --network thunder-mainnet
testnet
$ Truffle console --network thunder-mainnet

let contract = await DoubleOrNothing.deployed()
DoubleOrNothing.address
```
To make sure you've deployed doubleOrNothing smart contract successfully,you can double check the ==contract address== and ==contract block number== you've deployed lately.
* testnet
``` javascript=
truffle(thunder-testnet)>let contract = await DoubleOrNothing.deployed()
truffle(thunder-testnet)> DoubleOrNothing.address
'0x48caD7fe30Fd1CA52EcBda9C82E398B0FFd321eE'
truffle(thunder-testnet)> n = web3.eth.getBlockNumber();
62591612


```
* mainnet

``` javascript=
truffle(thunder-mainnet)>let contract = await DoubleOrNothing.deployed()
truffle(thunder-mainnet)> DoubleOrNothing.address
'0x8693A164EBC4429fCFF4461B481FCD4E60690fD3'
truffle(thunder-mainnet)> n = web3.eth.getBlockNumber();
83540251

```

We must now update our UI to use this contract address.
```
cd ./frontend
```
```
yarn install
# or
npm install
```
Find the .env file and change the **REACT_APP_CONTRACT_ADDRESS** to your new address which you got by the command **DoubleOrNothing.address** above.

Meanwhile, change **REACT_APP_TT_USDT_CONTRACT** to 0xB1Fb0b14Ffea209ABa1e62ff3F2F3DFD2eaa9FE0,
    and comment out another REACT_APP_TT_USDT_CONTRACT address.
If you’re not sure of the REACT_APP_TT_USDT_CONTRACT testnet or mainet address , check it on [thundercore bridge](https://bridge-venus.thundercore.com/eth/ ).

Below are the specific steps we mentioned above.


First of all, click on the option above.Next, click the info symbol below
![](https://i.imgur.com/RNRzYiF.png)

![](https://i.imgur.com/Y0yZiw9.png)
You can see the **TT-USDT ADDRESS** ,which is **REACT_APP_TT_USDT_CONTRACT**=0xB1Fb0b14Ffea209ABa1e62ff3F2F3DFD2eaa9FE0

![](https://i.imgur.com/XRGHrV4.png =x300)

```
yarn start
# or
npm run start
```

This will start a local server with your changes.
If you want to deploy this to your webpage run:
```
yarn build
# or
npm run build
```
```
git add -u

*Remember to not check in your mnemonic!!!!
```
```
git commit -m 'add my own contract address'
```
```
git push
```
Voila! In 5-10 seconds, your webpage will be running on your contract. Congratulations!
**Debugging: Add a Console to display an Error Message in the DApp**
Add a console in the DApp’s UI when running in the ThunderCore Hub Wallet’s Browser Tab to display any error messages for problems/errors encountered while interacting with the chain.
Example 1: [TT20 Transactions](https://github.com/thundercore/hubbit-field-support/blob/c69d3798f77fd07d8b3f0381b5a0dc78addd0691/src/index.js#L172)
Example 2: [DoubleOrNothing](https://github.com/thundercore/DoubleOrNothing/commit/8d5e755876f77f309937b31791ae246b4826566a#diff-1a2294bec8f8b96cd516ecd00ef9f3c8R135)

---
### Learn the developer tools
* [Truffle suite docs](https://www.trufflesuite.com/docs)
* [Truffle tutorial](https://www.trufflesuite.com/tutorial)
* [Remix](https://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.7+commit.e28d00a7.js)
* [Hardhat](https://hardhat.org/tutorial/)

**Learn the basics of development**

>* [Dapp University](https://www.dappuniversity.com/)
>* [Truffle tutorial](https://www.trufflesuite.com/docs/truffle/quickstart)
>* [cryptozombies tutorial](https://cryptozombies.io/)
>* Full stack DApp tutorial series
>* What is Ethereum?

**Keeping up with development**
Thundercore's twitter, telegram, discord account?

---

##  Developing on ThunderCore

----

### Using Remix

> Remix is a web-based IDE for writing, compiling, and deploying contracts.

**Setting up Remix IDE**
Visit [Remix](https://remix.ethereum.org/) to access the Remix IDE from your web browser.

Note: If this is your first time using Remix, you must locate and activate the "Solidity Compiler" plug-in, as shown in below <insert a picture>
1. Go to File explorers
2. Create a new file, name it
3. Copy & paste the Smart contract below into the newly created file

    ![](https://i.imgur.com/QqhqhLY.png)


**The smart contract**
1. Create new contract TT20Token.sol and copy contract code from the TT20 token template here<ins a link>
2. Modify "name","symbol","decimals",and "totalSupply" based on your requirements
![](https://i.imgur.com/qVRXeWt.png) --> need to change this picture

The first line, `pragma solidity^0.5.16`tells the Solidity version greater than 0.5.16.

A contract in Solidity is a collection of code (its functions) and data(its state) that resides at a specific address on the Ethereum blockchain.

**Compile smart contract**
1. Click button to switch to compile page
2. Select "TT20Token" contract
3. Enable "Auto compile" and "optimization"
4. After successful compilation, it will show ![](https://i.imgur.com/ZxQmr0Q.png)

4. Click "ABI" to copy the contract ABI and save it
![](https://i.imgur.com/ROOpYRn.png) --> need to change this picture

Let's deploy your smart contract on ThunderCore Network. To do so we need to connect to web3 world, which can be done by using services like Metamask, Brave and Portis etc.
We will be using Metamask to connect to web3 world. Please follow the tutorial to setup a Metamask Account.<insert link of configure ThunderCore on wallets>.

1. Open Metamask and select custom RPC from the network dropdown
2. Go to Setting page
![](https://i.imgur.com/uPlP8V0.png)
3. Add a new network
4. Put in a Network name - "Thundercore Testnet"
5. Put new RPC URL - "https://testnet-rpc.thundercore.com"
6. Put chain ID
    * "108"(MAINNET)
    * "18"(TESTNET)

7. Put currency symbol
    * "TTM"(MAINNET)
    * "TTT"(TESTNET)

8. Put block explorer URL - "https://scan-testnet.thundercore.com/"
9. Click save
---> may need to change the screenshots

![](https://i.imgur.com/u24taPM.png)

![](https://i.imgur.com/LLQhOWz.png)

10. Click on the account name just below the main address line will copy your address to the clipboard.
 ![](https://i.imgur.com/T72MECM.png)
11. Go to https://faucet-testnet.thundercore.com/ to request test TT
12. Deploy the smart contract on ThunderCore testnet
13. Select Injected Web3 in the Environment dropdown and your contract
![](https://i.imgur.com/gNuy6qt.png) --->need to change this picture
14. Accept the connection request
![](https://i.imgur.com/4ShBUmD.png)
    --->need to chage this picture
15. Once Metamask is connected to Remix, the 'Deploy' transaction would generate another Metamask popup that requires transaction confirmation
![](https://i.imgur.com/Ihl0rDW.png)
    --->need to change this picture

16. **Yay!** you have successfully deployed your smart contract. Check the deployment status here: https://scan-testnet.thundercore.com/

----
### Using Truffle

> Truffle is a tool that creates a development environment for Ethereum developers to test framework and asset pipeline, compile, deploy and debug for blockchains using EVM.

**Setting up Truffle**

Please install the following technical requirements before we start.

* [Node.js v8+ LTS and npm ](https://nodejs.org/en/)(comes with Node)
* [Git ](https://git-scm.com/)
* [Yarn](https://yarnpkg.com/) (optional)

Once we have those installed, we only need one command to install Truffle:
```
npm install -g truffle
# or
yarn global add truffle
```

To make sure Truffle is installed properly, type `truffle version`or `truffle -v`on terminal. If you see an error, make sure your npm modules are added to your path.

> To learn more about setting up Truffle environment, please go to [Truffle tutorial](https://www.trufflesuite.com/tutorial).

**Truffle config**

**1. Cloning TT20 repository and installing dependencies**
To make it easier to get started with ThunderCore, we've created a ERC20 contract, [TT20](https://github.com/thundercore/tt20). From the TT20 github you can download the contract with git command.

On a terminal, input the following command to download the repository
```
git clone https://github.com/thundercore/tt20
```
Next, we'll update the required dependencies for deploying the contract.
```
npm install
# or
yarn install
```
**2. Updating config file of ERC20 Token**
Need to updated the config file `config.json` in tt20 folder.
The `config.json`should look like the following:
```
{
    "name": "SampleToken",
    "symbol": "SPT",
    "decimals": 9,
    "initialSupply": 1.5e9
}
```
Change these fields to fit your needs, for example:
```
{
    "name": "MyToken",
    "symbol": "MT",
    "decimals": 8,
    "initialSupply": 1.5e9
}
```

Note:
* The `name` and `symbol` fields give our token a unique identity.
* The `decimals` field determines the degree to which this token can be subdivided
* The `initialSupply `field determines the number of tokens created when this contract is deployed. In this case, the number is arbitrary.


**3. Compiling and deploying the smart contract**
1. In the `migrations/2_deploy_contracts.js`, we load the configuration from `config.js` of ERC20 and deploy the contract.
2.Before we compile and deploy our own ERC20, we can setup a local chain. By using a local blockchain, we can test our contract without consuming real tokens. We recommend using [Ganache](https://github.com/thundercore/ganache). Refer to thundercore/ganache and build the Ganache GUI or using the CLI tool [thundercore/ganache-cli](https://github.com/thundercore/ganache-cli) with the following command.
```
# in tt20 repository
npm install -g truffle thundercore/ganache-cli #tt
```
After install the dependencies of ganache-cli, we can launch a local blockchain with the following command.
```
cd tt20
cd node_modules
cd / .bin
cd ganache-cli --networkId 5777 -p 9545
```
3. With our blockchain launched, run the following command to compile and deploy the contract
```
# deploy Token contract to network 'development'
./deploy-contracts --network development
```
You will see output that looks similar to this:
``` <!DOCTYPE html>
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
Now, your ```MyToken``` is deployed and mint to your first address in ganache.



**Deploy to the Thundercore network**
Now, you can prepare to deploy your token to ThunderCore testnet or mainnet. Please make sure you have ThunderCore Testnet Token (TST) or ThunderToken (TT)

1.First you set up the control of your account to truffle. You can set either by:

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
If you use metamask to control your address, you can check how to export the private key here. The address you used will be filled your ```MyToken```.


2.Compile and migrate your contract for testnet and mainnet
```
# Deploy to testnet
./deploy-contracts --network thunder-testnet

# or Deploy to mainnet
./deploy-contracts --network thunder-mainnet

```
After deploying your own token, totalSupply tokens will be added to your accounts. Check out MetaMask to see how to add custom token on MetaMask.

The token contract address should be in the stdout after you executed the deployment command.
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


**Congratulations!** You have successfully deployed your first ever tt20 token smart contract.

You can check the deployment status at: https://scan-testnet.thundercore.com/
or you can check if you have successfully deployed your smart contract by typing the command below in your truffle console.
By doing so, you can check the ==contract address== and ==contract block number== you've deployed lately.
* testnet
``` javascript=
truffle(thunder-testnet)>let contract = await DoubleOrNothing.deployed()
truffle(thunder-testnet)> DoubleOrNothing.address
'0x48caD7fe30Fd1CA52EcBda9C82E398B0FFd321eE'
truffle(thunder-testnet)> n = web3.eth.getBlockNumber();
62591612


```
* mainnet

``` javascript=
truffle(thunder-mainnet)>let contract = await DoubleOrNothing.deployed()
truffle(thunder-mainnet)> DoubleOrNothing.address
'0x8693A164EBC4429fCFF4461B481FCD4E60690fD3'
truffle(thunder-mainnet)> n = web3.eth.getBlockNumber();
83540251

```






----
### Using Hardhat   (include create a project steps?)
> Hardhat is a developement environemnt tool that helps developers to test, compile, deploy, and debug your Ethereum software.

**Setting up Hardhat**
There are a few technical requiements before we start. Please install the following:

* Node.js v10+ LTS and npm --->needs a hyperlink
* Git --->needs a hyperlink

Once we have those installed, we then install Hardhat.

To install it, you need to create an npm project by going to an empty folder, running `npm init`, and following the instructions. When the project is ready, run the code:
```
npm install --save-dev hardhat
```
Let's try to create a sample project to compile, test, and depoly sample contract.
To learn more about the sample contract [in this guide.](https://hardhat.org/getting-started/#installation)

**Hardhat config**
1. Go to hardhat.config.js
2. Update tne hardhat config with thundercore network credential
3. Create .env file in the root to store your private key
``` javascript=
require("@nomiclabs/hardhat-ethers");
const fs = require('fs');
const privateKey = fs.readFileSync(".secret").toString().trim();
module.exports = {
  defaultNetwork: 'thunder-testnet',
  networks: {
    'thunder-testnet': {
      url: 'https://testnet-rpc.thundercore.com',
      chainId: 18,
      gas: 30000000,
      gasPrice: 1000000000,
      accounts: [
        '0xPrivateKey',
      ],
    },
    'thunder-mainnet': {
      url: 'https://mainnet-rpc.thundercore.com',
      chainId: 108,
      gas: 30000000,
      gasPrice: 1000000000,
      accounts: [
        '0xPrivateKey',
      ],
    },
  },
  solidity: {
    // ... solc 版本到最新也可以，隨意
    evmVersion: 'byzantium', // 這邊一定要設定成拜占庭，直到我們升版
  },
  // ...
}
```

**Deploy on Thundercore Network**

Run the command in root of the project directory:
```
$ npx hardhat run scripts/sample-script.js --network thundercore
```
Contract will be deploy on Thundercore's testnet, which looks like:
```
Compilation finished successfully
Greeter deployed to: 0xfaFfCAD549BAA6110c5Cc03976d9383AcE90bdBE
```
---> need to change the address

> The address would be different, the above is just to proivde an idea of the structure.

**Congrats!** You have successfully deployed TT20 smart contract. Go ahead and interact with the smart contract!

You can check the deployment status here: https://scan-testnet.thundercore.com/


---
## Network details

### Thundercore Mainnet
The documentation corresponding contains details for the RPC - HTTP, and WS. There is also a full node setup if you wish to setup your own full node.

| Network name | ThunderCore Mainnet|
| -------- | -------- |
| Gas token | TT token  |
| RPC       | ThunderCore blockchain: https://mainnet-rpc.thundercore.com <br /><br /> Use these alternative RPCs only if the above RPC fails: <br />https://mainnet-rpc.thundertoken.net/ or <br />https://mainnet-rpc.thundercore.io/ or <br /> https://zeus-rpc.thundercore.com/ or <br /> https://zeus-rpc.prod.tt-eng.com/<br /> <br />
| Websocket |https://mainnet-ws.thundercore.com or <br />https://zeus-ws.thundercore.com/  or <br />https://zeus-ws.prod.tt-eng.com/ <br /> `wss://mainnet-ws.thundercore.com`<br /><br />
| Block Explorer| https://scan.thundercore.com/ |


>Important: Thundercore network native token is TT, which will be used as gas fee

---
### ThunderCore Testnet
The ThunderCore testnet is an alternative of ThunderCore mainnet, which is to be used for testing and experimenting smart contracts. Testnet tokens not only are saparated from mainnet tokens, they should never have any value.

The following contains details for the RPC - HTTP, and WS. There is also a full node setup if you wish to setup your own full node.

| Network name | ThunderCore Testnet|
| -------- | -------- |
| Gas token | TST token  |
| RPC       |ThunderCore Testnet: https://testnet-rpc.thundercore.com
| Websocket |`wss://testnet-ws.thundercore.com `
| Block Explorer| https://scan-testnet.thundercore.com/ |

---
### Mapped Tokens
**Mainnet**
**Testnet**
---
### Genesis contracts
**Mainnet**
**Testnet**
---
### Full node deployment
**Mainnet**
**Testnet**
---
##  Tools

### Faucet

Mainnet Thunder Token Faucet: https://faucet.thundercore.com/

Testnet Thunder Test Token Faucet: https://faucet-testnet.thundercore.com/

---

### Random number generator
**Summary**

The ThunderCore blockchain supports generating cryptographically secure 256-bit random numbers through a Thunder trusted random number generating pre-compiled contract.

**Motivation**

When developing smart contracts for Ethereum, developers do not have built-in support for generating cryptographically secure random numbers. While there are some possible solutions (e.g. using Ethereum Alarm r Oraclize), these solutions often rely on external services and are not scalable. To address this need, ThunderCore has implemented built-in support to generate cryptographically secure random numbers through a pre-compiled contract.

**Specification**
ThunderCore has implemented a pre-compiled contract which resides at address `0x8cC9C2e145d3AA946502964B1B69CE3cD066A9C7`. This address is the first 20 bytes of `sha256("Thunder_Random")`. Each invocation of fallback function of trusted random generator pre-compiled contract will return a 256-bit rnadom number. The gas cost for each invocation is `26134`. The invocation is the same as calling Ethereum pre-compiled contracts. Below is an example which can be embedded into a smart contract. ThunderCore also provides a library which can be sued in Remix with `import "github.com/thundercore/RandomLibrary/RandomLibrary.sol` from Github with URL in Remix. The random number generator will always return a `bytes32` value, so you will need to cast or convert this value as it suits your needs.
``` solidity=
function rand() internal returns (uint256) {
    uint256[1] memory m;
    assembly {
        if iszero(call(not(0), 0x8cC9C2e145d3AA946502964B1B69CE3cD066A9C7, 0, 0, 0x0, m, 0x20)) {
            revert(0, 0)
        }
    }
    return m[0];
}
```
**Example**
In the basic example shown below, random number is used to determine whether the contract will pay the user. If the number is greater than the bet from the user, the contract takes the user's wager. If not, the contract pays the user their own bet plus 1.

> Note: the `require(msg.sender == tx.origin)` check in `bet()` is necessary for security and explained below.
``` solidity=
pragma solidity ^0.4.25;

import "github.com/thundercore/RandomLibrary/RandomLibrary.sol";
contract RandomExample {
    event UserWon(bool, uint256, uint256);

    constructor() payable public {
    }

    function bet(uint256 v) payable external returns (bool) {
        // block calls from other contracts to prevent "revert transaction unless I won" attacks
        require(msg.sender == tx.origin);

        if (msg.value < 5) {
            emit UserWon(false, 0, 0);
            return false;
        }
        uint256 randomNumber = LibThunderRNG.rand();
        if (v < randomNumber) {
            msg.sender.transfer(msg.value+1);
            emit UserWon(true, v, randomNumber);
            return true;
        }
        emit UserWon(false, v, randomNumber);
        return false;
    }
}
```
**How to prevent Revert the Transaction Unless I Won attacks**
There's a conceptually simple approach to attack any game of chance on EVM compatible block chains. The attacker would deploy a contract and do something like:
1. Play game of chance
2. Check if balance in the attacker's contract decreased after teh game
3. Revert the transaction if the contract balace decreased

In Solidity, the attack would look like:

```solidity
    function attack(uint256 v) public  {
        uint256 pool = this.balance;
        /* play game of chance ... */
        require(this.balance >= pool);
    }
```


Add a `require(msg.sender == tx.origin)` check at the begining of your `bet` function prevents other contracts from calling your own and thus blocks the attack. See the [Block and Transaction Properties](https://docs.soliditylang.org/en/v0.4.25/units-and-global-variables.html#block-and-transaction-properties) section in [Solidity in Depth](https://docs.soliditylang.org/en/v0.4.25/solidity-in-depth.html) for details:
* `msg.sender``(address)`: sender of the message (current call)
* `tx.origin``(address)`: sender of the transaction (full call chain)

---
### Oracles
---

### Referral Library

Referral is one of the most effective form of marketing to get more users. Lots of popular DApps such as Fomo3d, MyCrypto Heroes, HyperSnake, as well as many others use referral mechanisms to drive success.

Hence, we built a referral library: [Referral Solidity](https://github.com/thundercore/referral-solidity), to help DApp developers to quickly build their own referral mechanisms. In this document we will share how to use our library.

**Referral Solidity Library**
Check out our basic multi-level referral: https://github.com/thundercore/referral-solidity/. With this library, you can have the following features in minutes:
* Up to three levels of referral system with native token (ETH,TT...)
* Pay referral bonus based o referee amount
* Pay intantly when downline joins
* Only active users will get the referral bonus

**How to use**
First, install our library with the following command.
```
npm install @thundercore/referral-solidity
```
Then, integrate referral solidity with your DApp by importing, initializing, binding referral relationship with `addReferrer` function and trigger referral payment by `payReferral`.
``` solidity=
pragma solidity ^0.5.0;
import '@thundercore/referral-solidity/contracts/Referral.sol';

contracts YourGame is Referral {
  // Referral(decimals, referralBonus, secondsUntilInactive, onlyRewardActiveReferrers, levelRate, refereeBonusRateMap)
  constructor() Referral (10000, 500, 1 days, true, [6000, 3000, 1000], [1, 10000]) public {
  }

  // bind uplineAddr as msg.sender's referrer
  function addUpline(address payable uplineAddr) public {
    addReferrer(upline);
  }

  // trigger pay referral in your business logic
  function play() public payable {
    payReferral(msg.value);
  }
}
```
In the line of `constructor() Referral (10000, 500, 1 days, true, [6000, 3000, 1000], [1, 10000])`. You may be confused what those parameters mean, thus please refer to the explanation for the parameters below:
```
Referral(decimals, referralBonus, secondsUntilInactive, onlyRewardActiveReferrers, levelRate, refereeBonusRateMap)
```
**decimals** `<unit>`
Base decimals for all rate calculation in referral. For example. if `decimals`equals to `10000`, and `referralBonus` is `500`, that means the referral bonus rate is `5%`.

**referralBonus**`<unit>`
The total referral bonus rate, which will be divided by `decimals`. For example, if you will like to set a rate of `5%`, then set `referralBonus` as `50` when `decimals` is `1000`.

**secondsUntilInactive**`<unit>`
How long, in seconds, a user will be inactive. For example, `one days`.

**onlyRewardActiveReferrers**`<bool>`
The flag to enable whether not to pay inactive uplines.

**levelRate**`<uint[]>`
The bonus rate for each level, which will be divided by decimals. The max level depth is 3. For example, set levelRate as` [6000,3000,1000]` when `decimals` is `10000` for the following case:

|| Level 1 | Level 2 | Level 3|
| -------- | -------- | -------- |-------- |
| Rate     | 60%    | 30%     |10%         |



**refereeBonusRateMap**`<uint[]>`
The bonus rate mapping to each referree amount will be divided by decimals too. The max depth is 3. the map should be passed as [`<lower amount>`,`<rate>`,...]. For example, you should pass `[1, 2500,5,5000,10,10000]` when decimals is `10000` for the following case:

|| 1-4 | 5-9 | 10+|
| -------- | -------- | -------- |-------- |
| Rate     | 25%    | 50%     |100%         |

Let's see an example to better understand it!

#### Example - Integrate to DoubleOrNothing
![](https://i.imgur.com/1X5tONQ.png =x600)

Let's add referrals to Double or Nothing!
To do so we need to set up referral rules first:

* A user would pay 3% for referral, in different referral levels would get 60%, 30%, 10% of 3%
* A user gets 50% of referral bonus when they refer less than 5 people, 75% for less than 25 people, and 100% when over 25 people
* A user needs to play within 24 hours to remain an active user, which means that if a user does not play once a day, this user cannot get the referral

So, assume:
The referral sequence A ← B ← C ← D
A has referrerd 25 people, B has 6 people and C has 1 person. When D bets 1TT, 3% of bet will go to the referral pool (0.03TT). Then each upline will get:
* A: 1 * 0.03 * 0.1 * 1 = 0.003
* B: 1 * 0.03 * 0.3 * 0.75 = 0.00675
* C: 1 * 0.03 * 0.6 * 0.5 = 0.009

So the parameters we pass to constructor will be:



|| decimals| referralBonus |secondsUntilInactive    |    |onlyRewardActiveReferrers    |levelRate    |refereeBnusRateMap|
| -------- | -------- | -------- | --- | --- | --- | --- | ---|
| value    | 1000     | 30     |86400     |true     |[600,200,100]    |[1,500,5,750,25,1000]     |[1,500,5,750,25,1000]|

Now let's enable the referral!

**Contract**

First import and pass parameters to our referral contract:
``` solidity=
pragma solidity 0.5.0;

import '@thundercore/referral-solidity/contracts/Referral.sol';
...

contract DoubleOrNothing is Ownable, Referral {
  ...
  constructor(
      uint _decimals,
      uint _referralBonus,
      uint _secondsUntilInactive,
      bool _onlyRewardActiveReferrers,
      uint256[] memory _levelRate,
      uint256[] memory _refereeBonusRateMap
  ) Referral(
      _decimals,
      _referralBonus,
      _secondsUntilInactive,
      _onlyRewardActiveReferrers,
      _levelRate,
      _refereeBonusRateMap
  ) public {}
  ...
```
Then, add overload bet function to bind referral upline when bet with the address.

``` solidity=
function bet(address payable _referrer) payable external {
    if(!hasReferrer(msg.sender)) {
      addReferrer(_referrer);
    }
    bet();
  }
```
Next, add payReferral in bet function

``` solidity=
function bet() payable public {
    // msg.value is added to the balance to begin with so you need to double it
    require( address(this).balance >= msg.value * 2, 'Balance too low!');
    uint256 winnings = 0;

    // DO NOT USE THIS IN PRODUCTION, IT IS INSECURE
    if(uint256(blockhash(block.number -1)) % 2 == 0) {
      // 3% is deducted to cover the referral bonus
      winnings = msg.value * 197/100;
      address(msg.sender).transfer(winnings);
    }
    payReferral(msg.value);
    emit BetSettled(msg.sender, winnings);
  }
```
Finally, to deploy our DoubleOrNothing, we need to pass parameters in the migrations.
``` javascript=
// migrations/1_initial_migration.js
module.exports = function(deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(
    Double,
    1000,
    30,
    86400,
    true,
    [600, 200, 100],
    [1, 500, 5, 750, 25, 1000]
  );
};
```
**Frontend**
Now, you can get the referral data from public accounts in the contract, including the total amount of reerees and the total referral bonus of a user.

``` javascript=
this.props.contract.accounts(this.props.address).then((info: any) => {
  this.setState({
    accountInfo: {
      reward: info.reward.toString(),
      referredCount: info.referredCount.toString()
    }
  });
});
```
Then, you can paste the URL to get referrer, like`https://thundercore.github.io/DoubleOrNothing?referrer=0x26b067f40696c97a058658949ec011ed6a84afe3`. Then, trigger smart contract by `contract.bet(address)` to bind uplines and `contract.bet()` for normal bet. The referral will pay directly when bet.

For more information, please refer to [here](https://github.com/thundercore/DoubleOrNothing).

---
### TTSwap Resources
TT Swap is a decentralized token exchange service based on the Uniswap open-source protocol and deployed on ThunderCore.

**Documents, ABI and source code**
For more information please refer to [ThunderCore Github repository](https://github.com/thundercore/ttswap-contracts#function-tokentotokentransferoutput).

___
##  Configure ThunderCore on Metamask

### Create a Metamask Wallet

If you are wondering how to create a new cryptocurrency wallet, consider creating one by installing the Metamask extension.

Metamask is a free an secure browser that allows web appllications to read and interact with the Ethereum blockchain.

**Step1 ==Install Metamask on your browser==**
Install Metamask extension from Chrome, Firefox, Brave and Opera browsers.

We will be using Google Chrome for the following tutoial.
1. Search Metamask extension using your search engine.
2. Install Metamask as a Google Chrome extension
3. Click add to Chrome
4. Click add extension


**Step2 ==Create an account==**
1. Click on the Metamask icon in the upper right corner to open the extension
1.1 Install the latest version if there is any
2. Create an account by creating new password
3. Prcceed by clicking Next, then accept Terms of Use
4. Click Reveal secret words
5. Metamask will show 12 words seed phrase. Save seed words as a file to a save place and click Next
6. Verify your secret phrase by selecting the previously generated phrase. When done, click confirm
By "solving this puzzle" you are confirming that you know your secret phrase


**Yay!** You have successfully created your Metamask account.

**Add ThunderCore network**
To add ThunderCore's mainnet, click on the Network selection dropdown and then clock on Custom RPC

1. Open Metamask and select custom RPC from the network dropdown
2. Go to Setting page
![](https://i.imgur.com/uPlP8V0.png)
3. Add a new network
4. Put in a Network name - "Thundercore Mainnet"
5. Put new RPC URL - "https://testnet-rpc.thundercore.com"
6. Put chain ID - "108" ->
7. Put currency symbol  - "TT"
8. Put block explorer URL - "https://scan.thundercore.com/"
9. Click save, you will be directly switched to ThunderCore's mainnet now in the network dropdown list. You can now close the dialog.

![](https://i.imgur.com/aAxfwf5.png)

---
**Configure Thundercore on Metamask**
In order to view the flow of funds in your accounts, on the Polygon Network, you will need to configure Thundercore{testnet, mainnet} URL on Metamask.

![](https://i.imgur.com/lzMxVEB.png)

![](https://i.imgur.com/99u9gMf.png)

![](https://i.imgur.com/v1KFvzl.png)

---

### Config Custom Tokens(tt-20)

#### Deploy Your Own ERC-20
**ERC20** tokens are one of the most popular DApps in the blockchain community. This tutorial will guide you through deploying an ERC-20 smart contract on ThunderCore in 5 simple steps. It's super easy and fast!
#### Requirements
This tutorial expects you to have some basic knowledge of Truffle, Ethereum, Metamask and Solidity.
#### Install development tools
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

**Install MetaMask**
MetaMask is a browser extension that serves as a “wallet” that safely stores your cryptocurrencies such as Ether (ETH) and Thunder Tokens (TT). It also serves as a “bridge” that connects the web application with the blockchain. You can download and learn more about [Metamask](https://metamask.io/).
**Get Thunder Tokens or Testnet Tokens**
To get started, you will need to get Thunder Tokens (Mainnet) or Testnet Tokens (Testnet) to deploy your smart contracts on ThunderCore. Please follow this instruction to get your tokens.

**Steps**
In this tutorial we will be covering:
* Cloning tt20 repository and installing dependencies
* Updating config file of ERC20 Token
* Compiling and deploying the smart contract on ThunderCore
* Transfering your ERC20 to others
**1.Cloning TT20 repository and installing dependencies**
To make it easier to get started with ThunderCore, we've created a ERC20 contract, TT20. You can download the contract with git command.​
On a terminal, input the following command to download the repository
>git clone https://github.com/thundercore/tt20

Next, we'll update the required dependencies for deploying the contract.
```
npm install
# or
yarn install
```
**2.Updating config file of ERC20 Token**
Since we've finished the contract already, the only thing we need to do is to update the config file config.json in tt20 folder.
The config.json should look like the following:
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
* The initialSupply field determines the number of tokens created when this contract is deployed. In this case, the number is arbitrary.
Now, we have our own tokens!
**3. Compiling and deploying the smart contract**
In the migrations/2_deploy_contracts.js, we load the configuration from config.js of ERC20 and deploy the contract.
Before we compile and deploy our own ERC20, we can setup a local chain. By using a local blockchain, we can test our contract without consuming real tokens. We recommend using Ganache. Refer to thundercore/ganache and build the Ganache GUI or using the CLI tool thundercore/ganache-cli with the following command.
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
``` <!DOCTYPE html>
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
Now, your ```MyToken``` is deployed and mint to your first address in ganache.



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
Now, your **MyToken** is deployed and mint to your first address in ganache.
**4. Deploy to the ThunderCore Testnet and Mainnet**
Now, you can prepare to deploy your token to ThunderCore testnet or mainnet. Please make sure you have ThunderCore Testnet Token (TST) or ThunderToken (TT).
 First you set up the control of your account to truffle. You can set either by:
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
3. If you use metamask to control your address, you can check how to export the private key here. The address you used will be filled your ``` MyToken``` .
4. Compile and migrate your contract for testnet and mainnet
```
# Deploy to testnet
./deploy-contracts --network thunder-testnet

# or Deploy to mainnet
./deploy-contracts --network thunder-mainnet

```

5. After deploying your own token, ```totalSupply``` will be added to your accounts. Check out MetaMask to see how to add custom token on MetaMask.
The token contract address should be in the stdout after you executed the deployment command.
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
**5. Transfering your ERC20 token to others**
If you have already added MyToken to your MetaMask, try to send your tokens to other accounts. See more detail on MetaMask doc
Note
If you try on your local ganache, make sure to set the custom network to your localchain. For exmaple, set rpc url to http://localhost:9545 and chain id 5777. Then you can import private key from ganache to metamask or open a browser without MetaMask (such as incognito window) to see your tokens.
Learning more about DApps
It’s beyond the scope of this tutorial to go over the code, but if you’d like to learn more about smart contract programming and building DApps in general, we recommend the official Solidity documentation and truffle tutorial.
For questions, please join to our Discord channel.
Happy Coding! 😆

---
### Create multiple accounts

To create multiple accounts,
1. Click on Profile icon on Metamask and then click on Create Account

![](https://i.imgur.com/dV7a9T5.png)

2. Add an account name and click on create

![](https://i.imgur.com/RRfpkqs.png)

To ceate more accounts by repeating step 1 and 2. When creating multiple accounts, your addresses will be different at your end.

---

---
## Wallets

### Metamask
**Getting started**

![](https://i.imgur.com/p858POB.png)

* Metamask is a browser add-on that manages a user’s Ethereum wallet by storing their private key on their browser’s data store and the seed phrase encrypted with their password. It is a non-custodial wallet, meaning, the user has full access and responsibility their private key.
    Once lost, the user can no longer control the savings or restore access to the wallet.

**Wallet Connected**
**1.connecting to the front-end part by web3.js**
``` javascript=
const config = require("../config.json");

const web3 = require('web3');//connect blockchain to frontend by web3
const BN = web3.utils.BN;

const initialSupply = new BN(config.initialSupply);
const name = config.name;
const symbol = config.symbol;
const decimals = new BN(config.decimals);




module.exports = function(deployer) {
  deployer.deploy(Token, initialSupply, name, symbol, decimals);
};
//erc-20 source code
```
**2.connecting to the wallet by  ``HDWalletProvider``**
If you want to set up your Dapp ,you can  export your private keys from your wallet to ``.private-keys``, then you can directly connect to either thunder testnet or mainnet network.
``` javascript=
/**
 * Use this file to configure your truffle project. It's seeded with some
 * common settings for different networks and features like migrations,
 * compilation and testing. Uncomment the ones you need or modify
 * them to suit your project as necessary.
 *
 * More information about configuration can be found at:
 *
 * truffleframework.com/docs/advanced/configuration
 *
 * To deploy via Infura you'll need a wallet provider (like @truffle/hdwallet-provider)
 * to sign your transactions before they're sent to a remote public node. Infura accounts
 * are available for free at: infura.io/register.
 *
 * You'll also need a mnemonic - the twelve word phrase the wallet uses to generate
 * public/private key pairs. If you're publishing your code to GitHub make sure you load this
 * phrase from a file you've .gitignored so it doesn't accidentally become public.
 *
 */

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

---
## Bridges
The ThunderCore bridge allows user to transfer assets between 2 chains in the Ethereum ecosystem. The bridge is a customized version of POA network bridge.

**Production asset-transfer bridges**
The following bridges are fully functioned in production environments:

Ethereum Network (ThunderCore network to ETH mainnet): Cost effective

BSC Network (ThunderCore mainnet to BSC Network): A bridge service providing access to inter-blockchain liquidity for Binance Chain, Binance Smart Chain decentralized applications.

HECO Network (ThunderCore mainnet to HECO Network): A decentralized and cost-efficient public chain that Ethereum developers can easily get started with and smart contracts are seamlessly compatible.

---
### Chain and Network definitions
A bridge is created between 2 networks, referred to as a Native (or Home) Network and Foreign network.

**Home**: A network with fast and inexpensive operations. This side of bridge collects validator confirmations.
**Foreign**: Can be any chain, but generally refers to Ethereum mainnet.

**Bridge components**
The bridge consists of several components, including smart contracts, an event handler, and an optional UI. All components are located in the repository.

**TokenBridge**: Listens to events and sends transactions to authorize asset transfers.
Bridge UI Application: A DApp GUI to transfer tokens and coins between chains.

**Bridge Monitor**: A tool for checking balances and unprocessed events in bridged networks
Bridge Deployment Playbooks: Optional playbook which can manae token-bridge configuration instructions for remote deployments.

**Bridge Smart Contracts**: Manages bridge validators, collects signatures, and confirms assets realy and disposal.

---
### Architecture
**ERC20-to-ERC20**
![](https://i.imgur.com/3wh6XZW.png)

For more information please refer to [Thunder Bridge](https://github.com/thundercore/thunder_bridge).

---
### Interact with ThunderCore Bridge
---
### Ethereum <> Thundercore
---
### BSC <> Thundercore
---
### Calling contracts
**ETH**
**ERC20**

---

## Integrate with ThunderCore
ThunderCore is a scaling solution for public blockchain. ThunderCore supports all existing Ethereum tooling along with faster and much much much cheaper transactions.

If you are looking to integrate with ThunderCore, you are in the right place.


### Network information

**Mainnet**
Network: ThunderCore Mainnet
RPC: https://mainnet-rpc.thundercore.com
Status: Running
Block Explorer: https://scan.thundercore.com/

**Testnet**
Network: ThunderCore Testnet
RPC: https://testnet-rpc.thundercore.com
Status: Running
Block Explorer: https://scan-testnet.thundercore.com/

**How to read Network details?**
You have the network details by visiting the below shared support links.


---
### Network details

----
### Thundercore faucet
---> direct the page to faucet page

---
### Full node deployment
---> direct the page to full nooe deployment

---
## DApp Submission
### DApp listing





