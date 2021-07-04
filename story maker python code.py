import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a tiger', 'a dog','a cat']
name = ['Chuwi', 'Makyr','Leia', 'Solo', 'Skywalker']
residence = ['Bhutan','India', 'Italy', 'France', 'Australia']
went = ['the movies', 'college','gym', 'school', 'mall']
happened = ['made a lot of friends','ate pizza', 'found a secret map', 'grew', 'wrote a book']
print(random.choice(when) + ',' + random.choice(who) +' named ' + random.choice(name) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
