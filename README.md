# Punto de Control 6 Checkpoint 3 

¡Buenas! Dejo aquí la respuesta de las preguntas teoricas respectivas al **Punto de Control 6 del Modulo 3.**

## 1-¿Para qué usamos Clases en Python?
 Lo que nos permiten hacer **las clases en Python es crear modelos de objetos que representan entidades en nuestro código**. Puedes definir **atributos (variables) y métodos (funciones)** que <u>describen las características y comportamientos de una entidad</u>. 
 Al crear instancias de una clase, **puedes tener objetos que representan diferentes instancias de esa entidad**. 

 Cuando definimos una clase podemos crear una serie de instancias de esa clase que contienen **datos y comportamientos relacionados**.

 Las clases **nos permiten reutilizar código escribiendo funciones y métodos que se aplican a todas las instancias de una clase**.Esto nos ahorra tiempo y nos permite **escribir código más conciso y legible**. 

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


## 2-¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
 El metodo al que se refiere la pregunta **es el método "Constructor" o "Método de inicialización"**, este **se ejecuta automáticamente cuando se crea una instancia de una clase**. Una explicacion sencilla de como funciona este método es que **se utiliza para inicializar los atributos de una instancia de una clase**. <u>Al crear una instancia de una clase, el constructor se ejecuta automáticamente y te permite establecer valores iniciales para los atributos de la instancia</u>. 
 
 **El constructor también puede realizar otras tareas de configuración y preparación inicial.**

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

## 4-¿Es MongoDB una base de datos SQL o NoSQL?
MongoDB **es una base de datos NoSQL porque no sigue el modelo relacional tradicional de bases de datos SQL**. En lugar de utilizar tablas con esquemas fijos y relaciones entre ellas, **MongoDB utiliza documentos JSON-like para almacenar datos**. **Cada documento puede tener una estructura diferente y puede contener campos y valores arbitrarios.** 

Esto permite una flexibilidad y escalabilidad adicional en la estructura y el modelo de datos.

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
print("Mensaje:", mensaje)

    
## 5-¿Qué es Postman?
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




## 6-¿Qué es el polimorfismo?
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

## 7-¿Qué es un método dunder?
   Un método dunder (o "dunder" por sus siglas en inglés) **es un método especial en Python que está precedido por doble guion bajo (__) y que tiene una funcionalidad especial en las clases.** **Los métodos dunder se utilizan para sobrecargar operaciones y proporcionar funcionalidades especiales en Python.**
Los métodos dunder **se utilizan para personalizar el comportamiento de las clases en Python.** **Proporcionan una forma de definir cómo se comportan las clases cuando se utilizan operaciones o métodos específicos.** 

**Por ejemplo, los métodos dunder se utilizan para sobrecargar operaciones como la suma (+), la multiplicación (*), el acceso a atributos (.), entre otros.**

Aquí hay algunos ejemplos de métodos dunder comunes en Python:
__init__: Método especial utilizado para inicializar un objeto de una clase.
__str__: Método especial utilizado para definir la representación en forma de cadena de un objeto.
__len__: Método especial utilizado para definir la longitud de un objeto.
__add__: Método especial utilizado para sobrecargar la operación de suma (+).
__mul__: Método especial utilizado para sobrecargar la operación de multiplicación (*).
__getattr__: Método especial utilizado para definir el comportamiento de acceso a atributos (.).

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









