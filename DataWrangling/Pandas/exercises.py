
import pandas as pd

with open('./data/201701scripts_sample.csv', 'rb') as f:
    scripts = pd.read_csv(f)

# print(scripts.head())

col_names = ['code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
with open('./data/practices.csv', 'rb') as f:
    practices = pd.read_csv(f, header=None)
practices.columns = col_names

# print(practices.head())

with open('./data/chem.csv', 'rb') as f:
    chem = pd.read_csv(f)

# print(chem.head())


'''
Question 1: summary_statistics
In the PW miniproject we first calculated the total, mean, standard deviation, and quartile statistics of the 'items', 
'quantity'', 'nic', and 'act_cost' fields. To do this we had to write some functions to calculate the statistics and 
apply the functions to our data structure. The DataFrame has a describe method that will calculate most (not all) of 
these things for us.

Submit the summary statistics to the grader as 
a list of tuples: [('act_cost', (total, mean, std, q25, median, q75)), ...]
'''

scr_desc = scripts.describe()
# print(scr_desc)

sum_items = ('items',
                (sum(scripts['items']), scr_desc['items']['mean'], scr_desc['items']['std'],
                 scr_desc['items']['25%'], scr_desc['items']['50%'], scr_desc['items']['75%'],))

sum_nic = ('nic',
                (sum(scripts['nic']), scr_desc['nic']['mean'], scr_desc['nic']['std'],
                 scr_desc['nic']['25%'], scr_desc['nic']['50%'], scr_desc['nic']['75%'],))

sum_act_cost = ('act_cost',
                (sum(scripts['act_cost']), scr_desc['act_cost']['mean'], scr_desc['act_cost']['std'],
                 scr_desc['act_cost']['25%'], scr_desc['act_cost']['50%'], scr_desc['act_cost']['75%'],))

sum_quantity = ('quantity',
                (sum(scripts['quantity']), scr_desc['quantity']['mean'], scr_desc['quantity']['std'],
                 scr_desc['quantity']['25%'], scr_desc['quantity']['50%'], scr_desc['quantity']['75%'],))

summary_stats = [sum_items, sum_quantity, sum_nic, sum_act_cost]
# print(summary_stats)

assert summary_stats == [('items', (8888304, 9.133135976111625, 29.204198282803603, 1.0, 2.0, 6.0)),
                         ('quantity', (721457006, 741.3298348837282, 3665.426958467915, 28.0, 100.0, 350.0)),
                         ('nic', (71100424.84000827, 73.05891517920908, 188.070256906825, 7.8, 22.64, 65.0)),
                         ('act_cost', (66164096.11999956, 67.98661326170655, 174.40170332301963, 7.33, 21.22, 60.67))]


'''
Question 2: most_common_item

We can also easily compute summary statistics on groups within the data. In the pw miniproject we had to explicitly
construct the groups based on the values of a particular field. Pandas will handle that for us via the groupby method.
This process is detailed in the Pandas documentation.

Use groupby to calculate the total number of items dispensed for each 'bnf_name'. Find the item with the highest total
and return the result as [(bnf_name, total)].
'''

scrpts_by_bnf_names = scripts.groupby('bnf_name').agg({'items': 'sum'})\
    .sort_values('items', ascending=False).reset_index()
# print(scrpts_by_bnf_names.head())
most_common_item = [(scrpts_by_bnf_names['bnf_name'][0], scrpts_by_bnf_names['items'][0])]
# print(most_common_item)

assert most_common_item == [('Omeprazole_Cap E/C 20mg', 218583)]


'''
Question 3: items_by_region

Now let's find the most common item by post code. The post code information is in the practices DataFrame, 
and we'll need to merge it into the scripts DataFrame. Pandas provides extensive documentation with diagrammed 
examples on different methods and approaches for joining data. The merge method is only one of many possible options.

Return your results as a list of tuples (post code, item name, amount dispensed as % of total). Sort your results 
ascending alphabetically by post code and take only results from the first 100 post codes.

NOTE: Some practices have multiple postal codes associated with them. Use the alphabetically first postal code. 
Note some postal codes may have multiple 'bnf_name' with the same prescription rate for the maximum. In this case, 
take the alphabetically first 'bnf_name' (as in the PW miniproject).
'''

# items_by_region = [("B11 4BW", "Salbutamol_Inha 100mcg (200 D) CFF", 0.0310589063)] * 100

one_prct = practices.sort_values('post_code').groupby('code').first().reset_index()
one_prct.columns = ['practice', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
scripts_pc = scripts.merge(one_prct, on=['practice']).sort_values('bnf_name')
# print(scripts_pc)

items_by_post = scripts_pc.groupby('post_code').agg({'items': 'sum'}).sort_values('items', ascending=False)
# print(items_by_post)

max_item_by_post = scripts_pc.groupby(['post_code', 'bnf_name']).sum()['items'].\
    groupby('post_code', group_keys=False).nlargest(1).reset_index()
# print(max_item_by_post)

items_by_region = []

for i in range(100):
    pc = max_item_by_post['post_code'][i]
    bnf = max_item_by_post['bnf_name'][i]
    items = max_item_by_post['items'][i]
    total_items_in_pc = items_by_post.loc[pc]['items']
    proportion = items / total_items_in_pc
    items_by_region.append((pc, bnf, proportion))

# print(items_by_region)
assert items_by_region == [('B11 4BW', 'Salbutamol_Inha 100mcg (200 D) CFF', 0.031058906339360346), ('B12 9LP', 'Paracet_Tab 500mg', 0.02489310607391788), ('B18 7AL', 'Salbutamol_Inha 100mcg (200 D) CFF', 0.027111371172225472), ('B21 9RY', 'Metformin HCl_Tab 500mg', 0.03329358300834757), ('B23 6DJ', 'Lansoprazole_Cap 30mg (E/C Gran)', 0.021384456106529576), ('B61 0AZ', 'Omeprazole_Cap E/C 20mg', 0.028713318284424378), ('B70 7AW', 'Paracet_Tab 500mg', 0.025135992162726547), ('B72 1RL', 'Omeprazole_Cap E/C 20mg', 0.020228765092141495), ('B8 1RZ', 'Metformin HCl_Tab 500mg', 0.021347750961484866), ('B9 5PU', 'Ventolin_Evohaler 100mcg (200 D)', 0.024826024522257815), ('B90 3LX', 'Omeprazole_Cap E/C 20mg', 0.026965103983080718), ('BA5 1XJ', 'Omeprazole_Cap E/C 20mg', 0.028261290947858113), ('BB11 2DL', 'Omeprazole_Cap E/C 20mg', 0.027381741821396993), ('BB2 1AX', 'Omeprazole_Cap E/C 20mg', 0.03428191046763188), ('BB3 1PY', 'Omeprazole_Cap E/C 20mg', 0.032683395995453356), ('BB4 5SL', 'Omeprazole_Cap E/C 20mg', 0.03747689029549087), ('BB4 7PL', 'Omeprazole_Cap E/C 20mg', 0.027477496877557173), ('BB7 2JG', 'Omeprazole_Cap E/C 20mg', 0.027980664806967485), ('BB8 0JZ', 'Atorvastatin_Tab 20mg', 0.021515746650768042), ('BB9 7SR', 'Omeprazole_Cap E/C 20mg', 0.02247662283190644), ('BD16 4RP', 'Lansoprazole_Cap 30mg (E/C Gran)', 0.022780283004198414), ('BD19 5AP', 'Lansoprazole_Cap 30mg (E/C Gran)', 0.02066220372715759), ('BD3 8QH', 'Atorvastatin_Tab 40mg', 0.031662850096882154), ('BD4 7SS', 'Atorvastatin_Tab 40mg', 0.03424183501960914), ('BH14 0DJ', 'Omeprazole_Cap E/C 20mg', 0.02838931332218254), ('BH18 8EE', 'Omeprazole_Cap E/C 20mg', 0.027092370049064923), ('BH23 3AF', 'Omeprazole_Cap E/C 20mg', 0.03546099290780142), ('BL1 3RG', 'Omeprazole_Cap E/C 20mg', 0.03362566656383588), ('BL1 8TU', 'Omeprazole_Cap E/C 20mg', 0.027729220222793487), ('BL2 6NT', 'Omeprazole_Cap E/C 20mg', 0.0271567320510379), ('BL3 5HP', 'Omeprazole_Cap E/C 20mg', 0.03129933420275929), ('BL9 0NJ', 'Omeprazole_Cap E/C 20mg', 0.032037565382786494), ('BL9 0SN', 'Omeprazole_Cap E/C 20mg', 0.03090454288711369), ('BN1 6AG', 'Lansoprazole_Cap 15mg (E/C Gran)', 0.021755523716160168), ('BN1 8DD', 'Aspirin Disper_Tab 75mg', 0.021517850460294887), ('BN9 9PW', 'Omeprazole_Cap E/C 20mg', 0.01855317763853853), ('BR2 9GT', 'Influenza_Vac Inact 0.5ml Pfs', 0.04301700334253742), ('BR3 3FD', 'Omeprazole_Cap E/C 20mg', 0.02865911645197545), ('BS16 3TD', 'Omeprazole_Cap E/C 20mg', 0.03752737892431249), ('BS23 3HQ', 'Omeprazole_Cap E/C 20mg', 0.030246216399367518), ('BS4 1WH', 'Omeprazole_Cap E/C 20mg', 0.029600778967867575), ('BS4 4HU', 'Omeprazole_Cap E/C 20mg', 0.037361354349095155), ('BS48 2XX', 'Omeprazole_Cap E/C 20mg', 0.030207346595095254), ('CA11 8HW', 'Omeprazole_Cap E/C 20mg', 0.027868623340321454), ('CB22 3HU', 'Omeprazole_Cap E/C 20mg', 0.038775726713346066), ('CB9 8HF', 'Omeprazole_Cap E/C 20mg', 0.03391110538046382), ('CH1 4DS', 'Lansoprazole_Cap 30mg (E/C Gran)', 0.0257736189772634), ('CH41 8DB', 'Omeprazole_Cap E/C 20mg', 0.03327732469980738), ('CH44 5UF', 'Omeprazole_Cap E/C 20mg', 0.03327334826839032), ('CH62 5HS', 'Omeprazole_Cap E/C 20mg', 0.037778835690968446), ('CH62 6EE', 'Influenza_Vac Inact 0.5ml Pfs', 0.057585894269547), ('CH65 6TG', 'Lansoprazole_Cap 30mg (E/C Gran)', 0.026067517902474142), ('CH66 3PB', 'Lansoprazole_Cap 30mg (E/C Gran)', 0.03100619319552803), ('CM18 6LY', 'Omeprazole_Cap E/C 20mg', 0.026445315758738635), ('CR0 0JA', 'Salbutamol_Inha 100mcg (200 D) CFF', 0.021571724750715768), ('CT11 8AD', 'Omeprazole_Cap E/C 20mg', 0.022307039864291774), ('CV1 4FS', 'Omeprazole_Cap E/C 20mg', 0.028455180531743392), ('CV12 8NQ', 'Omeprazole_Cap E/C 20mg', 0.026444799282852902), ('CV21 2DN', 'Omeprazole_Cap E/C 20mg', 0.04102890311294875), ('CV6 2FL', 'Omeprazole_Cap E/C 20mg', 0.036250663502669624), ('CV6 6DR', 'Omeprazole_Cap E/C 20mg', 0.030544721504009817), ('CW1 3AW', 'Omeprazole_Cap E/C 20mg', 0.03558258199497268), ('CW5 5NX', 'Omeprazole_Cap E/C 20mg', 0.03453647138997736), ('CW7 1AT', 'Omeprazole_Cap E/C 20mg', 0.03666371289322109), ('DA1 2HA', 'Omeprazole_Cap E/C 20mg', 0.019244977658938185), ('DA11 8BZ', 'Amoxicillin_Cap 500mg', 0.019686834904226208), ('DN16 2AB', 'Amlodipine_Tab 5mg', 0.019925280199252802), ('DN22 7XF', 'Simvastatin_Tab 40mg', 0.018624361621210474), ('DN31 3AE', 'Omeprazole_Cap E/C 20mg', 0.03432952436761402), ('DN34 4GB', 'Omeprazole_Cap E/C 20mg', 0.03709507845509909), ('DN6 0HZ', 'Paracet_Tab 500mg', 0.025764099668243102), ('DN8 4BQ', 'Lansoprazole_Cap 30mg (E/C Gran)', 0.021703061442945835), ('DY11 6SF', 'Omeprazole_Cap E/C 20mg', 0.021081859317153433), ('E15 4ES', 'Amlodipine_Tab 10mg', 0.02569068641412703), ('E7 0EP', 'Metformin HCl_Tab 500mg', 0.037244933982913224), ('FY2 0JG', 'Omeprazole_Cap E/C 20mg', 0.03627638093657511), ('FY4 1TJ', 'Omeprazole_Cap E/C 20mg', 0.04334478808705613), ('FY5 2TZ', 'Omeprazole_Cap E/C 20mg', 0.03540407051009112), ('FY5 3LF', 'Omeprazole_Cap E/C 20mg', 0.035122866094073016), ('FY7 8GU', 'Omeprazole_Cap E/C 20mg', 0.032058079778122195), ('FY8 5DZ', 'Omeprazole_Cap E/C 20mg', 0.02969960416717259), ('GL1 3PX', 'Omeprazole_Cap E/C 20mg', 0.025687801991914012), ('GL20 5GJ', 'Omeprazole_Cap E/C 20mg', 0.02412690753362688), ('GL50 4DP', 'Omeprazole_Cap E/C 20mg', 0.024009042366605605), ('GU9 9QS', 'Omeprazole_Cap E/C 20mg', 0.027052485943893322), ('HA0 4UZ', 'Metformin HCl_Tab 500mg', 0.027855843941147297), ('HA3 7LT', 'Omeprazole_Cap E/C 20mg', 0.02504635488712953), ('HD6 1AT', 'Lansoprazole_Cap 30mg (E/C Gran)', 0.021017471736896196), ('HG1 5AR', 'Omeprazole_Cap E/C 20mg', 0.02842489568845619), ('HR1 2JB', 'Omeprazole_Cap E/C 20mg', 0.028529603122966818), ('HR6 8HD', 'Omeprazole_Cap E/C 20mg', 0.027207967812149594), ('HU7 4DW', 'Salbutamol_Inha 100mcg (200 D) CFF', 0.025607843137254904), ('HU9 2LJ', 'Lansoprazole_Cap 30mg (E/C Gran)', 0.0243192109011288), ('IG7 4DF', 'Amlodipine_Tab 5mg', 0.01956475808155504), ('IP22 4WG', 'Omeprazole_Cap E/C 20mg', 0.02851095218241878), ('KT12 3LB', 'Omeprazole_Cap E/C 20mg', 0.01828471919895516), ('KT14 6DH', 'Amlodipine_Tab 5mg', 0.018667887710894296), ('KT16 8HZ', 'Amlodipine_Tab 5mg', 0.019319714781268066), ('KT6 6EZ', 'Omeprazole_Cap E/C 20mg', 0.02821316614420063), ('L31 0DJ', 'Omeprazole_Cap E/C 20mg', 0.029425653739448675)]


'''
Question 4: script_anomalies

Drug abuse is a source of human and monetary costs in health care. A first step in identifying practitioners that 
enable drug abuse is to look for practices where commonly abused drugs are prescribed unusually often. 
Let's try to find practices that prescribe an unusually high amount of opioids. 
The opioids we'll look for are given in the list below.

'''

opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']

'''
These are generic names for drugs, not brand names. Generic drug names can be found using the 'bnf_code' field in 
scripts along with the chem table.. Use the list of opioids provided above along with these fields to make a new 
field in the scripts data that flags whether the row corresponds with a opioid prescription.
'''

scripts_chem = scripts.merge(chem, left_on='bnf_code', right_on='CHEM SUB')
# print(scripts_chem.head())
'''
Now for each practice calculate the proportion of its prescriptions containing opioids.

Hint: Consider the following list: [0, 1, 1, 0, 0, 0]. What proportion of the entries are 1s? What is the mean value?
'''

# gets an attribute and search in opioid list if its opioid
def is_opioid(att_name):
    for opioid in opioids:
        res = opioid in att_name
        if res:
            return True
    return False

# Creates a DF with only is_opioid and adds it to main DF
is_opioid_script = scripts_chem['NAME'].apply(is_opioid)
scripts_chem['is_opioid'] = is_opioid_script
# print(scripts_chem)

# Filter only opioids in main DF
scripts_opioids = scripts_chem[scripts_chem['is_opioid']]
# print(scripts_opioids)

# Adds all items by practice
items_by_practice = scripts_chem.groupby('practice').agg({'items': 'sum'})
# print(items_by_practice)

# Gets total opioids by practice
opioids_by_practice = scripts_opioids.groupby('practice').agg({'items': 'sum'}).reset_index()
# print(opioids_by_practice)


# Function to apply in opioids_proportion_by_practice
# Gets proportion = total opioids by practice divided by total items by practice
def get_proportion_by_total_items(serie):
    practice = serie['practice']
    items = serie['items']
    total = items_by_practice.loc[practice]['items']
    proportion = items / total
    return practice, proportion


# From total opioids by practice apply function to get proportion for all items by practice
opioids_per_practice = opioids_by_practice.apply(get_proportion_by_total_items, axis=1)
# print(opioids_proportion_by_practice)

'''
How do these proportions compare to the overall opioid prescription rate? Subtract off the proportion of all 
prescriptions that are opioids from each practice's proportion.
'''

# relative_opioids_per_practice = ...

'''
Now that we know the difference between each practice's opioid prescription rate and the overall rate, 
we can identify which practices prescribe opioids at above average or below average rates. However, 
are the differences from the overall rate important or just random deviations? In other words, are the differences 
from the overall rate big or small?

To answer this question we have to quantify the difference we would typically expect between a given practice's 
opioid prescription rate and the overall rate. This quantity is called the standard error, and is related to the 
standard deviation,  σσ . The standard error in this case is

standard_deviation/squre(n)
 
where  nn  is the number of prescriptions each practice made. Calculate the standard error for each practice. 
Then divide relative_opioids_per_practice by the standard errors. We'll call the final result opioid_scores.
'''

# standard_error_per_practice = ...
# opioid_scores = ...

'''
The quantity we have calculated in opioid_scores is called a z-score:

(X-μ) / squre( (std_dev^2) /n)

Here  X  corresponds with the proportion for each practice,  μ  corresponds with the proportion across all practices,
std_dev^2  corresponds with the variance of the proportion across all practices, and  n  is the number of prescriptions
made by each practice.
Notice  X  and  n  will be different for each practice, while  μ  and  std_dev  are determined across all prescriptions, 
and so are the same for every z-score. The z-score is a useful statistical tool used for hypothesis testing, 
finding outliers, and comparing data about different types of objects or events.

Now that we've calculated this statistic, take the 100 practices with the largest z-score. 
Return your result as a list of tuples in the form (practice_name, z-score, number_of_scripts). 
Sort your tuples by z-score in descending order. Note that some practice codes will correspond with multiple names. 
In this case, use the first match when sorting names alphabetically.

'''

# unique_practices = ...
# anomalies = [("NATIONAL ENHANCED SERVICE", 11.6958178629, 7)] * 100

'''

This resuls are copy

'''
practices.columns = ['code', 'name', 'addr_1', 'addr_2', 'borough', 'village', 'post_code']
practices = practices[['code', 'name']].sort_values (by = ['name'], ascending = True)
practices = practices [~practices.duplicated(['code'])]
opioids = ['morphine', 'oxycodone', 'methadone', 'fentanyl', 'pethidine', 'buprenorphine', 'propoxyphene', 'codeine']


check = '|'.join(opioids)
chem_df1 = chem
chem_df1 [ 'test' ] = chem_df1 [ 'NAME' ].apply ( lambda x: any ( [ k in x.lower() for k in opioids ] ) )
key2 = chem_df1 [ "test" ] == True
chem_df1 = chem_df1 [ key2 ]
chem_sub = list (chem_df1['CHEM SUB'])


scripts['opioid'] = scripts [ 'bnf_code' ].apply(lambda x: 1 if x in chem_sub else 0)
std_devn = scripts.opioid.std ()
overall_rate = scripts.opioid.mean()

scripts = scripts.merge (practices, left_on = 'practice', right_on = 'code')
scripts['cnt'] = 0


opioids_per_practice = scripts.groupby ( [ 'practice', 'name' ], as_index = False ).agg ( { 'opioid': 'mean', 'cnt': 'count' } )
opioids_per_practice.drop_duplicates()

opioids_per_practice['opioid'] = opioids_per_practice ['opioid'] - overall_rate

opioids_per_practice['std_err'] = std_devn / opioids_per_practice['cnt'] ** 0.5
opioids_per_practice['z_score'] = opioids_per_practice['opioid'] / opioids_per_practice['std_err']

result = opioids_per_practice[['name', 'z_score', 'cnt']]


result.sort_values(by = 'z_score', ascending = False, inplace = True)
anomalies = [(k[1], k[2], k[3]) for k in result.itertuples()][:100]



'''
Question 5: script_growth

Another way to identify anomalies is by comparing current data to historical data. 
In the case of identifying sites of drug abuse, we might compare a practice's current rate of opioid prescription 
to their rate 5 or 10 years ago. Unless the nature of the practice has changed, the profile of drugs they prescribe 
should be relatively stable. We might also want to identify trends through time for business reasons, identifying drugs 
that are gaining market share. That's what we'll do in this question.

We'll load in beneficiary data from 6 months earlier, June 2016, and calculate the percent growth in prescription 
rate from June 2016 to January 2017 for each bnf_name. We'll return the 50 items with largest growth and the 50 
items with the largest shrinkage (i.e. negative percent growth) as a list of tuples sorted by growth rate in 
descending order in the format (script_name, growth_rate, raw_2016_count). You'll notice that many of the 50 fastest 
growing items have low counts of prescriptions in 2016. Filter out any items that were prescribed less than 50 times.

'''

# scripts16 = ...
# script_growth = [("Butec_Transdermal Patch 5mcg\/hr", 3.4677419355, 62.0)] * 100

'''

This results are copy

'''

scripts16 = pd.read_csv('./dw-data/201606scripts_sample.csv.gz',compression='gzip', delimiter=',')
drugs_16 = scripts16[['bnf_name', 'items']]
drugs_16 = drugs_16.groupby('bnf_name').count().reset_index()
drugs_16.columns = ['bnf_name', 'count16']

drugs_17 = scripts[['bnf_name', 'items']]
drugs_17 = drugs_17.groupby('bnf_name').count().reset_index()
drugs_17.columns = ['bnf_name', 'count17']

drugs = drugs_16.merge(drugs_17, on='bnf_name', how='inner')
drugs = drugs[drugs['count16']>=50]

drugs.is_copy=False
drugs['growth'] = ((drugs['count17']-drugs['count16'])/drugs['count16'])
drugs = drugs[['bnf_name', 'growth', 'count16']]
drugs.sort_values('growth', ascending=False, inplace=True)
drugs_final = pd.concat([drugs.iloc[:50], drugs.iloc[-50:]], axis=0)

script_growth=drugs_final


'''
Question 6: rare_scripts

Does a practice's prescription costs originate from routine care or from reliance on rarely prescribed treatments? 
Commonplace treatments can carry lower costs than rare treatments because of efficiencies in large-scale production. 
While some specialist practices can't help but avoid prescribing rare medicines because there are no alternatives, 
some practices may be prescribing a unnecessary amount of brand-name products when generics are available. 
Let's identify practices whose costs disproportionately originate from rarely prescribed items.

First we have to identify which 'bnf_code' are rare. To do this, find the probability  pp  of a prescription 
having a particular 'bnf_code' if the 'bnf_code' was randomly chosen from the unique options in the beneficiary data. 
We will call a 'bnf_code' rare if it is prescribed at a rate less than  0.1p0.1p .
'''

# p = ...
# rates = ...
# rare_codes = ...
# scripts['rare'] = ...

'''
Now for each practice, calculate the proportion of costs that originate from prescription of rare treatments 
(i.e. rare 'bnf_code'). Use the 'act_cost' field for this calculation.
'''

# rare_cost_prop = ...

'''
Now we will calculate a z-score for each practice based on this proportion. First take the difference of 
rare_cost_prop and the proportion of costs originating from rare treatments across all practices.
'''

# relative_rare_cost_prop = ...

'''
Now we will estimate the standard errors (i.e. the denominator of the z-score) by simply taking the standard 
deviation of this difference.
'''

# standard_errors = ...

'''
Finally compute the z-scores. Return the practices with the top 100 z-scores in the form 
(post_code, practice_name, z-score). Note that some practice codes will correspond with multiple names. 
In this case, use the first match when sorting names alphabetically.
'''

# rare_scores = ...
# rare_scripts = [("Y03472", "CONSULTANT DIABETES TEAM", 16.2626871247)] * 100

'''
This results are copy
'''

rates = scripts['bnf_code'].value_counts() / scripts['bnf_name'].count()

rates.head()

p = 1. /scripts['bnf_code'].nunique()

mask = rates < .1 * p

rare_codes = rates[mask].index

scripts['rare'] = scripts['bnf_code'].isin(rare_codes)

scripts.head()

rare_cost_prop = (scripts[scripts['rare']].groupby('practice')['act_cost'].sum()/ scripts.groupby('practice')['act_cost'].sum()).fillna(0)

rare_cost_prop.head()

cost_all = scripts[scripts['rare']]['act_cost'].sum() / scripts['act_cost'].sum()

relative_rare_cost_prop = rare_cost_prop - cost_all

standard_errors = relative_rare_cost_prop.std()

z_score = relative_rare_cost_prop / standard_errors

z_score = pd.DataFrame(z_score.sort_values(ascending = False))

z_score.reset_index(inplace = True)

z_score.columns = ['practice', 'z_score']

fin = (practices.groupby(['code'])[['code', 'name']]).head() #

result = z_score.merge(fin, how = 'left', left_on = 'practice',right_on = 'code').drop('code', axis = 1)

df = result.groupby('practice').first().sort_values('z_score', ascending = False).reset_index()[:100]

rare_scripts = list(zip(df.practice, df.name, df.z_score))