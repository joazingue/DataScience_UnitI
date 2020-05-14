
# from DataWrangling.IO.ex_scripts import scripts as SCRPTS
# from DataWrangling.IO.ex_scripts import  practices as PRCTCS

import simplejson as json


"""
Load Data
"""

with open('./Data/201701scripts_sample.json') as f:
    SCRPTS = json.load(f)

with open('./Data/practices.json') as f:
    PRCTCS = json.load(f)

"""
Question 1: summary_statistics

Our beneficiary data (scripts) contains quantitative data on the number of items dispensed ('items'), the total quantity
of item dispensed ('quantity'), the net cost of the ingredients ('nic'), and the actual cost to the 
patient ('act_cost'). Whenever working with a new data set, it can be useful to calculate summary statistics to develop 
a feeling for the volume and character of the data. This makes it easier to spot trends and significant features during
further stages of analysis.

Calculate the sum, mean, standard deviation, and quartile statistics for each of these quantities. Format your results 
for each quantity as a list: [sum, mean, standard deviation, 1st quartile, median, 3rd quartile]. We'll create a tuple 
with these lists for each quantity as a final result.
"""

from math import sqrt


def describe(key):

    total = 0
    avg = 0
    s = 0
    q25 = 0
    med = 0
    q75 = 0

    number_items = len(SCRPTS)
    list_items = []

    for scrpt in SCRPTS:
        total += scrpt[key]
        list_items.append(scrpt[key])

    avg = total / number_items
    variance = 0
    for scrpt in SCRPTS:
        variance += (scrpt[key] - avg) ** 2
    s = sqrt(variance/number_items)

    list_items.append(11)

    ordered_items = sorted(list_items)
    median_index = int(len(ordered_items) / 2)
    lfq = []
    ltq = []
    if len(ordered_items) % 2 == 0:
        med = (ordered_items[median_index - 1] + ordered_items[median_index]) / 2
        lfq = ordered_items[:median_index]
        ltq = ordered_items[median_index:]
    else:
        med = ordered_items[median_index]
        lfq = ordered_items[:median_index]
        ltq = ordered_items[median_index + 1:]

    lfq_mi = int(len(lfq) / 2)
    if len(lfq) % 2 == 0:
        q25 = (lfq[lfq_mi - 1] + lfq[lfq_mi]) / 2
    else:
        q25 = lfq[lfq_mi]

    ltq_mi = int(len(ltq) / 2)
    if len(ltq) % 2 == 0:
        q75 = (ltq[ltq_mi - 1] + ltq[ltq_mi]) / 2
    else:
        q75 = ltq[ltq_mi]

    return (total, avg, s, q25, med, q75)


summary = [('items', describe('items')),
           ('quantity', describe('quantity')),
           ('nic', describe('nic')),
           ('act_cost', describe('act_cost'))]

"""
Question 2: most_common_item

Often we are not interested only in how the data is distributed in our entire data set, but within particular groups --
 for example, how many items of each drug (i.e. 'bnf_name') were prescribed? Calculate the total items prescribed for 
 each 'bnf_name'. What is the most commonly prescribed 'bnf_name' in our data?

To calculate this, we first need to split our data set into groups corresponding with the different values of 
'bnf_name'. Then we can sum the number of items dispensed within in each group. Finally we can find the largest sum.

We'll use 'bnf_name' to construct our groups. You should have 5619 unique values for 'bnf_name'.
"""


def bnf_drugs(litems):
    bnfs = set()
    for item in litems:
        bnfs.add(item['bnf_name'])
    return bnfs


bnf_names = bnf_drugs(SCRPTS)
#assert(len(bnf_names) == 999)
assert(len(bnf_names) == 5619)

"""
We want to construct "groups" identified by 'bnf_name', where each group is a collection of prescriptions 
(i.e. dictionaries from scripts). We'll construct a dictionary called groups, using bnf_names as the keys. 
We'll represent a group with a list, since we can easily append new members to the group. To split our scripts into 
groups by 'bnf_name', we should iterate over scripts, appending prescription dictionaries to each group as 
we encounter them.
"""


