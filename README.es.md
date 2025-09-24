# Plantilla de Módulo de Integración en Odoo

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Odoo](https://img.shields.io/badge/Odoo-18.0-purple)
![Status](https://img.shields.io/badge/status-active-success)

> 🇬🇧 **Prefer English?** [Read this README in English 🇬🇧](./README.md)

Plantilla basada en **Cookiecutter** para crear **módulos de integración en Odoo 18**.  
Permite a cualquier desarrollador generar rápidamente un módulo personalizado para conectar Odoo con APIs externas, webhooks o servicios de terceros.  

---

## 🔹 Qué incluye la plantilla

- **Estructura base del módulo** siguiendo buenas prácticas de Odoo.  
- **Cliente HTTP** → `models/integration_client.py` para consumir APIs externas.  
- **Controlador de Webhooks** → `controllers/webhook.py` para manejar eventos entrantes.  
- **Vista de Configuración** → `views/integration_settings_views.xml` para guardar credenciales.  
- **Seguridad básica** → `security/ir.model.access.csv` y `security.xml`.  
- **Tareas programadas de ejemplo (CRON)** → `data/ir_cron_data.xml`.  
- **Prueba unitaria inicial** → `tests/test_integration.py`.  
- **Pipeline de CI/CD** → GitHub Actions (`.github/workflows/ci.yml`) con validaciones básicas.  
- **Documentación por módulo** → `README_MODULE.md`.  
- **Configuración de Cookiecutter** → `cookiecutter.json` para definir variables del proyecto.  

---

## 🚀 Cómo usar esta plantilla

### 1. Requisitos  

- [Python 3.8+](https://www.python.org/downloads/)  
- [Cookiecutter](https://cookiecutter.readthedocs.io/)


Instalar Cookiecutter:  

```bash
pip install cookiecutter
```

### 2. Generar un nuevo módulo de integración en Odoo

Ejecuta:

```bash
cookiecutter https://github.com/tu-usuario/odoo-integration-template.git
```

Se te pedirá ingresar algunas variables (definidas en `cookiecutter.json`):

- `module_name`: Nombre técnico del módulo
- `description`: Breve descripción
- `author`: Autor del módulo
- `version`: Versión inicial

Esto generará una carpeta con un módulo listo para personalizar.

---
## 📂 Estructura del módulo generado

```bash
{{module_name}}/
├─ __init__.py
├─ __manifest__.py                  # Metadatos del módulo Odoo
├─ models/
│  ├─ __init__.py
│  └─ integration_client.py         # Cliente API
├─ controllers/
│  ├─ __init__.py
│  └─ webhook.py                    # Endpoints para webhooks
├─ security/
│  ├─ ir.model.access.csv           # Permisos de acceso
│  └─ security.xml                  # Reglas de seguridad
├─ views/
│  └─ integration_settings_views.xml# Vistas de configuración
├─ data/
│  └─ ir_cron_data.xml              # Tareas programadas (CRON)
├─ tests/
│  └─ test_integration.py           # Pruebas unitarias
└─ README_MODULE.md                 # Documentación del módulo
```
---
## 🛠 Personalización

- Editar `integration_client.py` → Implementar llamadas a la API externa.
- Modificar `webhook.py` → Definir endpoints de integración.
- Ajustar `integration_settings_views.xml` → Añadir configuraciones en la UI.
- Cambiar `ir_cron_data.xml` → Definir sincronizaciones automáticas.
- Ampliar `test_integration.py` → Crear pruebas unitarias y de integración.

---

## ⚙️ CI/CD

La plantilla incluye un flujo de trabajo en `.github/workflows/ci.yml` con validaciones:

- Lint de Python
- Verificación de estructura de Odoo

Puedes ampliarlo para:

- Ejecutar pruebas unitarias
- Análisis de calidad de código
- Tests en contenedores de Odoo

---

## 📖 Documentación

Cada módulo generado incluye un archivo `README_MODULE.md` con instrucciones específicas:

- Instalación
- Configuración
- Uso
- Extensión

---

## 📜 Licencia

Este proyecto está bajo licencia **MIT**.
Eres libre de usarlo, modificarlo y distribuirlo.

---
## 📫 Contacto

- 📧 Email: macpdleonr@macleondev.com
- 🌐 Sitio: www.macleondev.com

---

## ⭐ ¿Te gustó el proyecto?
¡Dale una estrella ⭐ en GitHub y sígueme para más proyectos como este!
