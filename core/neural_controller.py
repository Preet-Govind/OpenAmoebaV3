import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

class NeuralController:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = models.Sequential([
            layers.Input(shape=(100,)),  # Updated to match the new sensory input size
            layers.Dense(128, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(2, activation='tanh')  # Output: x and y movement direction
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def decide_movement(self, sensory_inputs):
        # Ensure the input is in the correct format (batch size, input shape)
        inputs = np.expand_dims(np.array(sensory_inputs, dtype=np.float32), axis=0)  # Add batch dimension
        movement = self.model.predict(inputs)[0]  # Get the first (and only) prediction
        return movement
