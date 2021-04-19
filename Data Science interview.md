```python
import pandas as pd
import math
```


```python
use_data = pd.read_csv('Eluvio_DS_Challenge.csv')
```


```python
use_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time_created</th>
      <th>date_created</th>
      <th>up_votes</th>
      <th>down_votes</th>
      <th>title</th>
      <th>over_18</th>
      <th>author</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1201232046</td>
      <td>2008-01-25</td>
      <td>3</td>
      <td>0</td>
      <td>Scores killed in Pakistan clashes</td>
      <td>False</td>
      <td>polar</td>
      <td>worldnews</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1201232075</td>
      <td>2008-01-25</td>
      <td>2</td>
      <td>0</td>
      <td>Japan resumes refuelling mission</td>
      <td>False</td>
      <td>polar</td>
      <td>worldnews</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1201232523</td>
      <td>2008-01-25</td>
      <td>3</td>
      <td>0</td>
      <td>US presses Egypt on Gaza border</td>
      <td>False</td>
      <td>polar</td>
      <td>worldnews</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1201233290</td>
      <td>2008-01-25</td>
      <td>1</td>
      <td>0</td>
      <td>Jump-start economy: Give health care to all</td>
      <td>False</td>
      <td>fadi420</td>
      <td>worldnews</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1201274720</td>
      <td>2008-01-25</td>
      <td>4</td>
      <td>0</td>
      <td>Council of Europe bashes EU&amp;UN terror blacklist</td>
      <td>False</td>
      <td>mhermans</td>
      <td>worldnews</td>
    </tr>
  </tbody>
</table>
</div>



Based on looks alone, it looks like this data is taken from reddit. I can tell from the up votes and downvotes. All of them under then thread regarding world news. The variables taken into account are the data created, number of up and down votes, titels, whether the content is open to those over 18 years old and the author. 

# Clean and Tidy the Data


```python
use_data[use_data.category != 'worldnews']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time_created</th>
      <th>date_created</th>
      <th>up_votes</th>
      <th>down_votes</th>
      <th>title</th>
      <th>over_18</th>
      <th>author</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



Getting rid of the category column since they are all worldnews


```python
use_data = use_data.drop(columns = ['category'])
use_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time_created</th>
      <th>date_created</th>
      <th>up_votes</th>
      <th>down_votes</th>
      <th>title</th>
      <th>over_18</th>
      <th>author</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1201232046</td>
      <td>2008-01-25</td>
      <td>3</td>
      <td>0</td>
      <td>Scores killed in Pakistan clashes</td>
      <td>False</td>
      <td>polar</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1201232075</td>
      <td>2008-01-25</td>
      <td>2</td>
      <td>0</td>
      <td>Japan resumes refuelling mission</td>
      <td>False</td>
      <td>polar</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1201232523</td>
      <td>2008-01-25</td>
      <td>3</td>
      <td>0</td>
      <td>US presses Egypt on Gaza border</td>
      <td>False</td>
      <td>polar</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1201233290</td>
      <td>2008-01-25</td>
      <td>1</td>
      <td>0</td>
      <td>Jump-start economy: Give health care to all</td>
      <td>False</td>
      <td>fadi420</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1201274720</td>
      <td>2008-01-25</td>
      <td>4</td>
      <td>0</td>
      <td>Council of Europe bashes EU&amp;UN terror blacklist</td>
      <td>False</td>
      <td>mhermans</td>
    </tr>
  </tbody>
</table>
</div>



Separate the data into two tables: The news stories safe for minors or not safe.


```python
over_18 = use_data[use_data.over_18 == True].drop(columns = ['over_18'])
under_18 = use_data[use_data.over_18 == False].drop(columns = ['over_18'])
```


```python
over_18
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time_created</th>
      <th>date_created</th>
      <th>up_votes</th>
      <th>down_votes</th>
      <th>title</th>
      <th>author</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1885</th>
      <td>1206381438</td>
      <td>2008-03-24</td>
      <td>189</td>
      <td>0</td>
      <td>Pics from the Tibetan protests - more graphic ...</td>
      <td>pressed</td>
    </tr>
    <tr>
      <th>6721</th>
      <td>1211138718</td>
      <td>2008-05-18</td>
      <td>5</td>
      <td>0</td>
      <td>MI5 linked to Max Mosley’s Nazi-style, sadomas...</td>
      <td>alllie</td>
    </tr>
    <tr>
      <th>8414</th>
      <td>1212694925</td>
      <td>2008-06-05</td>
      <td>0</td>
      <td>0</td>
      <td>Tabloid Horrifies Germany: Poland s Yellow Pre...</td>
      <td>stesch</td>
    </tr>
    <tr>
      <th>12163</th>
      <td>1216672016</td>
      <td>2008-07-21</td>
      <td>0</td>
      <td>0</td>
      <td>Love Parade Dortmund: Techno Festival Breaks R...</td>
      <td>stesch</td>
    </tr>
    <tr>
      <th>12699</th>
      <td>1217381380</td>
      <td>2008-07-30</td>
      <td>5</td>
      <td>0</td>
      <td>IDF kills young Palestinian boy. Potentially N...</td>
      <td>cup</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>503776</th>
      <td>1477889966</td>
      <td>2016-10-31</td>
      <td>4</td>
      <td>0</td>
      <td>Latest Italian Earthquake Devastates Medieval ...</td>
      <td>pixelinthe</td>
    </tr>
    <tr>
      <th>508067</th>
      <td>1479400229</td>
      <td>2016-11-17</td>
      <td>12</td>
      <td>0</td>
      <td>ISIS Release Video Showing Melbourne As A Poss...</td>
      <td>halacska</td>
    </tr>
    <tr>
      <th>508176</th>
      <td>1479434681</td>
      <td>2016-11-18</td>
      <td>0</td>
      <td>0</td>
      <td>Animal welfare activists have released footage...</td>
      <td>NinjaDiscoJesus</td>
    </tr>
    <tr>
      <th>508376</th>
      <td>1479492875</td>
      <td>2016-11-18</td>
      <td>6</td>
      <td>0</td>
      <td>Jungle Justice : Public lynching of a street ...</td>
      <td>avivi_</td>
    </tr>
    <tr>
      <th>508706</th>
      <td>1479641575</td>
      <td>2016-11-20</td>
      <td>0</td>
      <td>0</td>
      <td>[NSFW] Teenage boy run over by  Iraqi army tan...</td>
      <td>atyzer</td>
    </tr>
  </tbody>
