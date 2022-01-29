### 1) ¿Puedes identificar el error en el siguiente código?
#> media = num_1 + num_2 + num_3 / 3

### Se pretende hacer una media muestral de 3 elementos pero no funciona correctamente

num_1 = 4
num_2 = 3
num_3 = 3

media = (num_1 + num_2 + num_3) / 3;
print('El promedio es ', media);

media_2 = num_1 + num_2 + num_3 / 3;
print('El promedio es ', media_2);