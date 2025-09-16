import hashlib
s='bridgeabbos'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
