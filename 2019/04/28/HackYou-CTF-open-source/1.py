first=0xcafe
second=25
third='h4cky0u'

h=first*31337+(second%17)*11+len(third)-1615810207
print('%x' % h)