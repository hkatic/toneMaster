# Tone Master #

* Autores: Hrvoje Katić
* Descargar [versión estable][1]

¡Bieinvenido a Tone Master! He creado este pequeño complemento de NVDA sólo por diversión, pero también para que te diviertas tú mientras lo utilizas.

Siempre quise crear tonos musicales con NVDA, en lugar de escuchar sus pitidos de progreso y de error. Sin embargo, no es demasiado fácil de hacer, así que primero quise hacerlo más fácil. Es por ello que escribí Tone Master. Sólo imagina lo que sería para ti escuchar a NVDA reproduciendo canciones de Mozzart o de Beethoven, o de los grandes éxitos de los Rolling Stones. Aunque los resultados finales suenan como aquellos tonos de llamada de los teléfonos móviles viejos, todavía puede ser divertido.

Tone Master simplifica el proceso de tocar secuencias de tonos implementando ficheros de datos de tonos. Estos ficheros pueden editarse con tu editor de textos favorito y entonces guardarlos para reproducirlos con NVDA. ¡Lee para instrucciones!

## Ficheros de datos de melodías

Antes de que puedas reproducir tu primera melodía musical con Tone Master, tienes que crear y cargar tu fichero de datos de la melodía primero. Los ficheros de datos de melodía son simples ficheros de texto con la extensión .tdf. Tone Master utiliza estos ficheros para procesar y reproducir secuencias de tonos. Para crear ficheros de datos de melodías para que Tone Master pueda reproducirlos con éxito, tienes que seguir unas simples reglas descritas abajo.

1. Cada línea en el fichero .tdf *debe* contener  tres parámetros separados por dos puntos (:). El primer parámetro es el tono, el segundo parámetro es la duración, y el tercero es el tiempo del silencio entre cada tono. Es necesario especificar todos los parámetros , de otro modo Tone Master no podrá reproducir tus datos de melodía.
2. Los parámetros tono y duración  deben especificarse como enteros, y el silencio debe especificarse como un valor real de coma flotante .
3. Un signo de número (#) al comienzo de cualquier línea en el fichero .tdf se tratará como un comentario y se ignorará por Tone Master.

Ejemplo: reproduce una secuencia de 3 tonos

1500:100:0.5

1000:100:0.09

500:100:0.7

En este ejemplo, la primera nota en una secuencia tiene un tono de 1500, una duración de 100 y un silencio de 0.5. la nota del segundo tono es 1000, la duración es 100, y el silencio es 0.09. la última nota en una secuencia tiene tono 500, duración 100, y el silencio es 0.7.

Nota, es necesario especificar el parámetro silencio incluso si piensas que no lo es, porque si no se especifica, NVDA anulará la nota anterior con la siguiente, y obtendrás resultados inesperados. Es por eso que lo hice ser necesario.

Para llegar a estar más familiarizado con la sintaxis de los ficheros de datos de melodías, por favor revisa e intenta editar el fichero ejemplo incluido con este complemento. Se encuentra en la subcarpeta "tones" , donde también se deben colocar todos tus ficheros .tdf.

## Atajos de teclado

* Alt+NVDA+T: reproduce el fichero de melodías actualmente cargado si todo está bien.
* Alt+Shift+NVDA+T: detiene la reproducción para el fichero de datos de melodía actualmente cargado si cualquier melodía se está reproduciendo.
* Alt+NVDA+N: crea y abre un fichero de datos de melodía nuevo en el Bloc de Notas para editar.
* Alt+NVDA+L: abre un diálogo que te permite elegir uno de tus ficheros de datos de melodía disponibles para que se carguen para reproducirse.
* Alt+NVDA+E: abre el fichero de datos de melodía actualmente cargado en el Bloc de Notas para editar.
* Alt+NVDA+O: abre una carpeta con ficheros de datos de melodía donde también deberías guardarlos para ser localizados por Tone Master.

## Otras notas

También puedes crear, editar y cargar ficheros de datos de melodía, o abrir la carpeta de melodías donde se encuentran estos ficheros yendo al menú NVDA, submenú Herramientas, submenú Tone Master.

Cuando se muestre el diálogo para crear ficheros de datos de melodía nuevos, teclea el nombre sin la extensión .tdf. La extensión se añadirá automáticamente por Tone Master. Si no se especificó nombre alguno, Tone Master utilizará el nombre predeterminado "untitled.tdf". Tone Master creará automáticamente und nuevo fichero cargado para ti, y también se abrirá en el Bloc de Notas para editar. Pulsa Escape en el indicativo del nombre de fichero para cancelar la creación del fichero nuevo.

Nota: Tone Master utiliza Bloc de Notas para editar ficheros de datos de melodía, ya que viene con Windows por defecto y por lo tanto cualquier ordenador debería tenerlo disponible.

Cuando el diálogo para cargar fichero de datos de melodía esté abierto, utiliza las teclas de flecha para seleccionar un fichero para cargar y entonces pulsa Intro. Pulsa Escape para cancelar la carga.

Cuando abres una carpeta con ficheros .tdf, puedes entonces cargarlos en tu editor de texto para verlos o editarlos. No obstante, para escuchar tus resultados al vuelo, te recomiendo enfáticamente cargar el fichero en Tone Master primero si es posible. entonces puedes editar el fichero, guarda tu progreso, y después de cada guardado puedes utilizar la orden reproducir para escuchar tu último resultado.

## Cambios para 1.3

* Corregido: Solucionado el problema de compatibilidad con las nuevas versiones de NVDA.

## Cambios para 1.2

* Corregido: dirigido un problema mayor donde al seleccionar un fichero de datos de melodía vacío, luego al seleccionar otro e intentar reproducirlo ocurre que los datos de melodía no se reproducen.

## Cambios para 1.1

* Añadida: Una opción para crear un fichero nuevo de datos de melodía y para abrirlo en el Bloc de Notas para editar.
* Añadida: Una opción para editar el fichero de datos de melodía actualmente cargado en el Bloc de Notas.
* Mejorado: los mensajes de error ahora son más amigables para el usuario.
* Mejorado: ciertas características del complemento tales como la apertura de la carpeta de melodías o la edición de ficheros de datos de melodía en el Bloc de Notas ahora no se permiten en las pantallas seguras.
* Mejorado: se notificará al usuario por NVDA si la reproducción de datos de melodía se detiene.
* Corregido: no se permite la reproducción de datos de melodía mientras uno esté ya en reproducción.

## Cambios para 1.0

* Versión inicial.

[1]: https://github.com/nvdaaddons/toneMaster/releases/download/v1.2/toneMaster-1.2.nvda-addon
