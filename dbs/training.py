from tensorflow.keras.preprocessing.text import Tokenizer
import random
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import metrics
def create_decoder(input_shape):
  decoder_input = layers.Input(shape=input_shape)
  num_features = input_shape[-1]
  x = layers.Dense(units=512, activation="relu")(decoder_input) 
  x = layers.Dense(units=256, activation="relu")(x)      
  x = layers.Dense(units=num_features, activation="sigmoid")(x)  
  decoder = keras.Model(inputs=decoder_input, outputs=x, name="decoder")
  return decoder

def generate_random_sql(max_iterations=100):
  tables = ["users", "products", "orders", "items"]  
  columns = ["id", "name", "email", "price", "quantity"] 
  operators = ["=", "<", ">", "<=", ">=", "!=", "<>"]
  values = ["?", "%s"]  
  iterations = 0
  while iterations < max_iterations:
    query = ""
    statement = random.choice(["SELECT", "INSERT", "UPDATE"])
    query += statement + " "
    query += random.choice(tables) + " "
    if statement == "UPDATE":
      query += "SET "
      query += random.choice(columns) + " = " + random.choice(values) + " "
    if random.random() < 0.5:  
      query += "WHERE "
      query += random.choice(columns) + " " + random.choice(operators) + " " + random.choice(values)
    if random.random() < 0.3: 
      query += "LIMIT " + str(random.randint(10, 50))
    try:
      if not query.endswith(";"):
        query += ";"
      return query
    except Exception:
      pass 

  return None 

def generate_augmented_sql_queries(num_queries=100):
  queries = set()
  while len(queries) < num_queries:
    query = generate_random_sql()
    if query is not None:
      queries.add(query)

  return list(queries)
sql_queries = generate_augmented_sql_queries(num_queries=100)
tokenizer = Tokenizer()  
tokenizer.fit_on_texts(sql_queries)
sequences = tokenizer.texts_to_sequences(sql_queries)
padded_sequences = pad_sequences(sequences, maxlen=100, padding='post')
one_hot_encoded_queries = tf.one_hot(padded_sequences, 100)
X_train=one_hot_encoded_queries
print(X_train.shape[1:])
model=create_decoder(X_train.shape[1:])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=[metrics.Accuracy(), 'mse'])
model.fit(X_train, X_train, epochs=10)
model.save('model.h5')

