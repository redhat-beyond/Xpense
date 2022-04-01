from django.db import models, migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from tips.models import Tip

        test_data = [
            ('Test User1', 'A simple test message', 'Rent'),
            ('Test User2', 'Another simple test message', 'Rent'),
        ]

        with transaction.atomic():
            for author, text in test_data:
                Tip(author=author, text=text).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
