# Punto de Control 6 Checkpoint 3 

¡Buenas! Dejo aquí la respuesta de las preguntas teoricas respectivas al **Punto de Control 6 del Modulo 3.**

## 1-¿Para qué usamos Clases en Python?
 Lo que nos permiten hacer **las clases en Python es crear modelos de objetos que representan entidades en nuestro código**. Puedes definir **atributos (variables) y métodos (funciones)** que <u>describen las características y comportamientos de una entidad</u>. 
 Al crear instancias de una clase, **puedes tener objetos que representan diferentes instancias de esa entidad**. 

 Además lo que nos permiten las clases en Python es una forma de estructurar y organizar el código.

 Cuando definimos una clase podemos crear una serie de instancias de esa clase que contienen **datos y comportamientos relacionados**.

 **Definición de una clase:** Una clase en Python se define utilizando la palabra clave class, seguida del nombre de la clase. Dentro de la clase, se pueden definir atributos (propiedades) y métodos (funciones asociadas a un objeto).

 class MiClase:
    atributo = "valor"

    def metodo(self):
        # Cuerpo del método
        pass


En este ejemplo, se define una clase llamada MiClase con un atributo llamado atributo y un método llamado metodo. El atributo se define directamente dentro de la clase, mientras que el método se define dentro de la clase y recibe un argumento especial llamado self, que se refiere al objeto actual.

**Creación de objetos:** Para crear objetos a partir de una clase, se utiliza la sintaxis nombre_de_la_clase(argumentos), donde nombre_de_la_clase es el nombre de la clase y argumentos son los valores de inicialización opcionales.

objeto = MiClase()

En este ejemplo, se crea un objeto llamado objeto a partir de la clase MiClase.

**Acceso a atributos y métodos:** Una vez que se ha creado un objeto, se pueden acceder a sus atributos y métodos utilizando la notación de punto.

 Las clases **nos permiten reutilizar código escribiendo funciones y métodos que se aplican a todas las instancias de una clase**.

 Esto nos ahorra tiempo y nos permite **escribir código más conciso y legible**. 

 Además, las clases <u>**nos brindan una forma estructurada de organizar y mantener el código**</u>.

    ###Así sería la sintaxis básica para definir una clase en Python es la siguiente:
            class NombreDeLaClase:
                # Atributos (variables de la clase)
                atributo1 = valor1
                atributo2 = valor2

                # Métodos (funciones asociadas a la clase)
                def metodo1(self, argumentos):
                    # Cuerpo del método

                def metodo2(self, argumentos):
                    # Cuerpo del método
