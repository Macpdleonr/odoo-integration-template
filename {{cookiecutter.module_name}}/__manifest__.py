{
    "name": "{{ cookiecutter.module_title }}",
    "version": "{{ cookiecutter.version }}",
    "summary": "{{ cookiecutter.summary }}",
    "description": """
        {{cookiecutter.description}}
        ============================
        Integration module in Odoo to connect with external services.
    """,
    "author": "{{ cookiecutter.author }}",
    "website": "{{ cookiecutter.website }}",
    "category": "{{ cookiecutter.category }}",
    "depends": {{ cookiecutter.depends }},
    "data": [
        "security/ir.model.access.csv",
        "views/res_config_settings_views.xml",
        "data/ir_cron_data.xml",
    ],
    "installable": True,
    "application": True,
    'auto_install': False,
    "license": "{{ cookiecutter.license }}",
}
