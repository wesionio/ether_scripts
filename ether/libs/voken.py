#!/usr/bin/env python3
# encoding: utf-8

import os
import cli_print as cp
from qwert import file_fn
from .ethereum import web3
import ether_scripts.settings as settings

""" Voken Main Contract
"""
VOKEN_ADDRESS = file_fn.read(
    os.path.join(settings.CONTRACT_DIR, 'voken_address.txt')
)
VOKEN_ABI = file_fn.read(
    os.path.join(settings.CONTRACT_DIR, 'voken_abi.json')
)

if not web3.isChecksumAddress(VOKEN_ADDRESS):
    cp.error('ERR(Voken): "{}" is not a checksum address.'.format(VOKEN_ADDRESS))
    exit()

VOKEN_CONTRACT = web3.eth.contract(
    abi=VOKEN_ABI,
    address=VOKEN_ADDRESS,
)

""" Batch Ether and Voken
"""
BATCH_ADDRESS = file_fn.read(
    os.path.join(settings.CONTRACT_DIR, 'batch_address.txt')
)
BATCH_ABI = file_fn.read(
    os.path.join(settings.CONTRACT_DIR, 'batch_abi.json')
)

if not web3.isChecksumAddress(BATCH_ADDRESS):
    cp.error('ERR(Voken): "{}" is not a checksum address.'.format(BATCH_ADDRESS))
    exit()

BATCH_CONTRACT = web3.eth.contract(
    abi=BATCH_ABI,
    address=BATCH_ADDRESS,
)


def get_balance(address: str):
    return VOKEN_CONTRACT.call().balanceOf(address)


def txn_transfer(to: str, value: int, nonce: int, gas_price: int, gas_limit: int = 300000):
    return VOKEN_CONTRACT.functions.transfer(
        to,
        value,
    ).buildTransaction({
        'chainId': settings.ETHEREUM_NETWORK_ID,
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': nonce,
    })


def txn_approve_batch(value: int,

                      nonce: int,
                      gas_price: int,
                      gas_limit: int = 100000):
    return VOKEN_CONTRACT.functions.approve(
        BATCH_ADDRESS,
        value,
    ).buildTransaction({
        'chainId': settings.ETHEREUM_NETWORK_ID,
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': nonce,
    })


def txn_batch(wei: int,
              accounts: list,
              ether_value: int,
              voken_value: int,

              nonce: int,
              gas_price: int,
              gas_limit: int = 8000000):
    return BATCH_CONTRACT.functions.batchTransfer(
        accounts,
        ether_value,
        voken_value,
    ).buildTransaction({
        'chainId': settings.ETHEREUM_NETWORK_ID,
        'value': wei,
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': nonce,
    })