simple_groups = {name: [] for name in bnf_names}

for script in SCRPTS:
    simple_groups[script['bnf_name']].append(script)

"""
Now that we've constructed our groups we should sum up 'items' in each group and find the 'bnf_name' with 
the largest sum. The result, max_item, should have the form [(bnf_name, item total)], e.g. [('Foobar', 2000)].
"""


def get_max_item(groups):
    max_item = [('', 0)]
    quant = 0
    for item in groups.items():
        for key in item[1]:
            quant += key['items']
        if quant > max_item[0][1]:
            del max_item[0]
            max_item.append((item[0], quant))
        elif quant == max_item[0][1]:
            if max_item[0][0] > item[0]:
                del max_item[0]
                max_item.append((item[0], quant))
        quant = 0
    return max_item


max_item_ = get_max_item(simple_groups)
#assert max_item_ == [('Omeprazole_Cap E/C 20mg', 344)]
assert max_item_ == [('Omeprazole_Cap E/C 20mg', 113826)]


"""
Challenge: 
Write a function that constructs groups as we did above. The function should accept a list of dictionaries 
(e.g. scripts or practices) and a tuple of fields to groupby (e.g. ('bnf_name') or ('bnf_name', 'post_code')) 
and returns a dictionary of groups. The following questions will require you to aggregate data in groups, so this 
could be a useful function for the rest of the miniproject.
"""


def group_by_field(data, fields):
    groups = {}
    for elements in data:
        for field in fields:
            f = elements.get(field)
            if f:
                item = groups.get(elements[field])
                if not item:
                    groups[elements[field]] = []
                groups[elements[field]].append(elements)
    return groups


gotten_groups = group_by_field(SCRPTS, ('bnf_name', ))

assert sorted(simple_groups) == sorted(gotten_groups)

test_max_item = get_max_item(gotten_groups)

assert test_max_item == max_item_

"""
Question 3: postal_totals

Our data set is broken up among different files. This is typical for tabular data to reduce redundancy. 
Each table typically contains data about a particular type of event, processes, or physical object. 
Data on prescriptions and medical practices are in separate files in our case. If we want to find the total items 
prescribed in each postal code, we will have to join our prescription data (scripts) to our clinic data (practices).

Find the total items prescribed in each postal code, representing the results as a list of tuples (post code, 
total items prescribed). Sort your results ascending alphabetically by post code and take only results from the 
first 100 post codes. Only include post codes if there is at least one prescription from a practice in that post code.

NOTE: Some practices have multiple postal codes associated with them. Use the alphabetically first postal code.

We can join scripts and practices based on the fact that 'practice' in scripts matches 'code' in practices. 
However, we must first deal with the repeated values of 'code' in practices. We want the alphabetically 
first postal codes.
"""


def get_practices_pc(practices):
    practice_postal = {}
    for practice in practices:
        if practice['code'] in practice_postal:
            if practice_postal[practice['code']] > practice['post_code']:
                practice_postal[practice['code']] = practice['post_code']
        else:
            practice_postal[practice['code']] = practice['post_code']
    return practice_postal

practice_postal = get_practices_pc(PRCTCS)

assert practice_postal['A81048'] == 'TS11 7BL'

"""
Challenge: This is an aggregation of the practice data grouped by practice codes. 
Write an alternative implementation of the above cell using the group_by_field function you defined previously.
"""

"""
Now we can join practice_postal to scripts.
"""


def join_cp(scripts, postals):
    for scrpt in scripts:
        join = postals.get(scrpt['practice'])
        if join:
            scrpt['post_code'] = postals[scrpt['practice']]
    return scripts


joined = join_cp(SCRPTS, practice_postal)

#assert scripts_wpostals[len(scripts_wpostals)-1]['post_code'] == 'TS18 1HU'


"""
Finally we'll group the prescription dictionaries in joined by 'post_code' and sum up the items prescribed in each 
group, as we did in the previous question.
"""

items_by_post = group_by_field(joined, ('post_code',))


