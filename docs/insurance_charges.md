It's another day in America - you wake up, enjoy some coffee to fight through that morning groginess, and crack open the paper. After your normal routine, it's time to start your day, and you head outside to warm your vehicle up to get to work. As you take your first step, the ground beneath you disappears and a sinkhole eats your entire right leg, then immediately closes. It looks like the ground has become sentient and has a craving for legs, but only right legs oddly enough. It happens so fast you can't react, but when your brain catches up with what is happening, you scramble away from the sinkhole. This isn't good - you need to go to the hospital, but the thought of that potential hospital bill makes you faint. After a moment, you regain consciousness and decide that it's ok; you have health insurance, and it can't be that bad. What does a sinkhole-bite replacement surgery cost, anyway? As your leg continues to bleed and you really need to get to the hospital, your curious nature continues to preoccupy you, and you can't help but wonder: do you know the price of *anything* at a hospital? Is there a way to know how much I'm going to pay before hand?

These are all great questions that an unfortunate number of Americans don't have the answer to. And while none of us are going to be eaten by a sentient sinkhole tomorrow (I hope), you never know what the day may bring and if a hospital visit is included. Even more nebulous is the cost of that visit, both to you and insurance provider, and what you end up with. Throughout this read, we're going to explore what factors about an individual relate to their average hospital charges, how well can we can predict these charges based off of those factors, and drawing conclusions.

### What data will we be using?

For this article, we'll be using a dataset from the book `Machine Learning with R by Brett Lantz` - specifically, this book provides a dataset that has medical billing data. The columns in this dataset contain an individual's `age`, `sex`, `bmi`, number of `children`, `smoker`, `region` of the U.S., and the amount their insurance was billed, or `charges`. This dataset is relatively simple - it's purpose is almost entirely educational. This matches the purpose of this article, to explore the basics of data visualization and predictive modeling.

### Exploring the data

Looking at the attributes available, we can start by visualizing how each one is directly correlated to the `charges` column. To do this, we can create bar charts for the non-continuous variables, which are `sex`, `children`, `smoker`, and `region`. For the continuous variables, `age` and `bmi`, we can review line charts that display the average cost to insurance and identify what the trend is for these variables.


#### Sex

![Sex vs average charges](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/sex_avg.png)

Looking at the first categorical variable, `sex` groups the average cost of medical charges by male and female. We don't immediately see any extreme difference - males are, on average, charged a little higher, although it's a fairly small difference.

#### Number of children

![Number of children vs average charges](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/children_avg.png)

Next, we have number of `children`. Here we can more of a disparity between groups, but not in the way one might expect - individuals with 0 children have smaller bills charged to insurance, on average, than individuals with 1 child. The same applies for individuals with 1 child to individuals with 2 children, and the same for individuals with 2 kids vs individuals with 3 kids. However, people with 4 and 5 kids are billed less on average than their counterparts with fewer kids. So we can't call this a linear correlation, but still an interesting trend. The reason for this could be indirect, or something entirely unrelated to having kids.

#### Smoker vs non smoker

![Smoker vs average charges](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/smoker_avg.png)

Now we take a look at `smoker` vs non smoker groups. The difference is pretty shocking - smokers' insurance are billed roughly **4x** as much as their non-smoking counterparts. Smoking has been proven to be extremely unhealthy, and the lifestyle can impact medical costs heavily, as seen here.

#### Regions

![Region vs average charges](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/region_avg.png)

Last for categorical variables is the `regions`. We have a breakdown of 4 groups - northeast, northwest, southeast, and southwest. In the bar chart above, there are no strong differences between any region. Similar to sex, we do see some range on the averages presented, but there are far too many factors to be able to say what causes this, and the difference is fairly minimal.

#### Age

![Age vs average charges](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/age_avg.png)

Moving on to the first of our continuous variables, we have `age`. The trend for this shows that as age increases, so do the average medical costs billed. This may seem to make complete sense, but there are additional considerations mentioned below that don't fall into the scope of this dataset.

#### BMI

![BMI vs average charges](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/bmi_avg.png)

