from web3 import Web3
import os
import requests
import time
import huaweisms.api.user
import huaweisms.api.wlan
import huaweisms.api.sms
import huaweisms.api.dialup

priv = [
]

rec = [
]

def cip:
    ctx = huaweisms.api.user.quick_login("username", "pass")
    # print(ctx)
    # output: <ApiCtx modem_host=192.168.8.1>
    print('started. waiting .....')

    resultBefore = requests.get('https://checkip.amazonaws.com').text.strip()

    huaweisms.api.dialup.disconnect_mobile(ctx)
    huaweisms.api.dialup.connect_mobile(ctx)

    time.sleep(20)
    resultAfter = None
    while resultAfter is None:
        try:
            # connect
            resultAfter = requests.get('https://checkip.amazonaws.com').text.strip()
        except:
            time.sleep(3)
            pass

    os.system('cmd.exe /c ipconfig/flushdns')
    os.system('cmd.exe /c ipconfig/release')
    os.system('cmd.exe /c ipconfig/renew')
    time.sleep(1)

    print('\x1b[6;30;42m' + 'IP before: {}\n'.format(resultBefore) + '\x1b[0m')
    print('\x1b[6;30;42m' + 'IP after: {}'.format(resultAfter) + '\x1b[0m')

    exit

##################################
RPC = "https://zetachain-mainnet-archive.allthatnode.com:8545"
GAS_PRICE = 1.1
CHAIN_ID = 7000
##################################

i = 0

while i < len(priv):
    web3 = Web3(Web3.HTTPProvider(RPC))
    
    private_key = priv[i]
    receiver_address = rec[i]
    
    cip()
    account = web3.eth.account.from_key(private_key)


    tx = {
        "from": account.address,
        "to": web3.to_checksum_address(receiver_address),
        "value": web3.to_wei(0.6, "ether"),
        "nonce": web3.eth.get_transaction_count(account.address),
        "gasPrice": web3.eth.gas_price,
        "gas": 21000,
        "chainId": CHAIN_ID,
    }
    signed_txn = web3.eth.account.sign_transaction(tx, private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()

    print(transaction_hash)
    i += 1
    time.sleep(46)

