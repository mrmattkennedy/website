It's another day in America - you wake up, enjoy some coffee to fight through that morning groginess, and crack open the paper. After your normal routine, it's time to start your day, and you head outside to warm your vehicle up to get to work. As you take your first step, the ground beneath you disappears and a sinkhole eats your entire right leg, then immediately closes. It looks like the ground has become sentient and has a craving for legs, but only right legs oddly enough. It happens so fast you can't react, but when your brain catches up with what is happening, you scramble away from the sinkhole. This isn't good - you need to go to the hospital, but the thought of that potential hospital bill makes you faint. After a moment, you regain consciousness and decide that it's ok; you have health insurance, and it can't be that bad. What does a sinkhole-bite replacement surgery cost, anyway? As your leg continues to bleed and you really need to get to the hospital, your curious nature continues to preoccupy you, and you can't help but wonder: do you know the price of *anything* at a hospital? Is there a way to know how much I'm going to pay before hand?

These are all great questions that an unfortunate number of Americans don't have the answer to. And while none of us are going to be eaten by a sentient sinkhole tomorrow (I hope), you never know what the day may bring, and if a hospital visit is included. Even more nebulous is the cost of that visit, both to your insurance provider, and what you end up with. Throughout this read, we're going to explore what factors about an individual relate to their average hospital charges, how well can we can predict these charges based off of those factors, and what you can do to help reduce your hospital bill charges.

### What data will we be using?

For this article, we'll be using a dataset from the book `Machine Learning with R by Brett Lantz` - specifically, this book provides a dataset that has medical billing data. The columns in this dataset contain an individual's `age`, `sex`, `bmi`, `number of children`, `smoker`, `region of the U.S.`, and the `amount their insurance was billed`. This dataset is relatively simple - it's purpose is almost entirely educational. This matches the purpose of this article, to explore the basics of data visualization and predictive modeling.

### Exploring the data

Look into most expensive bills - what were most common features of 10% most expensive and bottom 10% least expensive?

Looking at the attributes available, we can start by visualizing how each one is directly correlated to the `charges` column. To do this, we can create bar charts for the non-continuous variables, which are `sex`, `children`, `smoker`, and `region`. For the continuous variables, `age` and `bmi`, we can review line charts that display the average cost to insurance and identify what the trend is for these variables.


#### Sex

![Sex vs average charges](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/sex_avg.png)

Looking at the first categorical variable, `sex` groups the average cost of medical charges by male and female. We don't immediately see any extreme difference - males are, on average, charged a little higher, it's a fairly small difference.

#### Number of children

![Number of children vs average charges](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/children_avg.png)

Next, we have number of `children`. Here we can more of a disparity between groups, but not in the way one might expect - individuals with 0 children have smaller bills charged to insurance, on average, than individuals with 1 child. The same applies for individuals with 1 child to individuals with 2 children, and the same for individuals with 2 kids vs individuals with 3 kids. However, people with 4 and 5 kids are billed less on average than their counterparts with fewer kids. So we can't call this a linear correlation, but still an interesting trend. The reason for this could be indirect, or something entirely unrelated to having kids.

#### Smoker vs non smoker

![Smoker vs average charges](https://raw.githubusercontent.com/mrmattkennedy/TH-Medical-Charges/main/extras/figures/smoker_avg.png)

Now we take a look at `smoker` vs non smoker groups. The difference is pretty shocking - smokers' insurance are billed roughly **4x** as much as their non-smoking counterparts. Smoking has been proven to be extremely unhealthy, and the lifestyle can impact medical costs heavily, as seen here.

#### Regons

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


#### Highest average bills

To get a better understanding of what group of features may be most responsible for higher bills, we can split this data in deciles based on the amount charged to insurance, then take the top 10% decile and get a row count for each possible group of features. Because the number of features is so small, this is possible for us, but it wouldn't normally be if there were more columns or more possible values for the columns we have. After getting the top 10% most expensive charges, which is `134 rows` of data with an average charge amount of `$42,378` and getting the number of possible combinations of features out of our 6 columns, the total comes to `88,320` different unique groups of features. The table below lists what features are most commonly seen, and in how many rows that value is seen.

| Method      | Description                          |
| ----------- | ------------------------------------ |
| Age        | :material-check:     Fetch resource  |
| Sex        | :material-check-all: Update resource |
| BMI        | :material-close:     Delete resource |
| # Children | :material-close:     Delete resource |
| Smoker     | :material-close:     Delete resource |
| Region     | :material-close:     Delete resource |

### Data modeling

### What can I do to reduce my bill?