</table>
<p>320 rows × 6 columns</p>
</div>




```python
under_18
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time_created</th>
      <th>date_created</th>
      <th>up_votes</th>
      <th>down_votes</th>
      <th>title</th>
      <th>author</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1201232046</td>
      <td>2008-01-25</td>
      <td>3</td>
      <td>0</td>
      <td>Scores killed in Pakistan clashes</td>
      <td>polar</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1201232075</td>
      <td>2008-01-25</td>
      <td>2</td>
      <td>0</td>
      <td>Japan resumes refuelling mission</td>
      <td>polar</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1201232523</td>
      <td>2008-01-25</td>
      <td>3</td>
      <td>0</td>
      <td>US presses Egypt on Gaza border</td>
      <td>polar</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1201233290</td>
      <td>2008-01-25</td>
      <td>1</td>
      <td>0</td>
      <td>Jump-start economy: Give health care to all</td>
      <td>fadi420</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1201274720</td>
      <td>2008-01-25</td>
      <td>4</td>
      <td>0</td>
      <td>Council of Europe bashes EU&amp;UN terror blacklist</td>
      <td>mhermans</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>509231</th>
      <td>1479816764</td>
      <td>2016-11-22</td>
      <td>5</td>
      <td>0</td>
      <td>Heil Trump : Donald Trump s  alt-right  white...</td>
      <td>nonamenoglory</td>
    </tr>
    <tr>
      <th>509232</th>
      <td>1479816772</td>
      <td>2016-11-22</td>
      <td>1</td>
      <td>0</td>
      <td>There are people speculating that this could b...</td>
      <td>SummerRay</td>
    </tr>
    <tr>
      <th>509233</th>
      <td>1479817056</td>
      <td>2016-11-22</td>
      <td>1</td>
      <td>0</td>
      <td>Professor receives Arab Researchers Award</td>
      <td>AUSharjah</td>
    </tr>
    <tr>
      <th>509234</th>
      <td>1479817157</td>
      <td>2016-11-22</td>
      <td>1</td>
      <td>0</td>
      <td>Nigel Farage attacks response to Trump ambassa...</td>
      <td>smilyflower</td>
    </tr>
    <tr>
      <th>509235</th>
      <td>1479817346</td>
      <td>2016-11-22</td>
      <td>1</td>
      <td>0</td>
      <td>Palestinian wielding knife shot dead in West B...</td>
      <td>superislam</td>
    </tr>
  </tbody>
</table>
<p>508916 rows × 6 columns</p>
</div>



Looking at just the titles for each subgroup of reddit posts, I want to see if the title could be a good indicator of what could be classified as 18+. I decided to find a csv file that contains certain words that may be classifed as 18+.


```python
import csv
file_swears = open('swearWords.csv')
data_swears = csv.reader(file_swears)
restricted_words = list(data_swears)[0]
# restricted_words (not gonna show because the words may be triggering)
```


```python
swears = '|'.join(restricted_words)
```


```python
over_18['title_lower'] = over_18['title'].str.lower()
under_18['title_lower'] = under_18['title'].str.lower()
```


```python
over_18_swears = over_18.title_lower.str.contains(swears)
under_18_swears = under_18.title_lower.str.contains(swears)
```

Now I will perform and 2 prop Hypothesis Test.


```python
x1 = over_18_swears.sum()
n1 = len(over_18_swears)
p1 = over_18_swears.mean()
print(x1)
print(n1)
print(p1)
```

    134
    320
    0.41875



```python
x2 = under_18_swears.sum()
n2 = len(under_18_swears)
p2 = under_18_swears.mean()
print(x2)
print(n2)
print(p2)
```

    95027
    508916
    0.18672433171682556


Ho: p1 = p2 (There **is not** difference between the proportion of posts that are 18+ and those that are not that contain cenosored words)

vs.

H1: p1 != p2 (There **is** a difference between the proportion of posts that are 18+ and those that are not that contain censored words)


```python
pooled_p = (p1*n1 + p2*n2)/(n1+n2)
pooled_p
```




    0.18687013486870527




```python
z = (p1-p2)/math.sqrt(pooled_p*(1-pooled_p)*((1/n1)+(1/n2)))
z
```




    10.644484137073835



# Conclusion
With a z-value greater than 1.96 (the significance level at alpha = 0.05), we reject the null hypothesis. There is a difference between the proportion of posts that are 18+ and those that are not that contain censored words. Approximately 42% of the posts labeled as 18+ contained a censored word in the title while approximately 18.69% of the under 18 posts contained those words. 

Although there is a significant difference between the proportions, it is also pretty interesting how 95,000+ posts classified as safe for minors contained swear words in the title. Because of this, I dont think the title of the post could solely predict whether the rating is restricted or not. If I had more time and more access to all the variables, I'd like to predict this using a machine learning model. 
