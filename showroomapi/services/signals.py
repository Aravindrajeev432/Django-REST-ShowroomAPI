from django.db.models import signals
from django.dispatch import receiver
from .models import Services, ServiceHistory,BayCurrentJob

from channels.layers import get_channel_layer
import asyncio


@receiver(signals.post_save, sender=Services)
def service_log_maker(sender, instance, created, using, **kwargs):
    if created:
        # We're looking for status change
        pass
    else:

        if instance.status == 'billing':

            parts = instance.parts_used.all()
            try:
                service_history = ServiceHistory.objects.get(service=instance)
                print('update')
            except ServiceHistory.DoesNotExist:
                part_total = 0
                labour_charge = 0
                for price in parts:
                    print(price.price)
                    part_total = part_total + price.price
                for price in parts:
                    labour_charge = labour_charge + price.labour_charge

                if instance.is_free:
                    total = part_total
                else:
                    total = part_total + labour_charge
                print(f'total for parts{part_total}')
                print(f'total for labour charge{labour_charge}')
                print("create a service log")
                #
                # amount = models.IntegerField()
                # parts_total = models.IntegerField()
                # labour_charge = models.IntegerField()
                #
                # is_free = models.BooleanField()

                history = ServiceHistory.objects.create(service=instance, amount=total, parts_total=part_total,
                                                        labour_charge=labour_charge, is_free=instance.is_free)

                history.save()

                bay = BayCurrentJob.objects.filter(current_job=instance).update(is_completed=True)
                BayDetails.objects.filter(advisor=instance.advisor).update(status='free')


@receiver(signals.pre_save,sender=Services)
def notificatorofservice(sender,instance,using,**kwargs):

    print(instance.user_id)
    print(f'instance id{instance.id}')
    channel_layer = get_channel_layer()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(channel_layer.group_send(
        'notification_'+str(instance.user_id),
        {
            'type': 'notificator',
            'message': 'my message'
        }
    ))
