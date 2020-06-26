#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

def recMC(coinValueList,change):
   print(change)

   if change == 62:
       return
   min_coins = change
   if change in coinValueList:
       return 1
   else:
       for coin in coinValueList:
           if coin <= change:
               num_coins = 1 + recMC(coinValueList, change - coin)
               if num_coins < min_coins:
                   min_coins = num_coins
   return min_coins

#print(recMC([1,5,10,25],63))


def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

print(recDC([1,5,10,25],63,[0]*64))