Lastly, we have `bmi`, or body mass index. This is measured as a person's weight divided by their height. In the chart above, we can see a strong upward trend; as BMI increases, so does the average medical cost billed.


##### Thoughts
Shown above, we can see some trends that we would expect to see - that smoking, age, and BMI are all heavily impactful on medical costs. However, the dataset provided here is limited in scope. While it would be easy to assume that age directly increases medical costs on average, this data is looking at the amount charged to insurance. So for a younger population who may not have insurance, or may not be comfortable going to a doctor and will wait 10 years before the problem is unignorable, we may not have a fully accurate representation of these features vs medical costs.

To get a better understanding of what group of features may be most responsible for higher bills, we can split this data in deciles based on the amount charged to insurance, then take the top 10% decile and get a row count for each possible group of features. Because the number of features is so small, this is possible for us, but it wouldn't normally be if there were more columns or more possible values for the columns we have. 

#### Highest average bills



After getting the top 10% most expensive charges, which is `134 rows` of data with an average charge amount of `$42,378` and getting the number of possible combinations of features out of our 6 columns, the total comes to `88,320` different unique groups of features. The table below lists what features are most commonly seen, and in how many rows that value is seen.

| Age | Sex | BMI | # Children | Smoker | Region |
| ---- | ---- | ---- | ---- | ---- | ---- |
|Age 37: 7<br/>Age 43: 66<br/>Age 22: 5<br/>Age 60: 5<br/>Age 44: 5 | Male: 84<br/>Female: 50 | 36 BMI: 18<br/>34 BMI: 15<br/>31 BMI: 13<br/>37 BMI: 12<br/>35 BMI: 11 | 0 children: 48<br/>2 children: 34<br/>1 child: 31<br/>3 children: 19<br/>4 children: 2<br/> | Smoker: 131<br/>Non-smoker: 3 | Southeast: 55<br/>Southwest: 32<br/>Northeast: 27<br/>Northwest: 20 |

Some interesting trends to be seen in the table above - for example, almost every individual in the top 10% are smokers. Additionally, without making the page significantly longer, most of the expensive bills have a BMI that labels them as "obese". On the other side of the spectrum, the age was fairly diverse, except for 43 year olds - this is likely just due to natural aging, as well as the sample mostly comprising of this age range.

#### Lowest average bills

After getting the bottom 10% least expensive charges, which is `134 rows` of data with an average charge amount of `$1,796` and getting the number of possible combinations of features out of our 6 columns, the total comes to `6,264` different unique groups of features. The table below lists what features are most commonly seen, and in how many rows that value is seen.

| Age | Sex | BMI | # Children | Smoker | Region |
| ---- | ---- | ---- | ---- | ---- | ---- |
|Age 18: 46<br/>Age 19: 38<br/>Age 21: 14<br/>Age 20: 12<br/>Age 22: 12 | Male: 82<br/>Female: 52 | 26 BMI: 9<br/>30 BMI: 9<br/>34 BMI: 8<br/>29 BMI: 8<br/>28 BMI: 7 | 0 children: 118<br/>1 child: 15<br/>2 children: 1| Smoker: 0<br/>Non-smoker: 134 | Southeast: 47<br/>Southwest: 38<br/>Northeast: 25<br/>Northwest: 25 |

A lot of what we saw in highest cost billed matches for this table as well - this is likely due to how large a sample size is out of the entire population. For example, we can see still more males fall into the bottom 10% of bills than females, and still more individuals from the southeast. However, we also see that the lower age ranges (18-22) are the most common ages for cheapest bills. Additionally, the BMI ranges are slightly lower, and there are absolutely no smokers.

### Predictive modeling

After exploring the data and understanding that some features can impact the medical bill more than others, let's see if we can create some probabilstic modeling - first, we can start with a basic feed forward neural network, and see if any other regression models or probabilstic models can perform better.

#### Neural network

