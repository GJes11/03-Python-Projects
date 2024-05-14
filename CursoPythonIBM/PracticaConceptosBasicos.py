#Minimo entre 2 numeros
a = -1; b= -4
def minimum(a, b):
    if a <= b:
        return a
    else: 
        return b
print(minimum(a, b))

#Invertir palabras de una cadena dada
#entrada 
str = 'Codigo de practica de prueba de geeks'
#salida 
str = 'geeks de prueba de practica de codigo'

def rev_sentence(sentence):
    words = sentence.split(' ')

    reverse_sentence = ' '.join(reversed(words))

    return reverse_sentence

if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(rev_sentence(input))