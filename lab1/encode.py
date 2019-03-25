from entropy import process_file, get_results
import pandas as pd
import matplotlib.pyplot as plt


def base64encode(data):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
    
    bit_str = ''
    base64_str = ''
    div24_symb = ''
    
    for byte in data:
        bin_byte = bin(byte).lstrip("0b")
        bin_byte = bin_byte.zfill(8)
        bit_str += bin_byte
    
    while len(bit_str) % 24 != 0:
        div24_symb = '='
        bit_str += '0'

    groups = [bit_str[x:x+6] for x in range(0,len(bit_str),6)]
    for group in groups:
        base64_str += alphabet[int(group, 2)]

    base64_str += div24_symb

    return base64_str


kurz = open('sources/ray_kurz', 'rb')
struct = open('sources/struct', 'rb')
artic = open('sources/artic', 'rb')


with open('sources/ray_kurz_enc', 'w') as file:
    file.write(base64encode(kurz.read()))
with open('sources/struct_enc', 'w') as file:
    file.write(base64encode(struct.read()))
with open('sources/artic_enc', 'w') as file:
    file.write(base64encode(artic.read()))

with open('sources/ray_kurz.bz2', 'rb') as source, open('sources/ray_kurz_bz2_enc', 'w') as file:
    file.write(base64encode(source.read()))
with open('sources/struct.bz2', 'rb') as source, open('sources/struct_bz2_enc', 'w') as file:
    file.write(base64encode(source.read()))
with open('sources/artic.bz2', 'rb') as source, open('sources/artic_bz2_enc', 'w') as file:
    file.write(base64encode(source.read()))

kurz = open('sources/ray_kurz')
struct = open('sources/struct')
artic = open('sources/artic')

kurz_enc = open('sources/ray_kurz_enc')
struct_enc = open('sources/struct_enc')
artic_enc = open('sources/artic_enc')

kurz_bz2 = open('sources/ray_kurz_bz2_enc')
struct_bz2 = open('sources/struct_bz2_enc')
artic_bz2 = open('sources/artic_bz2_enc')

print
print
print

info_kurz = process_file(kurz, 'Kurzweil orig')
info_kurz_enc = process_file(kurz_enc, 'Kurzweil encoded')
info_kurz_bz2 = process_file(kurz_bz2, 'Kurzweil bz2 encoded')
print('Kurzweil orig: %f enc: %f bz2+enc: %f' % (info_kurz, info_kurz_enc, info_kurz_bz2))

info_struct = process_file(struct, 'Structured orig')
info_struct_enc = process_file(struct_enc, 'Structured encoded')
info_struct_bz2 = process_file(struct_bz2, 'Structured bz2 encoded')
print('Structured orig: %f enc: %f bz2+enc: %f' % (info_struct, info_struct_enc, info_struct_bz2))

info_artic = process_file(artic, 'Article orig')
info_artic_enc = process_file(artic_enc, 'Article encoded')
info_artic_bz2 = process_file(artic_bz2, 'Article bz2 encoded')
print('Article orig: %f enc: %f bz2+enc: %f' % (info_artic, info_artic_enc, info_artic_bz2))

df1 = pd.DataFrame([info_kurz, info_kurz_enc, info_kurz_bz2], index=['orig', 'enc', 'bz2+enc'])
ax1 = df1.plot(kind='bar')
ax1.legend(['Ray Kurzweil'])
df2 = pd.DataFrame([info_struct, info_struct_enc, info_struct_bz2], index=['orig', 'enc', 'bz2+enc'])
ax2 = df2.plot(kind='bar', color='green')
ax2.legend(['Structured Procr.'])
df3 = pd.DataFrame([info_artic, info_artic_enc, info_artic_bz2], index=['orig', 'enc', 'bz2+enc'])
ax3 = df3.plot(kind='bar', color='brown')
ax3.legend(['Article'])
plt.show()



