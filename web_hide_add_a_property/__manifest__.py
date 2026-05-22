# Copyright 2026 Ctrl-a
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

{
    "name": "Web Hide Add a property",
    "summary": "Hide the Add a property button globally",
    "version": "16.0.1.0.0",
    "development_status": "Alpha",
    "category": "Hidden",
    "website": "https://github.com/OCA/web",
    "author": "Ctrl-a, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["web"],
    "assets": {
        "web.assets_backend": [
            "/web_hide_add_a_property/static/src/scss/web_hide_add_a_property.scss",
        ],
    },
}
