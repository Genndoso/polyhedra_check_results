import pandas as pd




if __name__ == '__main__':
    wallets = list(pd.read_csv("wallets.txt", sep = " ", header = None).astype(str)[0])
    wallets = [x.lower() for x in wallets]
    sum_r = 0
    winning_wallets = []
    for num in [1000,30,15,10,5]:
        res = list(pd.read_csv(f"{num}b.txt",header = None)[0]) 
        res = [x.lower() for x in res]
        f = [x.lower() for x in wallets if x in res]
        winning_wallets.extend(f)
        sum_r += num*len(f)

    print(f'Суммарный профит = {sum_r}$')

    
    with open('winning_w.txt', 'w') as f:
        for w in winning_wallets:
            f.write(w + '\n')