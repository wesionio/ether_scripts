# coding:utf-8
import os
from django.core.management.base import (BaseCommand, CommandError)
from ether.models import Account
import ether_scripts.settings as settings
from qwert import (cli, file_fn)

ADDRS_DIR = os.path.join(settings.DATA_DIR, 'addrs')


class Command(BaseCommand):
    help = 'Address to db'

    def __init__(self, *args, **kwargs):
        print()
        super().__init__(*args, **kwargs)
        pass

    def handle(self, *args, **options):
        start = cli.integer('start block number')
        end = cli.integer('  end block number')

        for i in range(start, end + 1):
            filename = 'block_{:_>8}.txt'.format(i)
            print(filename)

            path_to_file = os.path.join(ADDRS_DIR, filename)
            for address in file_fn.read_to_list(path_to_file):
                print(filename, address)

                account, created = Account.objects.get_or_create(address=address,
                                                                 defaults={'first_block': i})
