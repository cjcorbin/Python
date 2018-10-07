# Function "pay" to find a pair of Bitcoin in a list whose sum = targetAmt with the lowest difference between the pair

def pay(btcList, targetAmt):

    if len(btcList) < 2 or (len(btcList) == 2 and sum(btcList) != targetAmt):
        return
    elif len(btcList) == 2 and sum(btcList) == targetAmt:
        print(btcList)
        return
    seen = set()
    output = ()
    for btc in btcList:
        targetMatch = targetAmt - btc
        if targetMatch not in seen:
            seen.add(btc)
        elif (output == () or output[2] > (max(btc, targetMatch) - min(btc, targetMatch))):
                output = (min(btc, targetMatch), max(btc, targetMatch), (max(btc, targetMatch) - min(btc, targetMatch)))

    #output contains the pair as well as difference between pair. Printing just the pair here:
    print(output[0:2])

#Use case:
arr = [0.1, 0.2, 0.01, 0.7, 0.6, 0.11, 0.68, 0.03, 0.35, 0.36]
pay(arr, 0.71)

