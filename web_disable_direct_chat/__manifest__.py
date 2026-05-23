# Copyright 2026 Ctrl-a
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

{
    "name": "Web Disable Direct Chat",
    "summary": "Disable direct chat features while preserving technical messages",
    "version": "16.0.1.0.0",
    "development_status": "Alpha",
    "category": "Hidden",
    "website": "https://github.com/OCA/web",
    "author": "Ctrl-a, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["mail"],
    "assets": {
        "web.assets_backend": [
            "/web_disable_direct_chat/static/src/scss/web_disable_direct_chat.scss",
        ],
    },
}
