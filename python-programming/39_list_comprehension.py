# List - Comprehensions

prices:list[int] = [80, 120, 30, 300]
print('Prices List:', prices)
print('Hiked Prices `[price * 1.1 for price in prices if price > 100]`:'
      , [price * 1.1 for price in prices if price > 100])

domains:list[str] = [
    'www.google.com', 
    'yahoo.com', 
    'localhost', 
    'WWW.DATA-DOMAIN.COM', 
    'example.org'
]
print('Domains List:', domains)
print('Cleaned Domains `[domain.lower().replace("www.", "") for domain in domains if "." in domain]`:'
      , [domain.lower().replace('www.', '') for domain in domains if '.' in domain])