For the neural network, we're going to start by creating an attention model with encoder and decoder layers, and provide multiple transformation layers to... actually, we don't need to do any of that. While AI has been getting incredibly popular and we've made some truly impressive advancements, this is a simple dataset. There's no need to build a crazy network - let's start with a basic model using `tensorflow`.

We'll start by importing our libraries and preprocessing our data using `sklearn`:
```python
#Preprocess data - #Start by converting string to int
df['sex'] = pd.Categorical(df['sex']).codes
df['children'] = pd.Categorical(df['children']).codes
df['smoker'] = pd.Categorical(df['smoker']).codes
df['region'] = pd.Categorical(df['region']).codes

#Create transformer
transformer = make_column_transformer(
    (MinMaxScaler(), ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'])
)

#Transform and split data
transformer.fit(df)
data = transformer.transform(df)

#Split data
y_data = data[:,-1]
X_data = df.iloc[:,:-1]

test_size = 100
X_train, X_test = X_data[:-test_size], X_data[-test_size:]
y_train, y_test = y_data[:-test_size], y_data[-test_size:]
```

In just a few lines of code, we've preprocessed our data to scale between 0 and 1 using the `MinMaxScaler` of sklearn, and split the data into train samples and 100 test samples. Now, we can make our model - we can create a basic 3 layer network, with a batch size of 8 and 50 epochs. We'll use the standard `Adam` optimizer, as well as `relu` activations on each layer except the last - the reason for this is `relu` will prevent negative output from coming through, and some predictions could potentially be negative.

```python
#Create model
model = Sequential()
model.add(Dense(256, input_shape=(X_data.shape[1],), activation="relu"))
model.add(Dense(128, activation="relu"))
model.add(Dense(1))

#Compile and fit model
model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(), metrics='mse')
model.fit(X_train, y_train, batch_size=8, epochs=50)
```

Great! We've run our model, let's see what our mean squared error is to check the accuracy of our model, and how our predictions look.

![nn_mse](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/nn_mse.png)

These are impressive results - we can see that the predictions of the model almost exactly match that of the true labels. The overall mean squared error here is only 0.01405. For many projects, these results would be above passing and could work for many applications - but can we do better?

#### Ensemble methods

With the `sklearn` library available, we can use over 200 different kinds of estimators. This article could be a lot longer if we wanted to step through each one. Instead, we'll use a few basic `ensemble` methods. Ensembles are groups of classifiers that work together to achieve better performance, and can often perform better than large independent classifiers. These are great for regression too - the ensemble methods we'll use `AdaBoost`, `RandomForest`, and `GradientBoost`.

Sklearn also makes it incredibly easy to use any of these models. The below code will create the different ensembles, fit and train them, then create predictions
```python
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor, GradientBoostingRegressor

ensembles = [AdaBoostRegressor(), RandomForestRegressor(), GradientBoostingRegressor()]
for e in ensembles:
    e.fit(X_train, y_train)
    preds = e.predict(X_test)
```

Now that we have our ensemble methods fit and predicting, let's see how they did

![adaboost_mse](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/adaboost_mse.png)
![gradientboost_mse](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/gradientboost_mse.png)
![randomforest_mse](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/randomforest_mse.png)

Once again, these results are ideal, and they even outperformed the neural network! While the MSE for the neural network was roughly 0.01405, each of these is significantly lower, with the RandomForest dropping under 0.004. With no doubt, if better results were necessary, some hyperparameter optimization and other fine tuning could push this mean squared error value even lower.

### Conclusions

After having a bad start to your day and having your leg eaten by a sinkhole, you were faced with the dilemma - what factors go into medical costs? Am I likely to be charged more? To be honest, we can't answer that very well - no one has ever had their leg eaten by a sinkhole like this before. However, we can make some confident predictions based on your `age`, `sex`, whether you are a `smoke`, and `BMI` as to what your average bill will be. Additionally, we can better understand what information would be beneficial in continuing this exploration of medical prices, such as what group is more likely to have insurance, what group is more likely to actually go to the doctor if there is an issue, etc. With this information in hand, you feel prepared to tackle the day. You are now 10 minutes late for work after reading this. Sorry about that.