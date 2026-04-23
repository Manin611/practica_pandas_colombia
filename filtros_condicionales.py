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

print("\n--- 1. Altos Ingresos: Salario superior a 10.000.000 ---")
print(df[df['Salario_COP'] > 10000000])

print("\n--- 2. Sede Principal: Empleados de Medellín ---")
print(df[df['Ciudad'] == 'Medellín'])

print("\n--- 3. Experiencia Sénior: Más de 15 años de experiencia ---")
print(df[df['Experiencia_Años'] > 15])

print("\n--- 4. Investigación Remota: Doctorado y Remoto ---")
print(df[(df['Nivel_Estudio'] == 'Doctorado') & (df['Remoto'] == True)])

print("\n--- 5. Segmento Joven: Edades entre 25 y 30 años inclusive ---")
print(df[(df['Edad'] >= 25) & (df['Edad'] <= 30)])

print("\n--- 6. Optimización en Bogotá: Ganan menos de 4.000.000 y viven en Bogotá ---")
print(df[(df['Salario_COP'] < 4000000) & (df['Ciudad'] == 'Bogotá')])

print("\n--- 7. Especialistas Valle: Profesionales de Cali con Especialización ---")
print(df[(df['Ciudad'] == 'Cali') & (df['Nivel_Estudio'] == 'Especialización')])

print("\n--- 8. Altos Salarios Junior: Experiencia < 5 años y salario > 4.000.000 ---")
print(df[(df['Experiencia_Años'] < 5) & (df['Salario_COP'] > 4000000)])

print("\n--- 9. Nivel Técnico: Nivel de estudio Tecnología o Pregrado ---")
print(df[df['Nivel_Estudio'].isin(['Tecnología', 'Pregrado'])])

print("\n--- 10. Presencialidad Santander: Bucaramanga y Presencial ---")
print(df[(df['Ciudad'] == 'Bucaramanga') & (df['Remoto'] == False)])