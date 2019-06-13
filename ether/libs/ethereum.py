#!/usr/bin/env python3
# encoding: utf-8

from web3 import Web3
import ether_scripts.settings as settings

web3 = Web3(Web3.HTTPProvider(
    'https://{network}.infura.io/v3/{project_id}'.format(network=settings.ETHEREUM_NETWORK,
                                                         project_id=settings.INFURA_PROJECT_ID),
))


def etherscan_tx(tx_hash: str):
    if 'mainnet' == settings.ETHEREUM_NETWORK:
        return 'https://etherscan.io/tx/{}'.format(tx_hash)
    elif 'kovan' == settings.ETHEREUM_NETWORK:
        return 'https://kovan.etherscan.io/tx/{}'.format(tx_hash)
    return
