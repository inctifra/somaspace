from django.contrib import admin


class SomaSpaceAdminSite(admin.AdminSite):
    index_title = "Somaspace"
    site_title = "Somaspace Admin"
    site_header = "Somaspace Administration"


somaspace_admin_site = SomaSpaceAdminSite(name="Somaspace")
