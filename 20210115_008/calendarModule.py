#!/usr/bin/env python
# coding: utf-8

# In[1]:


def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# In[2]:


def lastDay(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days[1] = 29 if isLeapYear(year) else 28
    return days[month-1]


# In[3]:


def totalDay(year, month, day):
    total = (year - 1) * 365 + (year - 1) // 4 - (year-1) // 100 + (year - 1) // 400
    for i in range(1, month):
        total += lastDay(year, i)
    return total + day


# In[4]:


def weekDay(year, month, day):
    return totalDay(year, month, day) % 7


# In[7]:


if __name__ == '__main__':
    print(isLeapYear(2000))
    print(lastDay(2021, 7))
    print(totalDay(2021, 1, 14))
    print(weekDay(2021, 1, 14))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




