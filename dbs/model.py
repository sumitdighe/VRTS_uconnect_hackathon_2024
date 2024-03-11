from tensorflow.keras import layers
from tensorflow.keras import layers
from tensorflow import keras
def create_decoder(input_shape):
  decoder_input = layers.Input(shape=input_shape)
  num_features = input_shape[-1]
  x = layers.Dense(units=512, activation="relu")(decoder_input) 
  x = layers.Dense(units=256, activation="relu")(x)      
  x = layers.Dense(units=num_features, activation="sigmoid")(x)  
  decoder = keras.Model(inputs=decoder_input, outputs=x, name="decoder")
  return decoder
