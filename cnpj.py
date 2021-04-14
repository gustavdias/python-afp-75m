
import string
#make translator object
# translator=str.maketrans('','',string.punctuation)
# string_name=string_name.translate(translator)

# cleaned_data = data.translate(str.maketrans('','',string.punctuation+string.digits,))

cnpj = "00.000.000/0001-00"
clean_cnpj = cnpj.translate(str.maketrans('','',string.punctuation))

print(clean_cnpj)