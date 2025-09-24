# Odoo Integration Module Template

![License](https://img.shields.io/badge/License-MIT-green)

> 🇪🇸 **¿Prefieres español?** [Lee este README en español 🇪🇸](./README.es.md)

Template for creating **integration modules in Odoo**.
Allows any developer to quickly generate a custom module to connect Odoo with external APIs, webhooks, or other services.

---

## 🔹 What the template includes

- Base module folder with:
- HTTP client (`models/integration_client.py`) to consume external APIs.
- Webhook controller (`controllers/webhook.py`).
- Configuration view (`views/integration_settings_views.xml`) to save credentials.
- Basic security (`security/ir.model.access.csv` and `security.xml`).
- Sample data (`data/ir_cron_data.xml`) for automated jobs.
- Unit tests (`tests/test_integration.py`).
- Integration with GitHub Actions (`.github/workflows/ci.yml`) for basic linting.
- Module README (`README_MODULE.md`) explaining internal usage.
- `cookiecutter.json` file to customize the module when generating a new project.

---

## 🚀 How to use this template

### 1. Install Cookiecutter

If you don't have it installed, run:

```bash
pip install cookiecutter
```
# Odoo 18 Integration Module Template

Template for creating **integration modules in Odoo 18**.
Allows any developer to quickly generate a custom module to connect Odoo with external APIs, webhooks, or other services.

---

## 🔹 What the template includes

- Base module folder with:
- HTTP client (`models/integration_client.py`) to consume external APIs.
- Webhook controller (`controllers/webhook.py`).
- Configuration view (`views/integration_settings_views.xml`) to save credentials.
- Basic security (`security/ir.model.access.csv` and `security.xml`).
- Sample data (`data/ir_cron_data.xml`) for automated jobs.
- Unit tests (`tests/test_integration.py`).
- Integration with GitHub Actions (`.github/workflows/ci.yml`) for basic linting.
- Module README (`README_MODULE.md`) explaining internal usage.
- `cookiecutter.json` file to customize the module when generating a new project.

---

## 🚀 How to use this template

### 1. Install Cookiecutter

If you don't have it installed, run:

```bash
pip install cookiecutter

```