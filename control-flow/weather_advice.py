question = input("What's the weather like today? (sunny/rainy/cold): \n")

if question.lower() == 'sunny':
    print('Wear a t-shirt and sunglasses.\n')

elif question.lower() == 'rainy':
    print("Don't forget your umbrella and a raincoat.\n")

elif question.lower() == 'cold':
    print("Make sure to wear a warm coat and a scarf.\n")

else:
    print("Sorry, I don't have recommendations for this weather./n")