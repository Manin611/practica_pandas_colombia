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

print("\n--- 1. Nómina Básica: Columnas Nombre y Salario_COP ---")
print(df.loc[:, ['Nombre', 'Salario_COP']])

print("\n--- 2. Rango Geográfico: De la fila 10 a la 20, columnas Ciudad y Edad ---")
print(df.loc[10:20, ['Ciudad', 'Edad']])

print("\n--- 3. Búsqueda Nominal: Fila completa de Elena Marín ---")
df_indice_nombre = df.set_index('Nombre')
print(df_indice_nombre.loc['Elena Marín'])

print("\n--- 4. Habilidades Maestría: Experiencia_Años del nivel Maestría ---")
print(df.loc[df['Nivel_Estudio'] == 'Maestría', 'Experiencia_Años'])

print("\n--- 5. Región Caribe: Filas de Barranquilla, desde Nivel_Estudio hasta Remoto ---")
print(df.loc[df['Ciudad'] == 'Barranquilla', 'Nivel_Estudio':'Remoto'])

print("\n--- 6. Presupuesto Itagüí: Salario_COP de los profesionales en Itagüí ---")
print(df.loc[df['Ciudad'] == 'Itagüí', 'Salario_COP'])

print("\n--- 7. Muestreo Intercalado: Filas pares, columnas Nombre y Nivel_Estudio ---")
print(df.loc[::2, ['Nombre', 'Nivel_Estudio']])

print("\n--- 8. Veteranía: Mayores de 40 años, columnas Nombre y Remoto ---")
print(df.loc[df['Edad'] > 40, ['Nombre', 'Remoto']])

print("\n--- 9. Cierre de Lista: Últimos 5 registros usando etiquetas de índice ---")
print(df.loc[df.index[-5:]])

print("\n--- 10. Precisión de Años: Ciudad de quienes tienen 10 años exactos de experiencia ---")
print(df.loc[df['Experiencia_Años'] == 10, 'Ciudad'])