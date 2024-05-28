class Usuario:
  def __init__(self, username, password):
      self.username = username
      self.password = password

# Crear un objeto Usuario
usuario = Usuario("ejemplo_usuario", "contraseña_secreta")

# Imprimir el nombre de usuario y la contraseña del objeto Usuario
print("Nombre de usuario:", usuario.username)
print("Contraseña:", usuario.password)