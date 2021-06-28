def display_model_details(_model, level=0):
    """
    Display information for model Layers.

  """
    for layer_number, layer in enumerate(_model.layers):
        extra = ' ' * level * 2
        print(f"{extra} {layer_number} {layer.name.ljust(35)} \t{layer.trainable}\t{layer.dtype}")
        if hasattr(layer, 'layers'):
            if level < 10:
                display_model_details(layer, level + 1)
                print("\n")
