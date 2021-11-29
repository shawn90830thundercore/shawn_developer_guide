# Deploy a DApp

### **Overview**

Let's use 5-10 minutes to deploy a complete game through ThunderCore that is easily accessible to your own friends and family -- accessible to anyone with internet access. We will release a simple coin toss game where players will receive twice as many bets if the coin is facing up. In the case of coins facing down, players will lose their bets, but still have a chance to double the bet.

#### **Exploring the Game**

To begin, we will obtain a wallet and gain access to the Thunder network. With either Metamask or TrustWallet pointed to the Thunder RPC, navigate [HERE](https://thundercore.github.io/DoubleOrNothing/) to play the game we will build in this tutorial!

![](https://i.imgur.com/IbBIWXd.png)

To make your own version of the page, just check out the [repo](https://github.com/thundercore/DoubleOrNothing) and follow the instructions in the readme.

At the end of those instructions, you should be able to access the game with either your mobile device through Metamask or any ThunderCore compatible mobile DApp browsers.

#### **Deploying Your Own Contract**

Now, let's get your game running on your own copy of the contract, so you can get started developing your own killer DApp!

First we will install all the dependencies.

```
node -v
# Let's make sure our node is v8 or v10
```

If you haven't downloaded node.js, go to [node.js](https://nodejs.org/en/download/) download the version 8 or version 10. If you have downloaded it before but your version is incompatible, install it with [nvm](https://github.com/nvm-sh/nvm), and follow the instructions below.

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

Next grab your mnemonic or import your private key from metamask and create a file called .private-keys under “./smart-contracts ” or Trust Wallet and add it to the HDWallet in truffle-config.js

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

In the console, you will see the price you've paid for its deployment, the contract address, and additional stats. Well done! Your contract is now up and running ready to be used by anyone. If the contract address of DoubleOrNothing didn’t show up in the console after the migration ,you can check the contract address by typing the command below.

```
mainnet
$ Truffle console --network thunder-mainnet
testnet
$ Truffle console --network thunder-mainnet

let contract = await DoubleOrNothing.deployed()
DoubleOrNothing.address
```

To make sure you've deployed doubleOrNothing smart contract successfully,you can double check the contract address and contract block number you've deployed lately.

#### Testnet

```
truffle(thunder-testnet)>let contract = await DoubleOrNothing.deployed()
truffle(thunder-testnet)> DoubleOrNothing.address
'0x48caD7fe30Fd1CA52EcBda9C82E398B0FFd321eE'
truffle(thunder-testnet)> n = web3.eth.getBlockNumber();
62591612
```

#### Mainnet

```
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

Find the .env file and change the **REACT\_APP\_CONTRACT\_ADDRESS** to your new address which you got by the command **DoubleOrNothing.address** above.

Meanwhile, change **REACT\_APP\_TT\_USDT\_CONTRACT** to 0xB1Fb0b14Ffea209ABa1e62ff3F2F3DFD2eaa9FE0, and comment out another REACT\_APP\_TT\_USDT\_CONTRACT address. If you’re not sure of the REACT\_APP\_TT\_USDT\_CONTRACT testnet or mainet address , check it on [thundercore bridge](https://bridge-venus.thundercore.com/eth/).

Below are the specific steps we mentioned above.

First of all, click on the option above.Next, click the info symbol below ![](https://i.imgur.com/RNRzYiF.png)

![](https://i.imgur.com/Y0yZiw9.png) You can see the **TT-USDT ADDRESS** ,which is **REACT\_APP\_TT\_USDT\_CONTRACT**=0xB1Fb0b14Ffea209ABa1e62ff3F2F3DFD2eaa9FE0

!\[]\(https://i.imgur.com/XRGHrV4.png =x300)

```
yarn start
# or
npm run start
```

This will start a local server with your changes. If you want to deploy this to your webpage run:

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

\*\*Voila! \*\*In 5-10 seconds, your webpage will be running on your contract. Congratulations!

#### **Debugging**

\*\* \*\*Add a Console to display an Error Message in the DApp's UI when running in the ThunderCore Hub Wallet’s Browser Tab to display any error messages for problems/errors encountered while interacting with the chain.

Example 1: [TT20 Transactions](https://github.com/thundercore/hubbit-field-support/blob/c69d3798f77fd07d8b3f0381b5a0dc78addd0691/src/index.js#L172)

Example 2: [DoubleOrNothing](https://github.com/thundercore/DoubleOrNothing/commit/8d5e755876f77f309937b31791ae246b4826566a#diff-1a2294bec8f8b96cd516ecd00ef9f3c8R135)
