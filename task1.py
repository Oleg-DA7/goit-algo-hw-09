# Маємо набір монет [50, 25, 10, 5, 2, 1]. Уявіть, що ви розробляєте систему для касового апарату, яка повинна визначити оптимальний спосіб видачі решти покупцеві.
#
#
# Необхідно написати дві функції для касової системи, яка видає решту покупцеві:
#
# Функція жадібного алгоритму find_coins_greedy. Ця функція повинна приймати суму, яку потрібно видати покупцеві, 
# і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми. 
# Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.
#
# Функція динамічного програмування find_min_coins. Ця функція також повинна приймати суму для видачі решти, 
# але використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет, необхідних для формування цієї суми. 
# Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим способом. 
# Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}


def find_coins_greedy(s, denominations):
    used = {}
    remain = s
    denominations = sorted(denominations, reverse = True)

    for d in denominations:
        if remain >= d: 
            count = remain // d
            remain -= d * count 
            if count > 0:
                used[d] = count
        
    if remain == 0: 
        return sum(used.values()), used
    else:
        return float('inf'), {}
        

def find_min_coins(amount, denominations):
    dp = [float('inf')] * (amount + 1)    
    dp[0] = 0  
    used = [{} for _ in range(amount + 1)]
    denominations = sorted(denominations)

    for i in range(1, amount + 1):
        for d in denominations:
            if d <= i:
                dp[i] = min(dp[i], dp[i - d] + 1)
                used[i] = used[i - d].copy()
                used[i][d] = used[i].get(d, 0) + 1

    return dp[amount],  used[amount] if dp[amount] != float('inf') else []


def main():
    denominations = [50, 25, 10, 5, 2, 1]
    amount = 113
    
    count, combination = find_min_coins(amount, denominations)
    
    print('Динамичне програмування.')
    if count == float('inf'):
        print(f"Неможливо видати суму {amount} з даними номіналами")
    else:
        print(f"Мінімальна кількість монет для суми {amount}: {count}")
        print(f"Комбінація монет: {combination}")

    gcount, gcombination = find_coins_greedy(amount, denominations)

    print('Жадібний алгоритм.')
    if gcount == float('inf'):
        print(f"Неможливо видати суму {amount} з даними номіналами")
    else:
        print(f"Мінімальна кількість монет для суми {amount}: {gcount}")
        print(f"Комбінація монет: {gcombination}")


if __name__ == "__main__":
    main()