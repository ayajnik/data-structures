## there are three ways by which we can create a dictionary

## Approach 1:

a = dict(one='uno',two='dos',three='tres')
print(a)

print('---------------------x-------------------------')

b = {'one':'uno','two':'dos','three':'tres'}
print(b)

print('---------------------x-------------------------')

c = [('one','uno'), ('dos','two'), ('three','tres')]
c_dict = dict(c)
print(c_dict)

print('---------------------x-------------------------')