def get_sum_item(groups):
    sum_item = []
    quant = 0
    for item in groups.items():
        for key in item[1]:
            quant += key['items']
        sum_item.append((item[0], quant))
        quant = 0
    return sum_item


all_postal_totals = get_sum_item(items_by_post)

#assert sums == [('TS18 2AW', 2), ('TS18 1HU', 3)]

sorted_apt = sorted(all_postal_totals)
postal_totals = sorted_apt[:100]


"""
Question 4: items_by_region

Now we'll combine the techniques we've developed to answer a more complex question. Find the most commonly dispensed 
item in each postal code, representing the results as a list of tuples (post_code, bnf_name, amount dispensed as 
proportion of total). Sort your results ascending alphabetically by post code and take only results from the first 100 
post codes.

NOTE: We'll continue to use the joined variable we created before, where we've chosen the alphabetically first postal 
code for each practice. Additionally, some postal codes will have multiple 'bnf_name' with the same number of items 
prescribed for the maximum. In this case, we'll take the alphabetically first 'bnf_name'.

Now we need to calculate the total items of each 'bnf_name' prescribed in each 'post_code'. Use the techniques we 
developed in the previous questions to calculate these totals. You should have 141196 ('post_code', 'bnf_name') groups.
"""

def items_pc_bnf(scripts):
    pc_bnf = {}
    for script in scripts:
        pc = script['post_code']
        bnf = script['bnf_name']
        q = script['items']
        tupla = (pc, bnf)
        old_bnf = pc_bnf.get(tupla)
        if old_bnf:
            q += pc_bnf[tupla]
        pc_bnf[tupla] = q
    return pc_bnf


total_items_by_bnf_post = items_pc_bnf(joined)
assert len(total_items_by_bnf_post) == 141196

"""
Let's use total_items to find the maximum item total for each postal code. To do this, we will want to regroup 
total_items_by_bnf_post by 'post_code' only, not by ('post_code', 'bnf_name'). First let's turn total_items into a 
list of dictionaries (similar to scripts or practices) and then group it by 'post_code'. You should have 118 groups in 
the resulting total_items_by_post after grouping total_items by 'post_code'.
"""

total_items = joined
total_items_by_post = group_by_field(total_items, ('post_code', ))

assert len(total_items_by_post) == 118

"""
Now we will aggregate the groups in total_by_item_post to create max_item_by_post. Some 'bnf_name' have the same item 
total within a given postal code. Therefore, if more than one 'bnf_name' has the maximum item total in a given postal 
code, we'll take the alphabetically first 'bnf_name'. We can do this by sorting each group according to the item 
total and 'bnf_name'.
"""

def get_max_item_by_post(groups):
    max_items = {}
    for item in groups.items():
        quant = 0
        pc = item[0]
        bnftupl = {}
        bnfgroup = group_by_field(item[1], ('bnf_name', ))
        max_item = get_max_item(bnfgroup)
        max_items[pc] = max_item[0]
    return max_items


max_item_by_post = get_max_item_by_post(total_items_by_post)
# print(max_item_by_post)


"""
In order to express the item totals as a proportion of the total amount of items prescribed across all 'bnf_name' in a 
postal code, we'll need to use the total items prescribed that we previously calculated as items_by_post. Calculate 
the proportions for the most common 'bnf_names' for each postal code. Format your answer as a list of 
tuples: [(post_code, bnf_name, total)]
"""


# # sorted_apt total all items by postal code
# # max_item_by_post item max in postal code


def get_items_by_region(items_by_post, max_items_by_post):
    items_by_region = []
    for (post_code, total) in items_by_post:
        bnf, maxim = max_items_by_post[post_code]
        proportion = maxim / total
        triple = (post_code, bnf, proportion)
        items_by_region.append(triple)
    return items_by_region


items_by_region = sorted(get_items_by_region(sorted_apt, max_item_by_post))

print(len(items_by_region))
print(items_by_region[:100])




def searchfor(arrNumbers, search):
    quant = 0
    for number in arrNumbers:
        if number == search:
            quant += 1
    return quant

arrNum = [2, 3, 4, 3, 2, 1]

assert searchfor(arrNum, 3)




arrNum.count(3)