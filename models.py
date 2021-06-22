
def display_model_details(model):
    for layer_number, layer in enumerate(model):
        print(layer_number, layer.name, layer.trainable)
