import json

# override its default() method
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)
          
complex_json = json.dumps(2 + 5j, cls=ComplexEncoder)          
encoder = ComplexEncoder()
encoder.encode(3 + 6j)

json.loads(complex_json)

def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

with open("complex_data.json") as complex_data:
    data = complex_data.read()
    numbers = json.loads(data, object_hook=decode_complex)