![image](https://github.com/ivandobarriocordon/PC6M3/assets/146997085/160a0d3a-68ef-4436-9524-c97e2238a27e)




## 2-¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
 El metodo al que se refiere la pregunta **es el método "Constructor" o "Método de inicialización"**, este **se ejecuta automáticamente cuando se crea una instancia de una clase**. Una explicacion sencilla de como funciona este método es que **se utiliza para inicializar los atributos de una instancia de una clase**. <u>Al crear una instancia de una clase, el constructor se ejecuta automáticamente y te permite establecer valores iniciales para los atributos de la instancia</u>. 

![image](https://github.com/ivandobarriocordon/PC6M3/assets/146997085/fe04fd8f-db28-4258-9725-8298df0a3792)

 
 **El constructor también puede realizar otras tareas de configuración y preparación inicial.**
   
   En Python, hay un método especial llamado __init__ que se ejecuta automáticamente cuando se crea una instancia de una clase. El método __init__ se utiliza para inicializar los atributos de la instancia.

   Definición del método init El método __init__ se define dentro de la clase y recibe como primer argumento el objeto actual (self), seguido de cualquier otro argumento que se desee utilizar para inicializar los atributos de la instancia.


   class MiClase:
    def __init__(self, atributo):
        self.atributo = atributo

    En este ejemplo, se define el método __init__ en la clase MiClase. El método recibe un argumento llamado atributo, que se utiliza para inicializar el atributo atributo de la instancia.

    Creación de instancias y ejecución de init Cuando se crea una instancia de una clase, se llama automáticamente al método __init__ para inicializar los atributos de la instancia.

    objeto = MiClase("valor")

    En este ejemplo, se crea una instancia de la clase MiClase llamada objeto y se pasa el valor "valor" como argumento para inicializar el atributo atributo de la instancia. El método __init__ se ejecuta automáticamente y se asigna el valor "valor" al atributo        
    atributo del objeto.

    Es importante tener en cuenta que el método __init__ es especial y se llama automáticamente cuando se crea una instancia de una clase.

    Estos son algunos metodos en Python:

    __init__(): Se ejecuta automáticamente cuando se crea una instancia de una clase y se utiliza para inicializar los atributos de la instancia.
    __new__(): Se ejecuta antes de la creación de una instancia de una clase y se utiliza para crear la instancia.
    __del__(): Se ejecuta automáticamente cuando se elimina una instancia de una clase. Se utiliza para realizar acciones antes de eliminar la instancia.
    __str__(): Define la representación en forma de cadena de la instancia. Se llama automáticamente cuando se utiliza la función str() en una instancia.
    __repr__(): Define una representación en forma de cadena que permite reconstruir una instancia. Se llama automáticamente cuando se utiliza la función repr() en una instancia.
    __len__(): Define la longitud de una instancia. Se llama automáticamente cuando se utiliza la función len() en una instancia.
    __getitem__(): Define el comportamiento de los índices en una instancia. Se llama automáticamente cuando se accede a un elemento de una instancia utilizando la sintaxis de índice.
    __setitem__(): Define el comportamiento de asignación de un elemento en una instancia. Se llama automáticamente cuando se asigna un valor a un elemento de una instancia utilizando la sintaxis de índice.
    __delitem__(): Define el comportamiento de eliminación de un elemento en una instancia. Se llama automáticamente cuando se elimina un elemento de una instancia utilizando la sintaxis de índice.
    __call__(): Define el comportamiento de llamar a una instancia como si fuera una función. Se llama automáticamente cuando se invoca una instancia utilizando la sintaxis de llamada.
    __iter__(): Define el comportamiento de iterar sobre una instancia. Se llama automáticamente cuando se utiliza un bucle for en una instancia.
    __next__(): Define el comportamiento de obtener el siguiente elemento en una iteración. Se llama automáticamente cuando se utiliza la función next() en una instancia.
    __contains__(): Define el comportamiento de verificar si un elemento está presente en una instancia. Se llama automáticamente cuando se utiliza la sintaxis in en una instancia.
    __eq__(): Define el comportamiento de comparación de igualdad entre instancias. Se llama automáticamente cuando se utiliza el operador == en dos instancias.
    __ne__(): Define el comportamiento de comparación de desigualdad entre instancias. Se llama automáticamente cuando se utiliza el operador != en dos instancias.
    __lt__(): Define el comportamiento de comparación de menor que entre instancias. Se llama automáticamente cuando se utiliza el operador < en dos instancias.
    __le__(): Define el comportamiento de comparación de menor o igual que entre instancias. Se llama automáticamente cuando se utiliza el operador <= en dos instancias.
    __gt__(): Define el comportamiento de comparación de mayor que entre instancias. Se llama automáticamente cuando se utiliza el operador > en dos instancias.
    __ge__(): Define el comportamiento de comparación de mayor o igual que entre instancias. Se llama automáticamente cuando se utiliza el operador >= en dos instancias.
    __getattr__(): Define el comportamiento de obtener un atributo que no está definido en una instancia. Se llama automáticamente cuando se accede a un atributo que no existe en una instancia.
    __setattr__(): Define el comportamiento de asignar un atributo en una instancia. Se llama automáticamente cuando se asigna un valor a un atributo de una instancia.

 
 ###Así sería la sintaxis básica para definir un constructor en Python es la siguiente:
     class NombreDeLaClase:
          def __init__(self, argumentos):
          # Cuerpo del constructor

          -def __init__(self, argumentos): es el método especial llamado __init__. Este método se utiliza como constructor y se ejecuta automáticamente cuando se crea una instancia de la clase.
          -self es un parámetro especial que se utiliza para referirse a la instancia de la clase.
          -argumentos son los parámetros que se pueden pasar al constructor para inicializar los atributos de la instancia.
  
###Ejemplo de uso del constructor
   class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

      Crear una instancia de la clase Persona
     persona1 = Persona("Juan", 25)
     
      Acceder a los atributos de la instancia
     print(persona1.nombre)  # Output: Juan
     print(persona1.edad)    # Output: 25

     En este ejemplo, la clase Persona tiene un constructor que toma dos argumentos: nombre y edad. Al crear una instancia de la clase Persona con los valores "Juan" y 25, el constructor se ejecuta automáticamente y establece los valores iniciales de los atributos nombre y edad de la instancia. Luego, podemos acceder a estos atributos a través de la instancia.

## 3-¿Cuáles son los tres verbos de API?
   A lo que se refiere la pregunta, **se refiere a los tres verbos comunes utilizados en las APIs** (Que es la Interfaz de Programación de Apliaciones): **GET POST y PUT**. 
   
   A continuación dejaré una expliacion sencilla y con ejemplos **de cómo se utilizan estos verbos en las APIs:**
![image](https://github.com/ivandobarriocordon/PC6M3/assets/146997085/09bc2ce1-2a5c-4525-a13b-1c3999ba2efc)


GET:
-Verbo HTTP utilizado **para recuperar datos de un recurso específico.**
-**No modifica el estado del recurso en el servidor.**
-Se utiliza **para obtener información o recursos.**

Ejemplo: **GET /api/users para obtener la lista de usuarios.**

POST

-Verbo HTTP utilizado **para enviar datos al servidor para crear un nuevo recurso.**
-**Modifica el estado del recurso en el servidor.**
-**Se utiliza para enviar datos al servidor para crear un nuevo recurso.**

Ejemplo: **POST /api/users para crear un nuevo usuario.**

PUT

-Verbo HTTP utilizado **para enviar datos al servidor para actualizar un recurso existente.**
-**Modifica el estado del recurso en el servidor.**
-**Se utiliza para enviar datos al servidor para actualizar un recurso existente.**

Ejemplo: **PUT /api/users/1 para actualizar el usuario con ID 1.**

Estos verbos HTTP **son utilizados en las APIs para realizar diferentes operaciones CRUD (Create, Read, Update, Delete) en los recursos.** **Cada verbo tiene su propósito y comportamiento específico, y se utilizan según las necesidades de la aplicación.**

GET: Se utiliza para obtener información de un recurso. Es el más común y se utiliza para consultar datos.
POST: Se utiliza para enviar datos al servidor para crear un nuevo recurso. Se utiliza para enviar formularios y enviar datos al servidor.
PUT: Se utiliza para enviar datos al servidor para actualizar un recurso existente. Se utiliza para enviar datos al servidor y actualizar un recurso.

Además de estos tres verbos, existen otros dos:

DELETE: Se utiliza para eliminar un recurso del servidor. Se utiliza para eliminar datos del servidor.
PATCH: Se utiliza para enviar datos al servidor para actualizar parcialmente un recurso existente. Se utiliza para enviar datos al servidor y actualizar parcialmente un recurso.
Estos verbos de API son fundamentales para la comunicación entre clientes y servidores en una API. Cada verbo tiene una funcionalidad específica y se utiliza en combinación con las rutas de la API para realizar diferentes operaciones en los recursos.

Las distintas operaciones que pueden hacer estos verbos en una API son las siguientes:

**GET:**
Obtener información de un recurso: El verbo GET se utiliza para recuperar información de un recurso específico en la API. Por ejemplo, si tienes una API de productos, puedes usar GET para obtener información sobre un producto en particular.
Listar recursos: GET también se puede utilizar para obtener una lista de recursos en la API. Por ejemplo, si tienes una API de usuarios, puedes usar GET para obtener una lista de todos los usuarios registrados.
Filtrar recursos: GET también se puede utilizar para filtrar y obtener una lista de recursos en función de ciertos criterios. Por ejemplo, si tienes una API de productos, puedes usar GET con parámetros de consulta para obtener una lista de productos que cumplan con ciertos criterios de búsqueda.

**POST:**
Crear un nuevo recurso: El verbo POST se utiliza para enviar datos al servidor y crear un nuevo recurso en la API. Por ejemplo, si tienes una API de productos, puedes usar POST para enviar datos de un nuevo producto y crearlo en la base de datos.
Enviar formularios: POST también se puede utilizar para enviar datos de un formulario al servidor. Por ejemplo, si tienes una API de registro de usuarios, puedes usar POST para enviar datos de un formulario de registro y crear un nuevo usuario en la base de datos.

**PUT:**
Actualizar un recurso existente: El verbo PUT se utiliza para enviar datos al servidor y actualizar un recurso existente en la API. Por ejemplo, si tienes una API de productos, puedes usar PUT para enviar datos de un producto existente y actualizarlo en la base de datos.
Reemplazar un recurso: PUT también se puede utilizar para reemplazar completamente un recurso existente con nuevos datos. Por ejemplo, si tienes una API de productos, puedes usar PUT para enviar datos completamente nuevos para reemplazar un producto existente en la base de datos.

**DELETE:**
Eliminar un recurso: El verbo DELETE se utiliza para eliminar un recurso específico en la API. Por ejemplo, si tienes una API de productos, puedes usar DELETE para eliminar un producto en particular de la base de datos.
Eliminar recursos en masa: DELETE también se puede utilizar para eliminar múltiples recursos en la API. Por ejemplo, si tienes una API de usuarios, puedes usar DELETE para eliminar múltiples usuarios seleccionados de la base de datos.

**PATCH:**
Actualizar parcialmente un recurso existente: El verbo PATCH se utiliza para enviar datos al servidor y actualizar parcialmente un recurso existente en la API. Por ejemplo, si tienes una API de productos, puedes usar PATCH para enviar datos parciales de un producto existente y actualizar solo esos campos en la base de datos.
Reemplazar campos específicos de un recurso: PATCH también se puede utilizar para reemplazar solo ciertos campos de un recurso existente con nuevos datos. Por ejemplo, si tienes una API de usuarios, puedes usar PATCH para actualizar solo el nombre y la dirección de correo electrónico de un usuario existente en la base de datos.

## 4-¿Es MongoDB una base de datos SQL o NoSQL?
MongoDB **es una base de datos NoSQL porque no sigue el modelo relacional tradicional de bases de datos SQL**. En lugar de utilizar tablas con esquemas fijos y relaciones entre ellas, **MongoDB utiliza documentos JSON-like para almacenar datos**. **Cada documento puede tener una estructura diferente y puede contener campos y valores arbitrarios.**

Esto permite una flexibilidad y escalabilidad adicional en la estructura y el modelo de datos.

Una explicacion más detallada de las diferencias entre bases de datos SQL y NoSQL, y cómo se relaciona MongoDB con este enfoque:

**Estructura de datos:**
Bases de datos SQL: Utilizan tablas y relaciones para almacenar datos. Cada fila representa un registro y las columnas definen los campos de datos. Se requiere un esquema predefinido para almacenar y recuperar datos.
Bases de datos NoSQL: No utilizan tablas y relaciones tradicionales. En lugar de eso, utilizan documentos JSON para almacenar datos. Cada documento puede tener una estructura diferente y no requiere un esquema predefinido.

**Consultas:**
Bases de datos SQL: Son estructuradas y se adaptan mejor a las consultas estructuradas. Permiten realizar consultas complejas utilizando lenguajes de consulta SQL.
Bases de datos NoSQL: Son escalables y se adaptan mejor a los datos dinámicos y complejos. Permiten realizar consultas más flexibles y eficientes utilizando lenguajes de consulta específicos como MongoDB Query Language (MQL).

**Escalabilidad:**
Bases de datos SQL: Pueden tener limitaciones en términos de escalabilidad cuando se trata de almacenar y recuperar grandes cantidades de datos. Requieren una infraestructura de alto rendimiento y pueden ser más costosas en términos de recursos.
Bases de datos NoSQL: Son escalables y se adaptan mejor a los datos dinámicos y complejos. Permiten almacenar y recuperar grandes cantidades de datos de manera eficiente. Pueden escalarse horizontalmente agregando más nodos o particiones 



**MongoDB es ampliamente utilizado en aplicaciones que requieren una alta flexibilidad en la estructura de los datos, como aplicaciones web, aplicaciones de IoT, análisis de datos, etc.** Algunos casos de uso comunes incluyen:

-Aplicaciones web y móviles que requieren almacenar y acceder a datos estructurados y no estructurados.
-Almacenamiento de datos semi-estructurados, como datos de usuarios, registros de eventos, etc.
-Análisis y procesamiento de datos en tiempo real.
-Almacenamiento de grandes volúmenes de datos no estructurados, como imágenes, archivos, etc.
-Sintaxis básica de MongoDB La sintaxis básica para interactuar con MongoDB utiliza el lenguaje de consultas JavaScript.

**Aquí tienes algunos ejemplos básicos de cómo se utiliza MongoDB:**

**Conectarse a una base de datos:**
const MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017', (err, client) => {
  if (err) {
    console.error('Error al conectar a la base de datos:', err);
    return;
  }

  console.log('Conexión exitosa a la base de datos');
  // Resto del código...

  client.close();
});

**Crear una colección:**

const db = client.db('nombre_de_la_base_de_datos');
const coleccion = db.collection('nombre_de_la_coleccion');

**Insertar una colección**:

const documento = { nombre: 'Juan', edad: 25 };
coleccion.insertOne(documento, (err, result) => {
  if (err) {
    console.error('Error al insertar documento:', err);
    return;
  }

  console.log('Documento insertado con éxito');
  // Resto del código...
});

**Consultar documentos:**

coleccion.find({}).toArray((err, documentos) => {
  if (err) {
    console.error('Error al consultar documentos:', err);
    return;
  }

  console.log('Documentos encontrados:', documentos);
  // Resto del código...
});

**MongoDB ofrece una amplia gama de características y operaciones avanzadas para trabajar con datos no estructurados y flexibles.**

**Documentos JSON:** MongoDB utiliza documentos JSON para almacenar datos. Los documentos pueden tener una estructura diferente en cada caso y no requieren un esquema predefinido. Esto permite una flexibilidad en la estructura de los datos.

**Escalabilidad horizontal:** MongoDB es escalable horizontalmente, lo que significa que se pueden agregar más nodos al clúster para manejar una carga más alta. Esto permite que MongoDB maneje grandes volúmenes de datos y se adapte a las necesidades de escalabilidad.

**Consultas avanzadas:** MongoDB ofrece una sintaxis de consulta poderosa que permite realizar consultas complejas y avanzadas en los datos no estructurados. Puedes realizar consultas por diferentes campos, combinar condiciones, realizar agregaciones y mucho más.

![image](https://github.com/ivandobarriocordon/PC6M3/assets/146997085/a3b499f6-de47-44ce-ab93-3bb631d05278)


## 5-¿Qué es una API?
    Una API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y protocolos que permiten a las aplicaciones comunicarse entre sí. Proporciona una forma estructurada de acceder a funcionalidades y recursos de un sistema o servicio. Las APIs permiten que     diferentes aplicaciones se comuniquen, intercambien datos y realizen acciones conjuntas.

    Una API es utilizada para facilitar la comunicación y la integración entre diferentes sistemas y aplicaciones. Aquí hay algunos casos de uso comunes de las APIs:

    Acceder a datos y servicios de un servidor remoto.
    Utilizar servicios web para obtener información o realizar acciones en línea.
    Desarrollar aplicaciones móviles que se conectan a servicios en línea.
    Integración de sistemas y aplicaciones, como en una arquitectura de microservicios.

Un ejemplo de como se puede realizar una solicitud a una API utilizando la biblioteca requests en Python:

**import requests**

url = 'https://api.example.com/endpoint'
data = {
    'parametro1': 'valor1',
    'parametro2': 'valor2'
}

response = requests.post(url, data=data)

 Procesar la respuesta de la API
response_data = response.json()

 **Acceder a los datos de la respuesta**
estado = response_data['estado']
mensaje = response_data['mensaje']

 **Imprimir los datos de la respuesta**
print("Estado:", estado)
print("Mensaje:", mensaje

Una explicación detallada de qué es una API (Application Programming Interface) y cómo funciona:

**Definición:** Una API es un conjunto de reglas y protocolos que permite a las aplicaciones comunicarse entre sí. En otras palabras, una API define cómo diferentes aplicaciones pueden interactuar y compartir datos.

**Funcionamiento:** Una API consta de dos partes principales: el servidor y el cliente. El servidor proporciona los recursos y las operaciones que pueden ser utilizadas por el cliente. El cliente es la aplicación que utiliza la API para acceder a esos recursos y realizar operaciones en ellos.

**Endpoints:** Los endpoints son los puntos de acceso a través de los cuales las aplicaciones pueden interactuar con la API. Son direcciones URL específicas que definen la ruta y el método HTTP (como GET, POST, PUT, DELETE) para acceder a los recursos y realizar operaciones en la API.

**Verbos HTTP:** Los verbos HTTP son métodos HTTP que se utilizan para realizar operaciones en recursos en una API. Los verbos más comunes son GET, POST, PUT y DELETE, que se utilizan para obtener, crear, actualizar y eliminar recursos, respectivamente.

**Formato de datos:** Las APIs pueden utilizar diferentes formatos de datos para transmitir información entre el servidor y el cliente. Algunos formatos comunes son JSON, XML y CSV.

**Autenticación y autorización:** Las APIs a menudo requieren autenticación y autorización para asegurar que solo las aplicaciones autorizadas puedan acceder a los recursos. Esto se logra mediante el uso de tokens de acceso, claves de API y otras formas de autenticación.

![image](https://github.com/ivandobarriocordon/PC6M3/assets/146997085/8837ff59-13cc-42a3-86ea-093555433f14)


    
## 6-¿Qué es Postman?
Postman **es una herramienta de desarrollo de API muy popular utilizada por desarrolladores, diseñadores y pruebas de API**. 

**Proporciona una interfaz gráfica fácil de usar para enviar solicitudes HTTP a una API y recibir y analizar las respuestas.** 

**Postman permite probar y depurar APIs, generar documentación de API, simular escenarios de prueba y mucho más.**

**Postman se utiliza para desarrollar y probar APIs.** 

Aquí hay algunos casos de uso comunes:

-Enviar solicitudes HTTP a una API y recibir y analizar las respuestas.
-Probar diferentes endpoints, parámetros, encabezados y cuerpos de solicitud de una API.
-Simular escenarios de prueba, como autenticación, carga de datos de prueba y más.
-Generar documentación de API automática a partir de las solicitudes y respuestas enviadas en Postman.
R-ealizar pruebas de rendimiento y carga de APIs.

La sintaxis de Postman se utiliza para enviar solicitudes HTTP a una API y recibir y analizar las respuestas. 

**Aquí hay un ejemplo básico de cómo se utiliza Postman:**

1-Abre Postman y crea una nueva solicitud.
2-Selecciona el método HTTP (GET, POST, PUT, DELETE, etc.) y la URL de la API a la que deseas enviar la solicitud.
3-Agrega los encabezados de solicitud, como el tipo de contenido y los tokens de autenticación, si es necesario.
4-Define el cuerpo de la solicitud, si es necesario, para métodos como POST y PUT.
5-Haz clic en "Enviar" para enviar la solicitud a la API.
6-Postman mostrará la respuesta de la API, incluyendo el código de estado, los encabezados y el cuerpo de la respuesta.
7-Analiza los datos de respuesta y realiza cualquier prueba adicional necesaria.

**Postman ofrece muchas más características y funcionalidades, como la posibilidad de guardar solicitudes y respuestas para futuras referencias, la posibilidad de crear colecciones de solicitudes y pruebas automatizadas, y la posibilidad de integrar Postman con otras herramientas de desarrollo.**

Una explicación más detallada de qué es Postman y cómo se utiliza:

**Definición:** Postman es una herramienta de desarrollo de API que permite a los desarrolladores probar, desarrollar y documentar sus APIs de manera eficiente. Ofrece una interfaz intuitiva y fácil de usar que les permite enviar solicitudes HTTP, probar rutas de API, ver respuestas y realizar pruebas automatizadas.

**Funcionamiento:** Postman se utiliza principalmente en dos áreas principales: la prueba de APIs y la documentación de APIs.

**Prueba de APIs:** Con Postman, los desarrolladores pueden enviar solicitudes HTTP a sus APIs y ver las respuestas en tiempo real. Esto les permite probar diferentes rutas de API, enviar datos de ejemplo y verificar si las respuestas son las esperadas. Postman también ofrece características avanzadas como la capacidad de realizar pruebas automatizadas, almacenar solicitudes y respuestas para futuras referencias y generar documentación de la API.

**Documentación de APIs:** Postman también se utiliza para documentar sus APIs. Los desarrolladores pueden exportar sus pruebas de API a un formato de documentación, como Markdown o HTML, lo que facilita la generación de documentación clara y concisa sobre sus APIs. Esta documentación puede ser útil para otros desarrolladores que estén trabajando en el proyecto o para los clientes que estén utilizando la API.

**Características clave:** Algunas de las características clave de Postman son:

**Envío de solicitudes HTTP:** Postman permite a los desarrolladores enviar solicitudes HTTP a sus APIs de manera sencilla y fácil de usar. Los desarrolladores pueden especificar el método HTTP, la ruta de la API, los encabezados, los parámetros y los datos de la solicitud.

**Verificación de respuestas:** Postman muestra las respuestas HTTP recibidas de las solicitudes enviadas. Los desarrolladores pueden verificar el código de estado de la respuesta, los encabezados, los datos de la respuesta y cualquier otro detalle relevante.

**Pruebas automatizadas:** Postman permite a los desarrolladores escribir pruebas automatizadas para sus APIs. Estas pruebas pueden ser ejecutadas de manera automatizada y proporcionan una forma confiable de verificar si las APIs están funcionando correctamente.

![image](https://github.com/ivandobarriocordon/PC6M3/assets/146997085/b2cfde4e-031c-4c74-99ce-c3a0e5fcbe16)



## 7-¿Qué es el polimorfismo?
   El polimorfismo **es una característica de la programación orientada a objetos que permite que un objeto de un tipo de datos sea tratado como si fuera un objeto de otro tipo de datos.** **Esto se logra a través de la sobrecarga de métodos y la herencia.**
    El polimorfismo **es útil porque permite escribir código más flexible y modular.** **Al utilizar el polimorfismo, puedes escribir código que funcione con objetos de diferentes tipos sin tener que realizar verificaciones de tipo explícitas.** **Esto facilita la extensibilidad y la reutilización del código.**
    
**En la mayoría de los lenguajes de programación orientados a objetos, el polimorfismo se logra a través de la sobrecarga de métodos y la herencia.** 

Aquí hay un ejemplo básico de cómo se utiliza el polimorfismo en Java:
    
    class Animal {
    public void hacerSonido() {
        System.out.println("El animal hace un sonido");
    }
}

class Perro extends Animal {
    @Override
    public void hacerSonido() {
        System.out.println("El perro ladra");
    }
}

class Gato extends Animal {
    @Override
    public void hacerSonido() {
        System.out.println("El gato maulla");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal1 = new Perro();
        Animal animal2 = new Gato();

        animal1.hacerSonido(); // Imprime "El perro ladra"
        animal2.hacerSonido(); // Imprime "El gato maulla"
    }
}

En este ejemplo, se define una clase base Animal con un método hacerSonido(). Luego, se definen dos clases derivadas Perro y Gato que heredan de Animal y sobrescriben el método hacerSonido() para proporcionar un comportamiento específico para cada tipo de animal. En el método main(), se crean objetos de tipo Animal que se inicializan con instancias de Perro y Gato. Al llamar al método hacerSonido() en estos objetos, se ejecuta el comportamiento específico de cada tipo de animal.

Una explicación detallada del polimorfismo en programación orientada a objetos:

**Definición:** El polimorfismo es un concepto que permite a los objetos tener múltiples formas o comportamientos en función de su tipo. En otras palabras, el polimorfismo permite que los objetos se comporten de diferentes maneras en función de su clase.

**Tipos de polimorfismo:** Hay dos tipos principales de polimorfismo: el polimorfismo de subtipos y el polimorfismo de mensajes.

**Polimorfismo de subtipos:** El polimorfismo de subtipos se refiere a la capacidad de un objeto de una clase derivada para ser tratado como un objeto de su clase base. Esto permite que los objetos de diferentes clases se comporten de manera similar en función de su clase base.

**Polimorfismo de mensajes:** El polimorfismo de mensajes se basa en el principio de que un objeto debería poder responder a un mensaje sin importar su tipo real. Esto se logra mediante la sobrecarga de métodos o la implementación de interfaces.

**Ventajas del polimorfismo:** El polimorfismo tiene varias ventajas, como:

**Reutilización de código:** El polimorfismo permite reutilizar código común en clases relacionadas, lo que reduce la duplicación de código y facilita la mantenibilidad del sistema.

**Modularidad:** El polimorfismo facilita la modularidad del sistema, ya que permite que diferentes partes del sistema se comuniquen y se comuniquen utilizando interfaces comunes.

**Flexibilidad:** El polimorfismo permite una mayor flexibilidad en el sistema, ya que permite que los objetos se comporten de diferentes maneras en función de su tipo.

![image](https://github.com/ivandobarriocordon/PC6M3/assets/146997085/4ae342a2-b6df-4e07-9fc1-ca561b6af2c0)



## 8-¿Qué es un método dunder?
   Un método dunder (o "dunder" por sus siglas en inglés) **es un método especial en Python que está precedido por doble guion bajo (__) y que tiene una funcionalidad especial en las clases.** **Los métodos dunder se utilizan para sobrecargar operaciones y proporcionar funcionalidades especiales en Python.**
Los métodos dunder **se utilizan para personalizar el comportamiento de las clases en Python.** **Proporcionan una forma de definir cómo se comportan las clases cuando se utilizan operaciones o métodos específicos.** 

**Por ejemplo, los métodos dunder se utilizan para sobrecargar operaciones como la suma (+), la multiplicación (*), el acceso a atributos (.), entre otros.**

una explicación más detallada de algunos de los métodos dunder más comunes en Python:

**Método __init__: Este método se utiliza para inicializar un objeto y se llama automáticamente cuando se crea una instancia de una clase. Se utiliza para establecer los valores iniciales de las variables de instancia. Por ejemplo:**

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
**Método __str__: Este método se utiliza para definir cómo se muestra un objeto cuando se convierte en una cadena de texto. Se utiliza para representar el objeto en una forma legible. Por ejemplo:**

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
**Método __repr__: Este método se utiliza para definir cómo se muestra un objeto cuando se utiliza la función repr(). Se utiliza para representar el objeto de manera más detallada, normalmente incluyendo información adicional. Por ejemplo:**

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"
**Método __len__: Este método se utiliza para definir cómo se determina la longitud de un objeto. Se utiliza para devolver la cantidad de elementos en el objeto. Por ejemplo:**

class Lista:
    def __init__(self, elementos):
        self.elementos = elementos
    
    def __len__(self):
        return len(self.elementos)
**Método __add__: Este método se utiliza para definir cómo se realiza la operación de suma entre dos objetos. Se utiliza para definir cómo se combinan dos objetos. Por ejemplo:**

class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def __add__(self, otro_numero):
        return Numero(self.valor + otro_numero.valor)

**Estos son solo algunos ejemplos de métodos dunder comunes en Python. Hay muchos más métodos dunder disponibles, cada uno con un propósito específico. Recuerda que estos métodos se utilizan para personalizar el comportamiento de los objetos en diferentes situaciones.**

## 8-¿Qué es un decorador de python?
   Un decorador en Python **es una función que se utiliza para modificar el comportamiento de otra función o clase. Los decoradores se aplican utilizando la sintaxis de @ antes de una función o clase. Un decorador puede agregar funcionalidades adicionales, como la caché, la validación de argumentos, la medición del tiempo de ejecución, entre otros.**

 Los decoradores **son útiles porque permiten escribir código más modular y reutilizable.** En lugar de tener que modificar directamente la función o clase original, **se pueden aplicar decoradores para agregar comportamiento adicional. Esto facilita la extensibilidad y la mantenibilidad del código.**

La sintaxis de un decorador en Python es la siguiente:

def decorador(funcion_original):
    def funcion_decorada(*args, **kwargs):
        # Lógica adicional antes de llamar a la función original
        resultado = funcion_original(*args, **kwargs)
        # Lógica adicional después de llamar a la función original
        return resultado
    return funcion_decorada

@decorador
def funcion_a_decorar():
    # Cuerpo de la función

funcion_a_decorar()  # Llamada a la función decorada

Unos ejemplos del método decorador en Python:
Ejemplo 1: Decorador para la caché
from functools import wraps

def cache(func):
    cache_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache_data:
            cache_data[key] = func(*args, **kwargs)
        return cache_data[key]

    return wrapper

@cache
def expensive_function(x, y):
    print("Calculando...")
    return x ** y

print(expensive_function(2, 3))  # Calculando... 8
print(expensive_function(2, 3))  # No se realiza el cálculo, se utiliza el valor de la caché

En este ejemplo, el decorador cache se utiliza para agregar una funcionalidad de caché a la función expensive_function. La primera vez que se llama a expensive_function, se realiza el cálculo y se almacena el resultado en la caché. Las siguientes veces que se llama a la función con los mismos argumentos, se utiliza el valor de la caché en lugar de volver a calcularlo.

Ejemplo 2: Decorador para la validación de argumentos
def validate_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, int) for arg in args):
            raise ValueError("Todos los argumentos deben ser enteros")
        return func(*args, **kwargs)

    return wrapper

@validate_arguments
def sum(a, b):
    return a + b

print(sum(1, 2))  # 3
print(sum("1", 2))  # ValueError: Todos los argumentos deben ser enteros

En este ejemplo, el decorador validate_arguments se utiliza para validar que todos los argumentos de la función sum sean enteros. Si alguno de los argumentos no es un entero, se lanza una excepción ValueError.

Ejemplo 3: Decorador para la medición del tiempo de ejecución
import time

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución: {end_time - start_time} segundos")
        return result

    return wrapper

@measure_time
def slow_function():
    time.sleep(2)

slow_function()  # Tiempo de ejecución: 2.00099991768728

**En este ejemplo, el decorador measure_time se utiliza para medir el tiempo de ejecución de la función slow_function. Se utiliza la biblioteca time para obtener el tiempo actual antes y después de llamar a la función, y se calcula la diferencia para determinar el tiempo de ejecución.**

**Estos son solo algunos ejemplos de decoradores en Python. Los decoradores pueden ser utilizados para agregar funcionalidades adicionales a las funciones y clases, como la caché, la validación de argumentos, la medición del tiempo de ejecución, entre otros.**

Aquí hay algunos conceptos clave relacionados con los decoradores:

**Decorador simple: Un decorador simple es una función que toma una función como argumento y devuelve una nueva función que modifica el comportamiento de la función original. Por ejemplo:**

def decorador(funcion):
    def nueva_funcion(*args, **kwargs):
        # Lógica adicional antes de llamar a la función original
        resultado = funcion(*args, **kwargs)
        # Lógica adicional después de llamar a la función original
        return resultado
    return nueva_funcion

**Luego, puedes aplicar el decorador a una función utilizando la sintaxis @nombre_del_decorador:**

@decorador
def mi_funcion(x, y):
    return x + y

**Decorador de clase: Un decorador de clase es una función que se utiliza para modificar la clase antes de que se cree una instancia de ella. Se utiliza para agregar funcionalidad a la clase sin modificar su código fuente. Por ejemplo:**

def decorador_de_clase(clase):
    class ClaseModificada(clase):
        # Agregar métodos o atributos adicionales a la clase
        def nuevo_metodo(self):
            print("Este es un nuevo método agregado por el decorador.")
    return ClaseModificada

**Luego, puedes aplicar el decorador a una clase utilizando la sintaxis @nombre_del_decorador:**

@decorador_de_clase
class MiClase:
    def __init__(self, valor):
        self.valor = valor

Decoradores de función y método: **También puedes aplicar decoradores a métodos de una clase. Para hacer esto, simplemente coloca el decorador antes del método dentro de la definición de la clase:**

class MiClase:
    @decorador
    def mi_metodo(self, x, y):
        return x + y

Decoradores de parámetros: Los decoradores también **se pueden aplicar a los parámetros de una función.**** Esto se conoce **como "decoradores de parámetros" y se utiliza para realizar tareas adicionales antes o después de llamar a la función.** 

Por ejemplo:

def decorador_de_parametro(funcion):
    def nueva_funcion(*args, **kwargs):
        # Lógica adicional antes de llamar a la función original
        resultado = funcion(*args, **kwargs)
        # Lógica adicional después de llamar a la función original
        return resultado
    return nueva_funcion

@decorador_de_parametro
def mi_funcion(x, y):
    return x + y

**Estos son solo algunos conceptos básicos sobre los decoradores en Python. Los decoradores pueden ser utilizados de manera muy poderosa para agregar funcionalidad adicional a las funciones y clases en Python.**

![image](https://github.com/ivandobarriocordon/PC6M3/assets/146997085/c142fe9c-5efa-43ff-91a9-145c44442790)









