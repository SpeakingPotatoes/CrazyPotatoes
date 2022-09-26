#%%
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"] 
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

term_dict = {}
for term in terms:
    key, value = term.split(" ")
    term_dict[key] = value

expirations = []
for privacy in privacies:
    key, value = privacy.split(" ")
    term = int(term_dict[value])
    date = list(map(int, key.split(".")))
    date[1] += term
    day = str(date[2]).zfill(2)
    month = str(date[1] % 12).zfill(2)
    year = str(date[1] // 12 + date[0])
    expirations.append(".".join([year, month, day]))

res = [int(today >= expiration) for expiration in expirations]
answer = []
for i, r in enumerate(res):
    if r == True:
        answer.append(i+1)
    
    
    

# %%
user = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

sale_rates = [0.4, 0.3, 0.2, 0.1]
user_rates = [u[0] * 0.01 for u in user]

user_prices = [u[1] for u in user]

max_sale = max(user_rates)
min_sale = min(user_rates)
sales = [sale_rate for sale_rate in sale_rates if sale_rate >= min_sale and sale_rate <= max_sale]

emoticon_prices = []
for emoticon in emoticons:
    a = []
    for sale in sales:
        a.append(emoticon * (1-sale))

for a in [1, 2, 3]:
    for b in [0,1, 2]:
        print(a,b)
        

        (1-sale) * emoticon
    prices = [emoticon * (1 - sale) for emoticon in emoticons]
    emoticon_prices .append(prices)


    
#%%
def solution(commands):
    answer = []
    df = [["" for _ in range(50)] for _ in range(50)]
    for command in commands:
        command = command.split(" ")
        if command[0] == "UPDATE":
            if len(command) == 4:
                r, c, val = command[1:]
                r = int(r)
                c = int(c)
                df = update(df, r, c, val)
            else:
                in_val, new_val = command[1:]
                df = update(df, new_value=new_val, in_value=in_val)

        elif command[0] == "MERGE":
            r1, c1, r2, c2 = command[1:]
            r1 = int(r1)
            r2 = int(r2)
            c1 = int(c1)
            c2 = int(c2)
            df = merge(df, r1, c1, r2, c2)

        elif command[0] == "UNMERGE":
            r, c = command[1:]
            r = int(r)
            c = int(c)
            df = unmerge(df, r, c)

        elif command[0] == "PRINT":
            r, c = command[1:]
            r = int(r)
            c = int(c)
            value = print_cell(df, r, c)
            answer.append(value)
        
    return answer


def update(df, r=None, c=None, new_value=None, in_value=None):
    if in_value != None:
        for r_idx, series in enumerate(df):
            for c_idx, value in enumerate(series):
                if in_value in value:
                    df[r_idx][c_idx] = value.replace(in_value, new_value)
    
    else:
        old_value = df[r-1][c-1]
        if old_value == "":
            df[r-1][c-1] = new_value
        else: 
            if len(old_value.split("_")) != 1:
                new_value = new_value + "_" + old_value.split("_")[1]
            for r_idx, series in enumerate(df):
                for c_idx, value in enumerate(series):
                    if value == old_value:
                        df[r_idx][c_idx] = new_value

    return df


def merge(df, r1, c1, r2, c2):
    value = df[r1-1][c1-1]
    if len(value.split("_")) == 1:
        value = f"{value}_{r1}{c1}"
    df[r1-1][c1-1] = value
    df[r2-1][c2-1] = value

    return df


def unmerge(df, r, c):
    old_value = df[r-1][c-1]
    new_value = old_value.split("_")[0]
    for r_idx, series in enumerate(df):
        for c_idx, value in enumerate(series):
            if value == old_value:
                df[r_idx][c_idx] = ""
    df[r-1][c-1] = new_value

    return df


def print_cell(df, r, c):
    value = df[r-1][c-1].split("_")[0]
    if value == "": value = "EMPTY"

    return value
    
#%%
df = [["" for _ in range(50)] for _ in range(50)]

df = update(df, 1, 1, "menu")
df = update(df, 1, 2, "category")
df = update(df, 2, 1, "bibimbap")
df = update(df, 2, 2, "korean")
df = update(df, 2, 3, "rice")
df = update(df, 3, 1, "ramyeon")
df = update(df, 3, 2, "korean")
df = update(df, 3, 3, "noodle")
df = update(df, 3, 4, "instant")
df = update(df, 4, 1, "pasta")
df = update(df, 4, 2, "italian")
df = update(df, 4, 3, "noodle")

df = merge(df, 1, 2, 1, 3)
df = merge(df, 1, 3, 1, 4)

df = update(df, new_value="hansik", in_value="korean")
df = update(df, 1, 3, "group")

df = unmerge(df, 1, 4)

print_cell(df, 1,3)
print_cell(df, 1,4)
# %%
commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
solution(commands)
#%%
format(111, "b")
res = []
num = 
def 
res.append(num % 2)

num  //= 2 
print(num)
res.reverse()
# %%
def decimal2binary(num):
    bin = []
    while num != 0:
        bin.append(str(num % 2))
        num //= 2
    bin.reverse()
    if len(bin) % 2 == 0:
        bin = ["0"] + bin
    bin = "".join(bin)

    return bin


decimal2binary(7)
decimal2binary(5)
decimal2binary(63)
decimal2binary(111)
tmp = decimal2binary(95)
mid(tmp)

cen = len(tmp) // 2
tmp[:cen]
tmp[cen+1:]

tmp = "101110110110100"


# %%
