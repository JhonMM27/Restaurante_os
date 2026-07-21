from django.db import migrations

def assign_default_images(apps, schema_editor):
    Plato = apps.get_model('menu', 'Plato')
    image_mapping = {
        'ceviche': 'platos/ceviche.png',
        'tequeños': 'platos/tequenos.png',
        'tequenos': 'platos/tequenos.png',
        'lomo saltado': 'platos/lomo_saltado.png',
        'aji de gallina': 'platos/aji_de_gallina.png',
        'ají de gallina': 'platos/aji_de_gallina.png',
        'inca kola': 'platos/inca.png',
        'inca': 'platos/inca.png',
        'pisco sour': 'platos/pisco.png',
        'pisco': 'platos/pisco.png',
        'arroz con pollo': 'platos/arroz_con_pollo.png',
        'arroz con pato': 'platos/arroz_con_pato.png',
        'cabrito': 'platos/cabrito_a_la_nortena.png',
        'chicharrones': 'platos/chicharrones.png',
        'cuy': 'platos/cuy_con_papas.png',
        'chicha': 'platos/chicha.png',
        'cerveza': 'platos/cerveza.png',
    }
    for plato in Plato.objects.all():
        if not plato.imagen:
            nombre_lower = plato.nombre.lower().strip()
            for key, img_path in image_mapping.items():
                if key in nombre_lower:
                    plato.imagen = img_path
                    plato.save(update_fields=['imagen'])
                    break

def reverse_assign_default_images(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_plato_control_stock_plato_stock_actual_and_more'),
    ]

    operations = [
        migrations.RunPython(assign_default_images, reverse_assign_default_images),
    ]
