# Class Planet

The ```Planet``` class allows to model a planet with a given monetary system and inhabitants with a certain amount of money. It allows to calculate the different possible combinations of coins and bills that can be obtained with the given amount of money and the possible purchase options.

<p align="center">
<img src="MonetaryPlanet/child-6902674.png" alt="Planet.png" width=30%/>
</p>



## Using the class
To use the ```Planet```class, you must first create an instance of this class by specifying the values of its attributes: ```monetary_system``` and ```money```.

``` python
monetary_system = [1, 2, 5, 10, 20, 50, 100, 200]
money = 15
planet = Planet(monetary_system, money)
```

Then, you can call the methods of the class to get the desired information.

``` python
# Get all possible combinations of coins and bills for the given amount of money.
combinations = planet.get_possible_wallet_combinations()

# Get all possible combinations of coins and bills that allow to pay a given amount without giving change.
purchases = planet.get_possible_purchases()
```

## Example

``` python
# Create an instance of the Planet class
monetary_system = [1, 2, 5, 10, 20, 50, 100, 200]
money = 10
planet = Planet(monetary_system, money)

# Get all possible combinations of coins and bills for the given amount of money.
combinations = planet.get_possible_wallet_combinations()
print(f"Possible combinations for {money} euros : {combinations}")

# Get all possible combinations of coins and bills that allow to pay a given amount without giving change.
purchases = planet.get_possible_purchases()
print(f"Possible purchases without giving change: {purchases}")
```

Output:

```
Possible combinations for 10 euros : [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1, 5], [1, 1, 1, 1, 1, 2, 2], [1, 1, 1, 1, 2, 5], [1, 1, 1, 2, 2, 2], [1, 1, 1, 5, 2], [1, 1, 2, 2, 5], [1, 1, 5, 5], [1, 2, 2, 5], [2, 2, 2, 2, 2], [2, 2, 2, 5], [2, 2, 5, 5], [5, 5]]
Possible purchases without giving change: [10]
```