import pandas as pd

with open('./Speciesnames.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

species_list = []
common_name_list = []

for line in lines:
    line = line.strip() 
    if line:
        parts = line.split('(')
        if len(parts) > 1:
            species_name = parts[0].strip()
            common_names = parts[1].replace(')', '').strip()
            common_names = common_names.split(',')
            for common_name in common_names:
                species_list.append(species_name)
                common_name_list.append(common_name.strip())

data = pd.DataFrame({'Species Name': species_list, 'Common Name': common_name_list})

data.to_csv('cleaned_plant_data.csv', index=False)

print("Data cleaned and saved to 'cleaned_plant_data.csv'")
