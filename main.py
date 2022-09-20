import time
import random
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

def getBlockData(rpc_connection,blockHash):
    data = rpc_connection.getblock(blockHash)
    return data

def getBlockHash(rpc_connection,blockHeight):
    blockhash = rpc_connection.getblockhash(blockHeight)
    return blockhash

def getBlockTimestamp(rpc_connection, height):
    blockHash = getBlockHash(rpc_connection,height)
    blockData = getBlockData(rpc_connection,blockHash)
    return blockData['time']

def getTimeStamp():
    rpc_connection = AuthServiceProxy("http://user:password@127.0.0.1:8332")
    genesisTimestamp = 1231006505
    userTimestamp = int(input('Please enter timestamp'))
    start = time.time()
    currentHeight = 754889
    blockChainAge = 1663647780 - genesisTimestamp
    difference = userTimestamp - genesisTimestamp
    startingHeight = round(currentHeight * (difference / blockChainAge))
    run = True
    min = 0
    max = 754889
    while run == True:
        guess = int(getBlockTimestamp(rpc_connection,startingHeight))
        if guess < userTimestamp + 1800 and guess > userTimestamp - 1800:
            print('Success!' + str(startingHeight))
            run = False
        elif guess > userTimestamp:
            newBlockheight = random.randrange(min, startingHeight+1)
            max = startingHeight
            startingHeight = newBlockheight
        elif guess < userTimestamp:
            newBlockheight = random.randrange(startingHeight, max+1)
            min = startingHeight
            startingHeight = newBlockheight
    end = time.time()
    print(end - start)


getTimeStamp()
