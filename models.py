def display_model_details(_model, level=0):
    for layer_number, layer in enumerate(_model.layers):
        extra = ' ' * level * 2
        print(f"{extra} {layer_number} {layer.name.ljust(35)} \t{layer.trainable}")
        if hasattr(layer, 'layers'):
            more_layers = True
            if level < 10:
                display_model_details(layer, level + 1)
                print("\n")
        else:
            more_layers = False
