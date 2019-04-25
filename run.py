from criptografador import *

#Frase a ser criptografada - Pode ser trocada para qualquer outra fase
b = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in diam vel tellus ultrices aliquet. Sed tellus eros, molestie eu mattis scelerisque, dictum vel lectus. Proin dapibus tellus metus, nec fringilla urna volutpat id. Pellentesque dictum interdum mi eu maximus. Pellentesque ac luctus nibh. Maecenas a fringilla mauris. Aliquam ut condimentum neque. Donec vitae erat justo. Maecenas accumsan commodo ante. Vivamus eu nibh non diam semper rhoncus ut et metus. Quisque ac lorem quis ex dignissim semper vel eget mauris. Quisque leo enim, posuere quis tincidunt malesuada, rutrum ultrices risus"
a = Blocos("acaba o semestre") #Frase utilizada como bloco - Qualquer quantidade de caracteres acima de 16 será ignorada nessa frase e se a quantidade for menor que 16 caracteres e maior que 1 caracter será preenchido com espaço
chave,aux = a.nextBloco()
c = Criptografador(chave)
print("Frase original: ")
print(b)
fraseCrip = c.cifra(b)
print("Frase criptografada: ")
print(fraseCrip)
print("Frase descriptografada: ")
fraseDecrip = c.decifra(fraseCrip)
print(fraseDecrip)