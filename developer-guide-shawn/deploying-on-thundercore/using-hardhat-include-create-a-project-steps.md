# Using Hardhat

> Hardhat is a development environment tool that helps developers to test, compile, deploy, and debug your Ethereum software.

#### **Setting up Hardhat**&#x20;

There are a few technical requirements before we start.  Please install the following:

* [Node.js v10+ LTS and npm](https://nodejs.org/en/)
* [Git ](https://git-scm.com)

Once we have those installed, we then install Hardhat.

To install it, you need to create an npm project by going to an empty folder, running `npm init`, and following the instructions. When the project is ready, run the code:

```
npm install --save-dev hardhat
```

Let's try to create a sample project to compile, test, and deploy sample contract. To learn more about the sample contract [in this guide.](https://hardhat.org/getting-started/#installation)

#### **Hardhat Config**

1. Go to hardhat.config.js
2. Update tne hardhat config with ThunderCore network credential
3. Create .env file in the root to store your private key

```
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
    // ... solc 
    evmVersion: 'byzantium', //
  },
  // ...
}
```

#### **Deploy on ThunderCore Network**

Run the command in root of the project directory:

```
$ npx hardhat run scripts/sample-script.js --network thundercore
```

Contract will be deploy on ThunderCore's testnet, which looks like:

```
Compilation finished successfully
Greeter deployed to: 0xfaFfCAD549BAA6110c5Cc03976d9383AcE90bdBE
```
