import os

# cartoonGAN models data

cartoon_models_file = ["GM", "SB", "DR"]  # "SB", "DR"은 가짜로 만듦
cartoon_models_name = ["Ghost Messanger", "Sponge Bob", "Dr.Frost"]

model_path = "saved_model"

cartoon_models_dict = {
    name: os.path.join(model_path, filee)
    for name, filee in zip(cartoon_models_name, cartoon_models_file)
}

"""
{'Dr.Frost': 'saved_model/DR',
 'Ghost Messanger': 'saved_model/GM',
 'Sponge Bob': 'saved_model/SB'}

cartoon_model_path = cartoon_models_dict['Ghost Messanger']
saved_model/GM

"""
