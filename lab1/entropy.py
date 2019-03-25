import matplotlib.pyplot as plt
import math
import pandas as pd
import os


def count_freq(chars):
    freq = {}
    total = sum(chars.values())
    for char in chars.keys():
        freq[char] = chars[char] * 1. / total
    
    return freq


def count_amount(string):
    chars = {}
    for char in string:
        if char not in chars.keys():
            chars[char] = 1
        else:
            chars[char] += 1
    
    return chars


def count_entropy(freq):
    entropy = 0
    for char in freq:
        entropy -= freq[char] * math.log(freq[char], 2)

    return entropy


def get_results(string):
    chars = count_amount(string)
    freq = count_freq(chars)
    entropy = count_entropy(freq)

    return chars, freq, entropy


def visualize_sep(chars, freq):
    order = sorted([*chars])
    
    df1 = pd.DataFrame.from_dict(chars, orient='index')
    df1 = df1.reindex(order)
    ax = df1.plot(kind='bar')
    ax.legend(['quantity of chars'])
    plt.show()

    df2 = pd.DataFrame.from_dict(freq, orient='index')
    df2 = df2.reindex(order)
    ax = df2.plot(kind='bar', color='green')
    ax.legend(['frequency of chars'])
    plt.show()


def process_file(file, name):
    string = file.read()
    chars, freq, entropy = get_results(string)
    print('Chars amounts in %s' % name)
    keys = [*chars]
    keys.sort()
    for key in keys:
        print('%s: %i' % (key, chars[key]))
    print

    print('Chars frequency in %s' % name)
    for key in keys:
        print('%s: %f' % (key, freq[key]))

    print('Entropy: %f' % entropy)
    print('Quantity of information: %f' % (entropy * sum(chars.values()) / 8))
    visualize_sep(chars, freq)

    return entropy * sum(chars.values()) / 8

kurz_orig = 'sources/ray_kurz'
file_kurz = open(kurz_orig)
kurz_zip = kurz_orig + '.zip'
kurz_gz = kurz_orig + '.gz'
kurz_bz2 = kurz_orig + '.bz2'
kurz_7z = kurz_orig + '.7z'
kurz_xz = kurz_orig + '.xz'
info_kurz = process_file(file_kurz, '\"The Singularity is Near\" Prologue')

struct_orig = 'sources/struct'
file_struct = open(struct_orig)
struct_zip = struct_orig + '.zip'
struct_gz = struct_orig + '.gz'
struct_bz2 = struct_orig + '.bz2'
struct_7z = struct_orig + '.7z'
struct_xz = struct_orig + '.xz'
info_struct = process_file(file_struct, '\"Structured Procrastination\"')

artic_orig = 'sources/artic'
file_artic = open(artic_orig)
artic_zip = artic_orig + '.zip'
artic_gz = artic_orig + '.gz'
artic_bz2 = artic_orig + '.bz2'
artic_7z = artic_orig + '.7z'
artic_xz = artic_orig + '.xz'
info_artic = process_file(file_artic, '\"3D Reconstruction of Human Face...\"')

orig = list(map(os.path.getsize, [kurz_orig, struct_orig, artic_orig]))
_zip = list(map(os.path.getsize, [kurz_zip, struct_zip, artic_zip]))
_gz = list(map(os.path.getsize, [kurz_gz, struct_gz, artic_gz]))
_bz2 = list(map(os.path.getsize, [kurz_bz2, struct_bz2, artic_bz2]))
_7z = list(map(os.path.getsize, [kurz_7z, struct_7z, artic_7z]))
_xz = list(map(os.path.getsize, [kurz_xz, struct_xz, artic_xz]))


plt.scatter([info_kurz, info_struct, info_artic], orig, label='original')
plt.scatter([info_kurz, info_struct, info_artic], _zip, label='zip')
plt.scatter([info_kurz, info_struct, info_artic], _gz, label='gz')
plt.scatter([info_kurz, info_struct, info_artic], _bz2, label='bz2')
plt.scatter([info_kurz, info_struct, info_artic], _7z, label='7z')
plt.scatter([info_kurz, info_struct, info_artic], _xz, label='xz')
plt.xlabel('Quantity of information')
plt.ylabel('Size of file')
plt.legend()
plt.show()
