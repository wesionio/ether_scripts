#!/usr/bin/env python3
# encoding: utf-8

import ether_scripts.settings as settings
from .ethereum import web3


def get_balance(address: str):
    return web3.eth.getBalance(address)


def txn_transfer(to: str, value: int, nonce: int, gas_price: int, gas_limit: int = 21000):
    return {
        'to': to,
        'value': value,
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': nonce,
        'chainId': settings.ETHEREUM_NETWORK_ID
    }
