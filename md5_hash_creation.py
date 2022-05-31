import hashlib
word='1111'
enc_wrd = word.encode('utf-8')
digest = hashlib.md5(enc_wrd.strip()).hexdigest()
print(digest)