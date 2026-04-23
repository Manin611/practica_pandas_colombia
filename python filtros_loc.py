import pandas as pd

data = {
    'Nombre': [
        'Juan Gómez', 'Elena Marín', 'Carlos Ruiz', 'Diana Toro', 'Andrés Felipe', 'Sofía Mesa', 'Mateo Cano', 'Laura Gil', 'Diego León', 'Sara Ortiz',
        'Luis Ángel', 'Marta Lucía', 'Hugo Posada', 'Paula Ríos', 'Simón Vélez', 'Valentina Paz', 'Jorge Eli', 'Camila Luz', 'Samuel Sol', 'Valeria Mar',
        'Ricardo Rey', 'Patricia San', 'Fernando Joy', 'Gloria Esperanza', 'Oscar Darío', 'Clara Inés', 'Iván René', 'Beatriz Pin', 'Mauricio Al', 'Claudia Sol',
        'Gabriel Jaime', 'Adriana María', 'Wilson Fer', 'Sandra Milena', 'Jairo Hernán', 'Natalia Andrea', 'César Augusto', 'Yolanda Estela', 'Héctor Fabio', 'Mónica Liz',
        'Ramiro José', 'Tatiana Marcela', 'Alvaro Javier', 'Lina Fernanda', 'Gonzalo Antonio', 'Angélica María', 'Esteban David', 'Silvia Juliana', 'Roberto Carlos', 'Ximena Paz'
    ],
    'Edad': [25, 34, 45, 28, 31, 23, 40, 29, 37, 26, 52, 41, 33, 27, 30, 24, 48, 32, 29, 35, 39, 44, 27, 50, 31, 36, 42, 28, 33, 46, 29, 38, 43, 31, 47, 25, 34, 41, 55, 30, 37, 26, 44, 28, 51, 32, 24, 33, 49, 27],
    'Ciudad': ['Medellín', 'Bogotá', 'Cali', 'Barranquilla', 'Medellín', 'Envigado', 'Bogotá', 'Sabaneta', 'Pereira', 'Bucaramanga', 'Medellín', 'Cali', 'Bogotá', 'Medellín', 'Itagüí', 'Cali', 'Barranquilla', 'Medellín', 'Bogotá', 'Cali', 'Medellín', 'Bogotá', 'Manizales', 'Pereira', 'Envigado', 'Cali', 'Medellín', 'Bogotá', 'Bucaramanga', 'Itagüí', 'Medellín', 'Bogotá', 'Cali', 'Medellín', 'Sabaneta', 'Cali', 'Barranquilla', 'Medellín', 'Bogotá', 'Cali', 'Medellín', 'Bogotá', 'Manizales', 'Pereira', 'Envigado', 'Cali', 'Medellín', 'Bogotá', 'Bucaramanga', 'Itagüí'],
    'Nivel_Estudio': ['Pregrado', 'Maestría', 'Doctorado', 'Tecnología', 'Especialización', 'Pregrado', 'Maestría', 'Especialización', 'Pregrado', 'Tecnología', 'Doctorado', 'Maestría', 'Pregrado', 'Especialización', 'Tecnología', 'Pregrado', 'Maestría', 'Doctorado', 'Pregrado', 'Especialización', 'Maestría', 'Doctorado', 'Pregrado', 'Maestría', 'Tecnología', 'Especialización', 'Doctorado', 'Pregrado', 'Maestría', 'Especialización', 'Pregrado', 'Doctorado', 'Maestría', 'Tecnología', 'Especialización', 'Pregrado', 'Maestría', 'Doctorado', 'Pregrado', 'Especialización', 'Maestría', 'Pregrado', 'Doctorado', 'Pregrado', 'Maestría', 'Especialización', 'Tecnología', 'Doctorado', 'Pregrado', 'Especialización'],
    'Experiencia_Años': [2, 8, 15, 4, 7, 1, 12, 5, 10, 3, 20, 14, 9, 4, 6, 2, 18, 6, 5, 9, 11, 16, 3, 22, 7, 10, 15, 4, 8, 17, 5, 12, 14, 6, 19, 2, 9, 13, 25, 7, 12, 3, 16, 5, 20, 8, 2, 11, 23, 6],
    'Salario_COP': [3500000, 7500000, 15000000, 2800000, 5200000, 3100000, 9000000, 4800000, 6000000, 2500000, 18000000, 8200000, 5500000, 4500000, 3200000, 3300000, 11000000, 14000000, 4200000, 6500000, 8800000, 16500000, 3800000, 9500000, 3000000, 5800000, 15500000, 4000000, 7800000, 6200000, 4400000, 17000000, 8500000, 3100000, 5900000, 3200000, 8900000, 14500000, 5000000, 6100000, 9200000, 3900000, 16000000, 4300000, 9800000, 6300000, 2900000, 15200000, 4800000, 6000000],
    'Remoto': [True, False, False, True, True, False, True, False, True, False, False, True, False, True, False, True, False, True, False, True, False, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False]
}
df = pd.DataFrame(data)

print("\n--- 1. Primeros Registros: Primeras 5 filas (posiciones 0 a 4) ---")
print(df.iloc[0:5])

print("\n--- 2. Punto Central: Datos de la fila en posición 24 ---")
print(df.iloc[24])

print("\n--- 3. Columnas Alternas: Índices 0, 2 y 5 para las primeras 10 filas ---")
print(df.iloc[0:10, [0, 2, 5]])

print("\n--- 4. Dato Específico: Valor de la celda en la fila 10, columna 3 ---")
print(df.iloc[10, 3])

print("\n--- 5. Último Decil: Últimas 10 filas usando slicing negativo ---")
print(df.iloc[-10:])

print("\n--- 6. Subsección de Matriz: Desde fila 15 a 25, columna 1 a 4 ---")
print(df.iloc[15:26, 1:5])

print("\n--- 7. Propiedades Finales: Todas las filas, últimas 2 columnas ---")
print(df.iloc[:, -2:])

print("\n--- 8. Muestreo Estratificado: Filas 0, 10, 20, 30, 40 y columnas 0 y 5 ---")
print(df.iloc[[0, 10, 20, 30, 40], [0, 5]])

print("\n--- 9. Segmento Final: Primeras 3 columnas de las últimas 10 filas (40 a 50) ---")
print(df.iloc[40:51, 0:3])

print("\n--- 10. Inversión: DataFrame con filas en orden inverso ---")
print(df.iloc[::-1])










