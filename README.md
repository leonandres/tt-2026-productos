# 🔹 Sistema de Gestión de Productos

Sistema de gestión de inventario desarrollado en Python que permite **agregar, mostrar, buscar y eliminar productos** con almacenamiento persistente en archivos de texto.

---

## 🔹 Objetivos

Desarrollar un sistema funcional de gestión de productos que garantice la **persistencia de datos** mediante archivos de texto (.txt), superando las limitaciones de almacenamiento en memoria RAM de versiones anteriores.

---

## 🔹 Funcionalidades

- ✅ **Agregar productos**: Registro de nuevos productos con validación de campos.
- 📋 **Mostrar productos**: Visualización completa del inventario.
- 🔍 **Buscar productos**: Localización de productos por coincidencia parcial o exacta.
- 🗑️ **Eliminar productos**: Eliminación de productos con confirmación.
- 💾 **Persistencia**: Los datos se guardan de forma persistente y permanecen al cerrar el programa.
- 🎨 **Interfaz en consola**: Menú estructurado con colores para mejorar la experiencia de usuario.

---

## 🔹 Tecnologías Utilizadas

- **Python 3.x**
- **Manejo de archivos**: Funciones nativas `open()`, `read()`, `write()` y modos `r`, `w`, `a`.
- **Validación de datos**: Métodos `strip()` e `isdigit()`.
- **Colores en consola**: Códigos y secuencias ANSI (`\033[`).

---

## 🔹 Instalación y Uso

1. **Clona este repositorio** en tu máquina local ejecutando:
   ```bash
   git clone https://github.com/leonandres/tt-2026-productos.git
   ```

2. **Navega a la carpeta de la entrega final** (versión persistente con archivos):
   ```bash
   cd tt-2026-productos/entrega-final
   ```

3. **Ejecuta la aplicación** con el siguiente comando:
   ```bash
   python main.py
   ```

---

## 🔹 Estructura del Proyecto

El repositorio se organiza de la siguiente manera según sus etapas de desarrollo:

```text
📂 tt-2026-productos/
├── 📂 pre-entrega/     # Versión inicial (almacenamiento temporal en memoria RAM)
│   └── 📄 main.py          # Código fuente de la primera entrega
└── 📂 entrega-final/   # Versión definitiva (almacenamiento persistente en archivos)
    └── 📄 main.py          # Código fuente principal de la aplicación final
```

---

## 🔹 Formato de Almacenamiento

En la versión final, el archivo persistente `productos.txt` (generado automáticamente tras agregar el primer elemento) utiliza una estructura de texto plano delimitada por comas:

```text
nombre, categoría, precio
```
