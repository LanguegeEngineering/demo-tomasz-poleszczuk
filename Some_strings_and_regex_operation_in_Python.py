#!/usr/bin/env python
# coding: utf-8

# ### Easy string manipulation

# In[1]:


x = 'a string'
y = "a string"
if x == y:
    print("they are the same")


# In[2]:


fox = "tHe qUICk bROWn fOx."


# To convert the entire string into upper-case or lower-case, you can use the ``upper()`` or ``lower()`` methods respectively:

# In[3]:


fox.upper()


# In[4]:


fox.lower()


# A common formatting need is to capitalize just the first letter of each word, or perhaps the first letter of each sentence.
# This can be done with the ``title()`` and ``capitalize()`` methods:

# In[5]:


fox.title()


# In[6]:


fox.capitalize()


# The cases can be swapped using the ``swapcase()`` method:

# In[7]:


fox.swapcase()


# In[8]:


line = '         this is the content         '
line.strip()


# To remove just space to the right or left, use ``rstrip()`` or ``lstrip()`` respectively:

# In[9]:


line.rstrip()


# In[10]:


line.lstrip()


# To remove characters other than spaces, you can pass the desired character to the ``strip()`` method:

# In[11]:


num = "000000000000435"
num.strip('0')


# In[12]:


line = 'the quick brown fox jumped over a lazy dog'
line.find('fox')


# In[13]:


line.index('fox')


# In[14]:


line[16:21]


# The only difference between ``find()`` and ``index()`` is their behavior when the search string is not found; ``find()`` returns ``-1``, while ``index()`` raises a ``ValueError``:

# In[15]:


line.find('bear')


# In[16]:


line.index('bear')


# In[17]:


line.partition('fox')


# The ``rpartition()`` method is similar, but searches from the right of the string.
# 
# The ``split()`` method is perhaps more useful; it finds *all* instances of the split-point and returns the substrings in between.
# The default is to split on any whitespace, returning a list of the individual words in a string:

# In[18]:


line_list = line.split()
print(line_list)


# In[19]:


print(line_list[1])


# A related method is ``splitlines()``, which splits on newline characters.
# Let's do this with a Haiku, popularly attributed to the 17th-century poet Matsuo Bashō:

# In[ ]:


haiku = """matsushima-ya
aah matsushima-ya
matsushima-ya"""

haiku.splitlines()


# Note that if you would like to undo a ``split()``, you can use the ``join()`` method, which returns a string built from a splitpoint and an iterable:

# In[20]:


'--'.join(['1', '2', '3'])


# A common pattern is to use the special character ``"\n"`` (newline) to join together lines that have been previously split, and recover the input:

# In[21]:


print("\n".join(['matsushima-ya', 'aah matsushima-ya', 'matsushima-ya']))


# In[24]:


pi = 3.14159
str(pi)


# In[27]:


print ("The value of pi is " + pi)


# Pi is a float number so it must be transform to sting.

# In[28]:


print( "The value of pi is " + str(pi))


# A more flexible way to do this is to use *format strings*, which are strings with special markers (noted by curly braces) into which string-formatted values will be inserted.
# Here is a basic example:

# In[29]:


"The value of pi is {}".format(pi)


# ### Easy regex manipulation!

# In[30]:


import re


# In[31]:


line = 'the quick brown fox jumped over a lazy dog'


# With this, we can see that the ``regex.search()`` method operates a lot like ``str.index()`` or ``str.find()``:

# In[32]:


line.index('fox')


# In[33]:


regex = re.compile('fox')
match = regex.search(line)
match.start()


# Similarly, the ``regex.sub()`` method operates much like ``str.replace()``:

# In[34]:


line.replace('fox', 'BEAR')


# In[35]:


regex.sub('BEAR', line)


# The following is a table of the repetition markers available for use in regular expressions:
# 
# | Character | Description | Example |
# |-----------|-------------|---------|
# | ``?`` | Match zero or one repetitions of preceding  | ``"ab?"`` matches ``"a"`` or ``"ab"`` |
# | ``*`` | Match zero or more repetitions of preceding | ``"ab*"`` matches ``"a"``, ``"ab"``, ``"abb"``, ``"abbb"``... |
# | ``+`` | Match one or more repetitions of preceding  | ``"ab+"`` matches ``"ab"``, ``"abb"``, ``"abbb"``... but not ``"a"`` |
# | ``.`` | Any character | ``.*`` matches everything | 
# | ``{n}`` | Match ``n`` repetitions of preeeding | ``"ab{2}"`` matches ``"abb"`` |
# | ``{m,n}`` | Match between ``m`` and ``n`` repetitions of preceding | ``"ab{2,3}"`` matches ``"abb"`` or ``"abbb"`` |

# In[36]:


bool(re.search(r'ab', "Boabab"))


# In[37]:


bool(re.search(r'.*ma.*', "Ala ma kota"))


# In[38]:


bool(re.search(r'.*(psa|kota).*', "Ala ma kota"))


# In[39]:


bool(re.search(r'.*(psa|kota).*', "Ala ma psa"))


# In[40]:


bool(re.search(r'.*(psa|kota).*', "Ala ma chomika"))


# In[44]:


zdanie = "Ala ma kota."
wzor = r'.*' #pasuje do każdego zdania
zamiennik = r"Ala ma psa."


# In[45]:


re.sub(wzor, zamiennik, zdanie)


# In[46]:


wzor = r'(.*)kota.'
zamiennik = r"\1 psa."


# In[47]:


re.sub(wzor, zamiennik, zdanie)


# In[48]:


wzor = r'(.*)ma(.*)'
zamiennik = r"\1 posiada \2"


# In[49]:


re.sub(wzor, zamiennik, zdanie)

