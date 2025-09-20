{
    "name": "{{ cookiecutter.module_title }}",
    "version": "{{ cookiecutter.version }}",
    "summary": "{{ cookiecutter.summary }}",
    "author": "{{ cookiecutter.author }}",
    "license": "{{ cookiecutter.license }}",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/integration_settings_views.xml"
    ],
    "installable": True,
}