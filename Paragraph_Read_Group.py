#!/usr/bin/env python
# coding: utf-8

# ## Read paragraph and group words.

# In[46]:


def group_para_words(paragraph):
    filter_para=paragraph.replace(',','').lower()
    unwanted_words=['to','is','the','this','of','has','have','you','at','a','an','and','or','that']
    list_all_words=[wrd.replace('.','') for wrd in filter_para.split(' ') if wrd not in unwanted_words]
    wrd_freq=[list_all_words.count(n_wrd) for n_wrd in list_all_words]
    combine_list=list(zip(list_all_words,wrd_freq))
    return list(set(combine_list))


# In[47]:


paragraph="Guides are text-based articles that help you remove roadblocks and solve technical problems faster with reliable, just-in-time answers. With helpful resources like code blocks and real-life examples, guides are easy to search for quick answers or dive deep on a specific technology question.Data visualization plays a crucial role in exploratory data analysis and communicating business insights. However, there are several human factors that are also an important part of generating unbiased and useful results. In this guide, you will learn about these concepts, which will help you generate meaningful business insights through data visualization using R.When you have a lot of variables to analyze, it becomes important to decide which one to visualize. The human ability to use subject matter expertise and domain knowledge to identify such features is required. A few examples are discussed in the section below.The first couple of lines of code below give the number of records in the dataset that have an age below 18 years. We have three such records. The third line of code removes such records, while the fourth line prints the dimensions of the new data: 566 observations and 12 variables.Finally, look again at the summary of the age variable. This shows that the range of age is now between 23 to 76 years, indicating that the correction has been made."


# In[50]:


print(paragraph)


# In[51]:


group_list=group_para_words(paragraph)


# In[52]:


print(group_list)


# In[ ]:




