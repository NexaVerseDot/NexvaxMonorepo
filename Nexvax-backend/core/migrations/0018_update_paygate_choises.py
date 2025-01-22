from django.db import migrations, models
from core.lib.inouts import StripeGate

def get_choices():
    return [(StripeGate.ID, StripeGate.NAME)]

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0017_new_pair_params'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paygatetopup',
            name='gate_id',
            field=models.IntegerField(choices=get_choices()),
        ),
        migrations.AddField(
            model_name='paygatetopup',
            name='stripe_payment_intent',
            field=models.CharField(max_length=255, null=True, blank=True, db_index=True),
        ),
    ]