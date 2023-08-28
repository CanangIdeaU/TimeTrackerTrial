from time import sleep
from tqdm import trange
def bar(Kegiatan):
    print()
    print(f'{Kegiatan}....')
    for i in trange(20) :
        sleep(0.1)
    print(f'{Kegiatan} is done')
    print()