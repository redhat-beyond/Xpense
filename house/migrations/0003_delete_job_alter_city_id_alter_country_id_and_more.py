from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_add_initial_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='house',
            name='parent_profession_1',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student'), (
                'Programmer', 'Programmer'), ('Artist', 'Artist'), ('Manager', 'Manager'), ('Army', 'Army'), (
                    'Police', 'Police'), ('Doctor', 'Doctor'), ('Vet', 'Vet'), ('Nurse', 'Nurse'), (
                        'Technichian', 'Technichian'), ('Cleaner', 'Cleaner'), ('Other', 'Other'), (
                            'Unemployed', 'Unemployed')], default='Other', max_length=50),
        ),
        migrations.AlterField(
            model_name='house',
            name='parent_profession_2',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student'), (
                'Programmer', 'Programmer'), ('Artist', 'Artist'), ('Manager', 'Manager'), ('Army', 'Army'), (
                    'Police', 'Police'), ('Doctor', 'Doctor'), ('Vet', 'Vet'), ('Nurse', 'Nurse'), (
                        'Technichian', 'Technichian'), ('Cleaner', 'Cleaner'), ('Other', 'Other'), (
                            'Unemployed', 'Unemployed')], default='Other', max_length=50),
        ),
    ]
