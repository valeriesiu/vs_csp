#VS, memory diagram

name="Alex"
age=14

print(f"The variable name has the value of {name} and is saved at {id(name)}")
print(f"The variabe age has the value of {age} and is saved at {id(age)}")

score=10
print(f"The variable score has the value of {score} and is saved at {id(score)}")
score=25 
print(f"The variable score has the value of {score} and is saved at {id(score)}")

height=5.9
city="Denver"
zip_code=80202
print(f"The variable height has a value of {height} and is saved at {id(height)}")
print(f"The variable city has a value of {city} and is saved at {id(city)}")
print(f"The variable zip code has a value of {zip_code} and is saved at {id(zip_code)}")

price1=10
print(f"The variable price 1 has a value of {price1} and is saved at {id(price1)}")
price2=10.0
print(f"The variable price 2 has a value of {price2} and is saved at {id(price2)}")