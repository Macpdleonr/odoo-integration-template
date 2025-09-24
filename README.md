# Odoo Integration Module Template

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Odoo](https://img.shields.io/badge/Odoo-18.0-purple)
![Status](https://img.shields.io/badge/status-active-success)

> 🇪🇸 **¿Prefieres español?** [Lee este README en español 🇪🇸](./README.es.md)

**A Cookiecutter-based template** for creating **integration modules in Odoo**.
It allows developers to quickly generate a custom Odoo module for connecting with external APIs, webhooks, or third-party services.

---
## 🔹Features Included

- **Module boilerplate** with standard Odoo structure.
- **HTTP client** → `models/integration_client.py` to consume external APIs.
- **Webhook controller** → `controllers/webhook.py` to handle incoming events.
- **Configuration view** → `views/integration_settings_views.xml` for storing credentials.
- **Basic security setup** → `security/ir.model.access.csv` and `security.xml`.
- **Sample CRON jobs** → `data/ir_cron_data.xml` for scheduled syncs.
- **Unit test example** → `tests/test_integration.py`.
- **CI/CD workflow → GitHub Actions** (`.github/workflows/ci.yml`) with basic linting.
- **Per-module documentation** → `README_MODULE.md`.
- **Cookiecutter config** → `cookiecutter.json` for defining project variables.

---

## 🚀 Usage
### 1. Requirements:
- [Python 3.8+](https://www.python.org/downloads/)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)

Install Cookiecutter:

```bash
pip install cookiecutter
```

### 2. Generate a new Odoo integration module:
Run:
```bash
cookiecutter https://github.com/your-username/odoo-integration-template.git
```
You will be prompted for some variables (defined in `cookiecutter.json`):

- `module_name`: Module technical name
- `description`: Short description
- `author`: Module author
- `version`: Starting version

This will create a new Odoo module folder ready for customization.

---

## 📂 Structure of the Generated Module

```bash
{{module_name}}/
├─ __init__.py
├─ __manifest__.py                  # Odoo module metadata
├─ models/
│  ├─ __init__.py
│  └─ integration_client.py         # API client
├─ controllers/
│  ├─ __init__.py
│  └─ webhook.py                    # Webhook endpoints
├─ security/
│  ├─ ir.model.access.csv           # Access control
│  └─ security.xml                  # Security rules
├─ views/
│  └─ integration_settings_views.xml# Configuration views
├─ data/
│  └─ ir_cron_data.xml              # CRON jobs
├─ tests/
│  └─ test_integration.py           # Unit tests
└─ README_MODULE.md                 # Instructions for this module
```

---

## 🛠 Customization

- Extend `integration_client.py` → Implement your API calls.
- Modify `webhook.py` → Define webhook endpoints.
- Update `integration_settings_views.xml` → Add UI settings for users.
- Adjust `ir_cron_data.xml` → Define background jobs.
- Expand `test_integration.py` → Add integration and unit tests.

---

## ⚙️ CI/CD

The included GitHub Actions pipeline (`.github/workflows/ci.yml`) validates your module with:

- Python linting
- Odoo structure checks

You can extend it with:

- Unit tests execution
- Static code analysis
- Odoo test containers

---

## 📖 Documentation

Each generated module includes its own `README_MODULE.md` file with instructions for installation, configuration, and usage.

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it.

---

## 📫 Contact
- 📧 Email: macpdleonr@macleondev.com

- 🌐 Website: www.macleondev.com

---

## ⭐ Like the project?
Give it a ⭐ on GitHub and follow for more projects like this!
