{
    "name": "{{ cookiecutter.module_title }}",
    "version": "{{ cookiecutter.version }}",
    "summary": "{{ cookiecutter.summary }}",
    "description": """
        {{cookiecutter.module_name}}
        ============================
        Integration module in Odoo to connect with external services.
    """,
    "author": "{{ cookiecutter.author }}",
    "website": "https://github.com/{{cookiecutter.github_user}}",
    "category": "Integration",
    "license": "{{ cookiecutter.license }}",
    "depends": ["base", "web"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/integration_settings_views.xml",
        "data/ir_cron_data.xml",
    ],
    "installable": True,
    "application": False,
    "license": "MIT",
}