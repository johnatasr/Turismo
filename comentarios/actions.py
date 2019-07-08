def aprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=True)

def reprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=False)


aprova_comentarios.short_description = 'Aprovar Comentários'
reprova_comentarios.short_description = 'Reprovar Comentários'