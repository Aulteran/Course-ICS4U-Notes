# 09/20/23

## FILTER
# Filter erquires (funtion: return, iterable)
nums=[1,2,3,4]

even= list(filter(lambda x: x%2==0, nums))
print(even)

odd= list(filter(lambda x: x%2!=0, nums))
print(odd)

data=list(range(1,120))
mean= st.mean(data)
print(mean)

above_avg= list(filter(lambda x: x>mean,data))
print(above_avg)

p_u_30= ['Lamello','Tom','Gainnis','Ja','Justin','Alfonso','Sexy Red','Young Boy']

p_5= tuple(filter(lambda x: len(x)>5,p_u_30))
print(p_5)

## MAP
# Map iterate over every item and takes 2 parameters and then retuns an idicator that applies the funtion to evry item iterable

nums = list(range(1,10))
print(nums)

sq_nums = list(map(lambda x: x ** 2, nums))
print(sq_nums)

even2 = list(map(lambda x: x % 2 == 0, nums))
print(even2)

wc_teams = [('Brazil',21),
            ('Germany',19),
            ('Italy',18),
            ('Argentina',17),
            ('France',15),
            ('England',15)]

# Create new list with incrementedd # of times teams appeared
appearances = list(map(lambda x: (x[0], x[1] + 1), wc_teams))
print(appearances)