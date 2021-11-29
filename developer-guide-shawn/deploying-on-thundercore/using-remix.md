# Using Remix

> Remix is a web-based IDE for writing, compiling, and deploying contracts.

#### **Setting up Remix IDE**&#x20;

Visit [Remix](https://remix.ethereum.org) to access the Remix IDE from your web browser.

Note: If this is your first time using Remix, you must locate and activate the "Solidity Compiler" plug-in, as shown in below

1. Go to File explorers
2. Create a new file, name it
3.  Copy & paste the Smart contract below into the newly created file hellothundercore.sol

    ![](https://i.imgur.com/QqhqhLY.png)

#### **The smart contract**

````solidity
hellothundercore.sol
// Specifies that the source code is for a version
// of Solidity greater than 0.5.10
pragma solidity ^0.5.10;

// A contract is a collection of functions and data (its state)
// that resides at a specific address on the Ethereum blockchain.
contract hellothundercore {

    // The keyword "public" makes variables accessible from outside a contract
    // and creates a function that other contracts or SDKs can call to access the value
    string public message;

    // A special function only run during the creation of the contract
    constructor(string memory initMessage) public {
        // Takes a string value and stores the value in the memory data storage area,
        // setting `message` to that value
        message = initMessage;
    }

    // A publicly accessible function that takes a string as a parameter
    // and updates `message`
    function update(string memory newMessage) public {
        message = newMessage;
    }
}
```
````

The first line, `pragma solidity ^0.5.10` specifies that the source code is for a Solidity version greater than 0.5.10. [Pragmas](https://solidity.readthedocs.io/en/latest/layout-of-source-files.html#pragma) are common instructions for compilers about how to treat the source code (e.g., pragma once).

A contract in the sense of Solidity is a collection of code (its functions) and data (its state) that resides at a specific address on the Ethereum blockchain. The line `string public message` declares a public state variable called `message` of type `string`. You can think of it as a single slot in a database that you can query and alter by calling functions of the code that manages the database. The keyword public automatically generates a function that allows you to access the current value of the state variable from outside of the contract. Without this keyword, other contracts have no way to access the variable.

The [constructor](https://solidity.readthedocs.io/en/latest/contracts.html#constructor) is a special function run during the creation of the contract and cannot be called afterward. In this case, it takes a string value `initMessage`, stores the value in the [memory](https://solidity.readthedocs.io/en/latest/introduction-to-smart-contracts.html#storage-memory-and-the-stack) data storage area, and sets `message` to that value.

The `string public message` function is another public function that is similar to the constructor, taking a string as a parameter, and updating the `message` variable.

#### **Compile smart contract**

***

* ![](https://i.imgur.com/rzqMPps.png)Go to Solidity Compiler
* Select Compiler Version to 0.5.10
* Now, `Compile hellothundercore.sol`
* After Successful Compilation, it will show ![](https://i.imgur.com/eCD9qGV.png)
* Now, We have to deploy our smart contract on ThunderCore Network. For that, we have to connect to web3 world, this can be done by using any of the services like Metamask, Brave, Portis etc. We will be using Metamask. 
* Open Metamask and select Custom RPC from the networks dropdown

Let's deploy your smart contract on ThunderCore Network. To do so we need to connect to web3 world, which can be done by using services like Metamask, Brave and Portis etc. We will be using Metamask to connect to web3 world. Please follow the tutorial to setup a Metamask Account..

1. Open Metamask and select custom RPC from the network dropdown
2. Go to Setting page ![](https://i.imgur.com/uPlP8V0.png)
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

![](../.gitbook/assets/image%20\(1\).png)

![](../.gitbook/assets/Metamask-rpc.png)

9\. Go ahead and click save

10\. Copy your address from Metamask

* Head over to [Faucet](https://faucet-testnet.thundercore.com/) and request test ether - you will need this pay for gas on ThunderCore. Select 'ThunderCore testnet or mainnet' as the network and 'tt Token' as the token in the faucet
* Now, let's Deploy the Smart Contract on ThunderCore Network
* Select Injected Web3 in the Environment dropdown and your contract
* Accept the Connection Request!
* Once Metamask is connected to Remix, the ‘Deploy’ transaction would generate another Metamask popup that requires transaction confirmation.

![](../.gitbook/assets/image%20\(4\).png)

**Congratulations!** You have successfully deployed HelloWorld Smart Contract. Now you can interact with the Smart Contract. Check the deployment status here:[https://viewblock.io/thundercore](https://viewblock.io/thundercore)

![](../.gitbook/assets/image%20\(3\).png)

![](https://i.imgur.com/QWtGKWz.png)
