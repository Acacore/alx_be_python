weather = input("What's the weather like today? (sunny/rainy/cold): \n")

if weather.lower() == 'sunny':
    print('Wear a t-shirt and sunglasses.\n')

elif weather.lower() == 'rainy':
    print("Don't forget your umbrella and a raincoat.\n")

elif weather.lower() == 'cold':
    print("Make sure to wear a warm coat and a scarf.\n")

else:
    print("Sorry, I don't have recommendations for this weather./n")