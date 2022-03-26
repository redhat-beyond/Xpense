from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Expenses",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Rent", "Rent"),
                            ("Mortgage", "Mortgage"),
                            ("bills", "Bills"),
                            ("Transportation", "Transportation"),
                            ("Clothing", "Clothing"),
                            ("Healthcare", "Healthcare"),
                            ("Food", "Food"),
                            ("Insurance", "Insurance"),
                            ("Kids", "Kids"),
                            ("Culture", "Culture"),
                            ("Vacations", "Vacations"),
                            ("Other", "Other"),
                        ],
                        default="Other",
                        max_length=32,
                    ),
                ),
            ],
        ),
    ]
