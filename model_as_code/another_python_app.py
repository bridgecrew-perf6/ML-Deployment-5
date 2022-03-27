#import model_as_code/house_price_predictor

model_object = HousePricePredictor()

model_object.predict_price(2)


import os
command = 'python house_price_predictor_2.py --distance 1'
os.system(command)

class HousePricePredictor:
    
    def __init__(self):
        print("Prediction started")
    
    def predict_price(self, distance):
        distance = float(distance)
        price = 610710.0319872361 - 72635.89282856 * distance
        print("House price is >>> "+str(price))
        
# if __name__ == "__main__":
#     model_instance = HousePricePredictor()
#     model_instance.predict_price(6)