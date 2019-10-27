import Reader
import GramsHelper

# Step 1: Prepare data
data = Reader.get_data()

# Step 2: Feature definition
# Feature set 1: characters 4-grams
for item in data:
    item.append(GramsHelper.generate_char_k_gram(4, item[0]))
